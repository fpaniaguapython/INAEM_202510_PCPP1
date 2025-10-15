'''
Crear una clase Pelicula
Atributos: Título, Director, Año
Métodos: 
- agregar_taquilla -> Añadir un nuevo atributo con el importe de la taquilla

1. Crear un película.
2. Mostrar por pantalla los atributos y los valores (no sabes cuales son)
3. Agregamos la taquilla
3. Mostrar por pantalla los atributos y los valores (no sabes cuales son)
'''
class Pelicula:
    def __init__(self, titulo, director, anyo):
        self.titulo = titulo
        self.director = director
        self.anyo = anyo

    def agregar_taquilla(self, importe_taquilla):
        self.importe_taquilla = importe_taquilla

pelicula_1 = Pelicula('Inception', 'Antonio', 2001)

atributos = pelicula_1.__dict__
# Opción Carlos
for at in atributos:
    print(at, getattr(pelicula_1, at))

# Opción Fernando
for nombre_atributo, valor_atributo in pelicula_1.__dict__.items():
    print(nombre_atributo.capitalize(), ':', valor_atributo)

pelicula_1.agregar_taquilla(1_000_000)

for nombre_atributo, valor_atributo in pelicula_1.__dict__.items():
    print(nombre_atributo.capitalize(), ':', valor_atributo)