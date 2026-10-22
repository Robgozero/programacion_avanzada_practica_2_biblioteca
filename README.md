# Práctica 2: Sistema básico de biblioteca

**Materia:** Programación Avanzada  
**Unidad:** Clases, encapsulamiento y colecciones  
**Archivo principal:** `biblioteca.py`

## Descripción

Programa de consola que simula una biblioteca pequeña. Permite registrar libros, mostrar los disponibles y realizar la solicitud de un libro por parte de un usuario.

## Clases y conceptos aplicados

- **`Libro`:** almacena título y autor. El estado de disponibilidad está encapsulado en el atributo privado `__disponible`. Incluye métodos para consultar información, prestar y devolver el libro.
- **`Usuario`:** almacena el nombre y permite solicitar un libro.
- **`Biblioteca`:** administra una colección (`list`) de objetos `Libro`, permite agregar libros y mostrar los disponibles.
- **Interacción entre objetos:** un usuario solicita un libro; el objeto Libro cambia su estado de disponible a prestado y la biblioteca actualiza la lista de disponibles.

## Cómo ejecutar

Requiere Python 3 y no necesita bibliotecas adicionales.

```bash
python biblioteca.py
```

En algunos sistemas, utiliza `python3 biblioteca.py`.

## Resultado esperado

El programa agrega tres libros, muestra la colección disponible, registra el préstamo de *El principito* por parte de Ana López y vuelve a mostrar los libros disponibles. El libro prestado ya no aparece en esa lista.
