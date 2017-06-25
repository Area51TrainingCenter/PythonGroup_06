class Libro:
    def __init__(self, titulo, publicacion):
        self.titulo = titulo
        self.publicacion = publicacion


class Autor:
    def __init__(self, nombre, nacimiento):
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.libros = []

    def agregar_libro(self, titulo, publicacion):
        libro = Libro(titulo, publicacion)
        self.libros.append(libro)

    def mostrar(self):
        nombre_y_nacimiento = '{} - {}'.format(self.nombre, self.nacimiento)
        libros = []
        for libro in self.libros:
            libros.append('{} ({})'.format(libro.titulo, libro.publicacion))

        print('{}: {}'.format(nombre_y_nacimiento, ', '.join(libros)))

vargas_llosa = Autor(nombre='MVLL', nacimiento=1936)
vargas_llosa.agregar_libro(titulo='La casa verde', publicacion=1965)
vargas_llosa.agregar_libro(titulo='La ciudad y los perros', publicacion=1962)
pantaleon = Libro(titulo='Pantaleón y las visitadoras', publicacion=1973)
vargas_llosa.libros.append(pantaleon)
vargas_llosa.mostrar()  # => MVLL - 1936: La casa verde (1965), La ciudad y los perros (1962)
