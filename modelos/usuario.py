from .persona import Persona


class Usuario(Persona):
    def __init__(self, nombre, apellido, dni, email):
        super().__init__(nombre, apellido, dni)
        self.email = email

    def obtener_tipo_usuario(self):
        return "Usuario"


class UsuarioRegular(Usuario):
    def __init__(self, nombre, apellido, dni, email):
        super().__init__(nombre, apellido, dni, email)

    def calcular_limite_prestamos(self):
        return 3

    def obtener_tipo_usuario(self):
        return "Regular"


class UsuarioPremium(Usuario):
    def __init__(self, nombre, apellido, dni, email):
        super().__init__(nombre, apellido, dni, email)

    def calcular_limite_prestamos(self):
        return 10

    def obtener_tipo_usuario(self):
        return "Premium"
