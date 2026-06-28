# Sistema de Gestion de Biblioteca Digital

Trabajo Practico Final - Programacion Avanzada (189)
Universidad Nacional Guillermo Brown

## Descripcion

Sistema en Python para administrar libros, usuarios y prestamos de una biblioteca digital, aplicando conceptos de Programacion Orientada a Objetos.

## Integrantes

- Nombre Apellido 1
- Nombre Apellido 2
- Nombre Apellido 3
- Nombre Apellido 4

## Requisitos

- Python 3.10+

## Ejecucion

```bash
python3 main.py
```

## Estructura del proyecto

```
├── main.py                  # Punto de entrada / demo
├── modelos/
│   ├── persona.py           # Clase abstracta Persona
│   ├── usuario.py           # Usuario, UsuarioRegular, UsuarioPremium
│   ├── libro.py             # Libro (metaclass MetaLibro)
│   └── prestamo.py          # Prestamo
├── servicios/
│   └── biblioteca.py        # Biblioteca (Singleton)
├── decoradores/
│   └── logger.py            # Decorador @log_operacion
├── metaclases/
│   └── metalibro.py         # Metaclase para ISBN unicos
├── tests/
├── uml/
│   └── diagrama.png
├── README.md
└── AGENTS.md
```

## Conceptos POA implementados

- **Herencia**: Persona -> Usuario -> UsuarioRegular / UsuarioPremium
- **Polimorfismo**: obtener_tipo_usuario() y calcular_limite_prestamos()
- **Agregacion**: Biblioteca agrega Libros y Usuarios
- **Composicion**: Biblioteca compone Prestamos
- **Decorador**: @log_operacion para trazabilidad
- **Metaclase**: MetaLibro (type) para evitar ISBN duplicados
- **Singleton**: Biblioteca como unica instancia
