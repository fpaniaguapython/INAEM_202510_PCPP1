import json
import os

from gestor import GestorPersistenciaBase
from movie import Movie

class GestorJSON(GestorPersistenciaBase):
    @staticmethod
    def get_nombre_fichero(titulo):
        return titulo.lower().replace(' ','_')+'.json'

    def create(self, movie : Movie):
        nombre_fichero = GestorJSON.get_nombre_fichero(movie.titulo)
        with open(nombre_fichero, mode='w', encoding='utf-8') as fichero:
            json.dump(movie.__dict__, fichero, ensure_ascii=False)

    def find_by_title(self, title : str):
        nombre_fichero = GestorJSON.get_nombre_fichero(title)
        with open(nombre_fichero, mode='r', encoding='utf-8') as fichero:
            diccionario = json.load(fichero)
            movie = Movie(**diccionario)
        return movie

    def delete(self, title : str):
        nombre_fichero = GestorJSON.get_nombre_fichero(title)
        os.remove(nombre_fichero)

    def update(self, updated_movie : Movie):
        self.create(updated_movie)
    
if __name__=='__main__':
    movie = Movie('El señor de los anillos', 'Peter Jackson', 280)
    GestorJSON().create(movie)