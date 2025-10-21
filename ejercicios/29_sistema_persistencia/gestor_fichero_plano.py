from gestor import GestorPersistenciaBase
from movie import Movie

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
        raise NotImplementedError()

    def update(self, updated_movie : Movie):
        raise NotImplementedError()
    
if __name__=='__main__':
    #movie = Movie('El señor de los anillos', 'Peter Jackson', 280)
    #GestorFicheroPlano().create(movie)
    movie = GestorFicheroPlano().find_by_title('El señor de los anillos')
    print(movie)