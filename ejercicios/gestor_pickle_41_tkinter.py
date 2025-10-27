import os
import pickle

class GestorPickle():
    @staticmethod
    def get_nombre_fichero(titulo):
        return titulo.lower().replace(' ','_')+'.pckl'

    def create(self, movie : Pelicula):
        nombre_fichero = GestorPickle.get_nombre_fichero(movie.titulo)
        with open(nombre_fichero, mode='wb') as fichero:
            pickle.dump(movie, fichero)

    def find_by_title(self, title : str):
        nombre_fichero = GestorPickle.get_nombre_fichero(title)
        with open(nombre_fichero, mode='rb') as fichero:
            pelicula = pickle.load(fichero)
        return pelicula

    def delete(self, title : str):
        nombre_fichero = GestorPickle.get_nombre_fichero(title)
        os.remove(nombre_fichero)

    def update(self, updated_movie : Pelicula):
        self.create(updated_movie)