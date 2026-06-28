from decoradores.logger import log_operacion
from modelos.prestamo import Prestamo
from datetime import date


class Biblioteca:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.libros = []
            cls._instance.usuarios = []
            cls._instance.prestamos = []
        return cls._instance

    @log_operacion
    def alta_libro(self, libro):
        self.libros.append(libro)

    @log_operacion
    def baja_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                self.libros.remove(libro)
                return libro
        return None

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    @log_operacion
    def registrar_prestamo(self, libro, usuario, fecha_prestamo):
        if self.tiene_prestamo_activo(libro):
            raise ValueError(
                f"El libro '{libro.titulo}' ya tiene un prestamo activo"
            )
        prestamo = Prestamo(libro, usuario, fecha_prestamo)
        self.prestamos.append(prestamo)
        return prestamo

    @log_operacion
    def registrar_devolucion(self, isbn, dni):
        for prestamo in self.prestamos:
            if (prestamo.libro.isbn == isbn
                    and prestamo.usuario.dni == dni
                    and prestamo.fecha_devolucion is None):
                prestamo.fecha_devolucion = date.today()
                return prestamo
        return None

    def listar_libros(self):
        return self.libros.copy()

    def listar_usuarios(self):
        return self.usuarios.copy()

    def listar_prestamos(self):
        return self.prestamos.copy()

    def buscar_libro_por_isbn(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def modificar_libro(self, isbn, **kwargs):
        libro = self.buscar_libro_por_isbn(isbn)
        if not libro:
            return None
        for attr, valor in kwargs.items():
            if hasattr(libro, attr):
                setattr(libro, attr, valor)
        return libro

    def baja_usuario(self, dni):
        for usuario in self.usuarios:
            if usuario.dni == dni:
                self.usuarios.remove(usuario)
                return usuario
        return None

    def modificar_usuario(self, dni, **kwargs):
        for usuario in self.usuarios:
            if usuario.dni == dni:
                for attr, valor in kwargs.items():
                    if hasattr(usuario, attr):
                        setattr(usuario, attr, valor)
                return usuario
        return None

    def tiene_prestamo_activo(self, libro):
        for prestamo in self.prestamos:
            if prestamo.libro.isbn == libro.isbn and prestamo.fecha_devolucion is None:
                return True
        return False

    def listar_prestamos_activos(self):
        return [p for p in self.prestamos if p.fecha_devolucion is None]
