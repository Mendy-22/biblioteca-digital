from modelos.libro import Libro
from modelos.usuario import UsuarioRegular, UsuarioPremium
from servicios.biblioteca import Biblioteca
from datetime import date


def main():
    biblio = Biblioteca()

    print("=== ALTA DE LIBROS ===")
    libro1 = Libro("Cien anios de soledad", "Gabriel Garcia Marquez", "978-3-16-148410-0", 1967, 417)
    libro2 = Libro("El principito", "Antoine de Saint-Exupery", "978-0-14-243723-0", 1943, 96)
    biblio.alta_libro(libro1)
    biblio.alta_libro(libro2)

    print("\n=== MODIFICACION DE LIBRO ===")
    biblio.modificar_libro("978-3-16-148410-0", titulo="Cien anos de soledad", cantidad_paginas=432)
    lib = biblio.buscar_libro_por_isbn("978-3-16-148410-0")
    print(f"Titulo: {lib.titulo} | Paginas: {lib.cantidad_paginas}")

    print("\n=== ALTA DE USUARIOS ===")
    user1 = UsuarioRegular("Juan", "Perez", "12345678", "juan@email.com")
    user2 = UsuarioPremium("Maria", "Garcia", "87654321", "maria@email.com")
    biblio.registrar_usuario(user1)
    biblio.registrar_usuario(user2)

    print(f"Tipo: {user1.obtener_tipo_usuario()} | Limite: {user1.calcular_limite_prestamos()} prestamos")
    print(f"Tipo: {user2.obtener_tipo_usuario()} | Limite: {user2.calcular_limite_prestamos()} prestamos")

    print("\n=== MODIFICACION DE USUARIO ===")
    biblio.modificar_usuario("12345678", email="juan.perez@email.com")
    print(f"Nuevo email: {user1.email}")

    print("\n=== BAJA DE USUARIO ===")
    user3 = UsuarioRegular("Carlos", "Lopez", "11223344", "carlos@email.com")
    biblio.registrar_usuario(user3)
    print(f"Usuarios antes: {len(biblio.listar_usuarios())}")
    biblio.baja_usuario("11223344")
    print(f"Usuarios despues: {len(biblio.listar_usuarios())}")

    print("\n=== PRESTAMO ===")
    prestamo1 = biblio.registrar_prestamo(libro1, user1, date.today())
    print(f"Prestamo de '{libro1.titulo}' a {user1.nombre} registrado")

    print("\n=== VALIDACION: PRESTAMO DUPLICADO ===")
    try:
        biblio.registrar_prestamo(libro1, user2, date.today())
    except ValueError as e:
        print(f"Error capturado: {e}")

    print("\n=== PRESTAMOS ACTIVOS ===")
    activos = biblio.listar_prestamos_activos()
    print(f"Cantidad de prestamos activos: {len(activos)}")
    for p in activos:
        print(f"  - '{p.libro.titulo}' a {p.usuario.nombre} ({p.fecha_prestamo})")

    print("\n=== DEVOLUCION ===")
    biblio.registrar_devolucion("978-3-16-148410-0", "12345678")
    print("Libro devuelto")
    print(f"Prestamos activos restantes: {len(biblio.listar_prestamos_activos())}")

    print("\n=== VERIFICACION SINGLETON ===")
    biblio2 = Biblioteca()
    print(f"Misma instancia: {biblio is biblio2}")
    print(f"Libros en catalogo: {len(biblio2.listar_libros())}")

    print("\n=== METACLASE: ISBN DUPLICADO ===")
    try:
        Libro("Otro libro", "Autor", "978-3-16-148410-0", 2020, 200)
    except ValueError as e:
        print(f"Error capturado: {e}")

    print("\n=== LISTADO DE LIBROS ===")
    for l in biblio.listar_libros():
        print(f"  - {l.titulo} | {l.autor} | ISBN: {l.isbn}")

    print("\n=== LISTADO DE USUARIOS ===")
    for u in biblio.listar_usuarios():
        print(f"  - {u.nombre} {u.apellido} | DNI: {u.dni} | {u.obtener_tipo_usuario()}")

    print("\nSistema funcionando correctamente.")


if __name__ == "__main__":
    main()
