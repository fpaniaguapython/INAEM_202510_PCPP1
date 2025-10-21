from gestor import GestorPersistenciaBase
from movie import Movie

class GestorFicheroPlano(GestorPersistenciaBase):
    def create(self, movie : Movie):
        nombre_fichero = movie.titulo.lower().replace(' ','_')+'.movie'
        with open(nombre_fichero, mode='w', encoding='utf-8') as fichero:
            fichero.write(movie.titulo)
            fichero.write('\n')
            fichero.write(movie.director)
            fichero.write('\n')
            fichero.write(str(movie.duracion))

    def find_by_title(self, title : str):
        raise NotImplementedError()

    def delete(self, title : str):
        raise NotImplementedError()

    def update(self, updated_movie : Movie):
        raise NotImplementedError()
    
if __name__=='__main__':
    movie = Movie('El señor de los anillos', 'Peter Jackson', 280)
    GestorFicheroPlano().create(movie)