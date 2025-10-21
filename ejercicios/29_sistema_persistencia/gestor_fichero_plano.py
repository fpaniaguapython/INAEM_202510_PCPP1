from gestor import GestorPersistenciaBase
from movie import Movie
import os

class GestorFicheroPlano(GestorPersistenciaBase):
    @staticmethod
    def get_nombre_fichero(titulo):
        return titulo.lower().replace(' ','_')+'.movie'

    def create(self, movie : Movie):
        nombre_fichero = GestorFicheroPlano.get_nombre_fichero(movie.titulo)
        with open(nombre_fichero, mode='w', encoding='utf-8') as fichero:
            fichero.write(movie.titulo)
            fichero.write('\n')
            fichero.write(movie.director)
            fichero.write('\n')
            fichero.write(str(movie.duracion))

    def find_by_title(self, title : str):
        nombre_fichero = GestorFicheroPlano.get_nombre_fichero(title)
        with open(nombre_fichero, mode='r', encoding='utf-8') as fichero:
            titulo = fichero.readline().replace('\n','')
            director = fichero.readline().replace('\n','')
            duracion = fichero.readline().replace('\n','')
            pelicula = Movie(titulo, director, duracion)
        return pelicula

    def delete(self, title : str):
        nombre_fichero = GestorFicheroPlano.get_nombre_fichero(title)
        os.remove(nombre_fichero)

    def update(self, updated_movie : Movie):
        self.create(updated_movie)