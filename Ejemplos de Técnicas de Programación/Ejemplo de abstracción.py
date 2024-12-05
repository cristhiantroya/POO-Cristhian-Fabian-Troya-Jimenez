# Definición de la clase Libro
class Libro:
    # Constructor de la clase, se llama al crear una nueva instancia de Libro
    def __init__(self, titulo, autor, fecha_publicacion):
        # Inicializa los atributos del libro con los valores proporcionados
        self.titulo = titulo  # Título del libro
        self.autor = autor  # Autor del libro
        self.fecha_publicacion = fecha_publicacion  # Fecha de publicación del libro

    # Método para obtener el título del libro
    def obtener_titulo(self):
        return self.titulo  # Retorna el título del libro

    # Método para obtener el autor del libro
    def obtener_autor(self):
        return self.autor  # Retorna el autor del libro

    # Método para obtener la fecha de publicación del libro
    def obtener_fecha_publicacion(self):
        return self.fecha_publicacion  # Retorna la fecha de publicación del libro

# Crear una instancia de la clase Libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "1967")

# Imprimir información del libro utilizando los métodos definidos en la clase
print("Título:", libro1.obtener_titulo())  # Imprime el título del libro
print("Autor:", libro1.obtener_autor())  # Imprime el autor del libro
print("Fecha de Publicación:", libro1.obtener_fecha_publicacion())  # Imprime la fecha de publicación del libro