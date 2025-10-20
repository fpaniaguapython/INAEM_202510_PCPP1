'''
Construir un decorador que genere una ficha con los nombres y los valores
de los atributos del primer argumento de la función que decora.

El decorador recibe como argumento:
0, para generar la ficha en HTML.
1, para generar la ficha en XML.

Las fichas se guardan en los ficheros 'fichas_html.txt' o 'fichas_xml.txt'
'''
class Pelicula:
    def __init__(self, titulo, director, duracion):
        self.titulo = titulo
        self.director = director
        self.duracion = duracion

et = Pelicula('ET','Spielberg',92)

