# Reglas Específicas del Proyecto

## Contexto

Este proyecto corresponde al Trabajo Práctico Final de Programación Avanzada.

El objetivo es desarrollar un Sistema de Gestión de Biblioteca Digital aplicando conceptos avanzados de Programación Orientada a Objetos.

El agente debe priorizar el cumplimiento de los requisitos académicos por encima de optimizaciones o arquitecturas alternativas.

---

# Arquitectura Obligatoria

## Patrón de Diseño

Se utilizará el patrón Singleton.

La clase `Biblioteca` debe existir como única instancia del sistema y centralizar:

* Gestión de libros.
* Gestión de usuarios.
* Gestión de préstamos.

No reemplazar Singleton por otros patrones sin autorización explícita.

---

# Modelo de Dominio

## Persona

Clase base abstracta.

Atributos mínimos:

* nombre
* apellido
* dni

Responsabilidad:

Representar información común de las personas del sistema.

---

## Usuario

Hereda de Persona.

Atributos adicionales:

* email

Responsabilidad:

Representar usuarios habilitados para solicitar préstamos.

---

## UsuarioRegular

Hereda de Usuario.

Debe implementar comportamiento específico para préstamos.

---

## UsuarioPremium

Hereda de Usuario.

Debe implementar comportamiento específico para préstamos.

---

## Libro

Atributos mínimos:

* titulo
* autor
* isbn
* anio_publicacion
* cantidad_paginas

Responsabilidad:

Representar material bibliográfico disponible.

---

## Prestamo

Atributos mínimos:

* libro
* usuario
* fecha_prestamo
* fecha_devolucion

Responsabilidad:

Representar una operación de préstamo.

---

## Biblioteca

Responsabilidad central del sistema.

Debe administrar:

* colección de libros
* colección de usuarios
* colección de préstamos

---

# Requisitos Académicos Obligatorios

## Herencia

Implementar:

Persona → Usuario

---

## Polimorfismo

Implementar mediante:

UsuarioRegular
UsuarioPremium

Ambas clases deben redefinir al menos un método común.

Ejemplo:

calcular_limite_prestamos()

o

obtener_tipo_usuario()

---

## Agregación

Biblioteca agrega:

* Usuarios
* Libros

Los objetos pueden existir independientemente de Biblioteca.

---

## Composición

Biblioteca compone:

* Préstamos

La vida útil del préstamo depende de Biblioteca.

---

## Decorador Propio

Implementar un decorador personalizado.

Objetivo recomendado:

Registrar operaciones importantes.

Ejemplos:

* alta_libro()
* baja_libro()
* registrar_prestamo()
* registrar_devolucion()

El decorador debe generar trazabilidad visible.

---

## Metaclase

Implementar utilizando `type` o una clase derivada de `type`.

Objetivo recomendado:

Garantizar ISBN únicos.

La metaclase debe impedir la creación de libros con ISBN duplicados.

---

# Restricciones de Desarrollo

No eliminar:

* Herencia
* Polimorfismo
* Decorador
* Metaclase
* Singleton

aunque existan alternativas más simples.

El cumplimiento de la consigna tiene prioridad.

---

# Estructura de Carpetas

project/

├── main.py

├── modelos/
│ ├── persona.py
│ ├── usuario.py
│ ├── libro.py
│ └── prestamo.py

├── servicios/
│ └── biblioteca.py

├── decoradores/
│ └── logger.py

├── metaclases/
│ └── metalibro.py

├── uml/
│ └── diagrama.png

├── tests/

├── README.md

└── AGENTS.md

---

# UML

Toda modificación de clases debe mantener consistencia con el UML.

Si se agrega una clase:

1. Actualizar UML.
2. Mantener relaciones correctas.
3. Documentar el cambio.

---

# Defensa del Trabajo

Toda decisión de diseño debe poder justificarse académicamente.

El agente debe favorecer soluciones simples, claras y fáciles de explicar durante una defensa oral.

Evitar patrones, frameworks o abstracciones innecesarias que compliquen la explicación del sistema.

---

# Criterio de Éxito

Una tarea se considera completada únicamente si:

* Compila correctamente.
* Cumple la consigna.
* Respeta la arquitectura acordada.
* Mantiene UML consistente.
* Mantiene documentación actualizada.
* Puede justificarse durante la defensa del TP.
