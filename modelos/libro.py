from metaclases.metalibro import MetaLibro


class Libro(metaclass=MetaLibro):
    def __init__(self, titulo, autor, isbn, anio_publicacion, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.anio_publicacion = anio_publicacion
        self.cantidad_paginas = cantidad_paginas
