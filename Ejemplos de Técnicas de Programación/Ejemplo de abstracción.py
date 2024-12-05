class Libro:
    def __init__(self, titulo, autor, fecha_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion

    def obtener_titulo(self):
        return self.titulo

    def obtener_autor(self):
        return self.autor

    def obtener_fecha_publicacion(self):
        return self.fecha_publicacion

# Crear una instancia de la clase Libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "1967")

# Imprimir información del libro
print("Título:", libro1.obtener_titulo())
print("Autor:", libro1.obtener_autor())
print("Fecha de Publicación:", libro1.obtener_fecha_publicacion())