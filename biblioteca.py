# Unidad 2: Clases, encapsulamiento y colecciones
# Práctica 2: Sistema básico de biblioteca

class Libro:
    """Representa un libro y encapsula su estado de préstamo."""

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.__disponible = True

    def consultar_informacion(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        return f"'{self.titulo}' - {self.autor} | Estado: {estado}"

    def esta_disponible(self):
        return self.__disponible

    def prestar(self):
        if not self.__disponible:
            print(f'El libro "{self.titulo}" ya está prestado.')
            return False

        self.__disponible = False
        print(f'El libro "{self.titulo}" se ha prestado correctamente.')
        return True

    def devolver(self):
        if self.__disponible:
            print(f'El libro "{self.titulo}" ya estaba disponible.')
            return False

        self.__disponible = True
        print(f'El libro "{self.titulo}" se ha devuelto correctamente.')
        return True


class Usuario:
    """Representa a una persona que solicita libros."""

    def __init__(self, nombre):
        self.nombre = nombre

    def solicitar_libro(self, libro):
        print(f'\n{self.nombre} solicita "{libro.titulo}".')
        if libro.prestar():
            print(f'Préstamo registrado para {self.nombre}.')
        else:
            print("No fue posible completar el préstamo.")


class Biblioteca:
    """Administra una colección de objetos Libro."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f'Se agregó "{libro.titulo}" a la biblioteca.')

    def mostrar_libros_disponibles(self):
        print(f"\nLibros disponibles en {self.nombre}:")
        disponibles = [libro for libro in self.libros if libro.esta_disponible()]

        if not disponibles:
            print("No hay libros disponibles.")
            return

        for libro in disponibles:
            print(f"- {libro.consultar_informacion()}")


def main():
    biblioteca = Biblioteca("Biblioteca Central")

    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
    libro2 = Libro("El principito", "Antoine de Saint-Exupéry")
    libro3 = Libro("La ciudad y los perros", "Mario Vargas Llosa")

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    biblioteca.mostrar_libros_disponibles()

    usuario = Usuario("Ana López")
    usuario.solicitar_libro(libro2)

    biblioteca.mostrar_libros_disponibles()

    print("\nInformación del libro solicitado:")
    print(libro2.consultar_informacion())


if __name__ == "__main__":
    main()
