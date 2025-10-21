import factory
import movie

if __name__=='__main__':
    mi_gestor = factory.get_sistema_persistencia()

    movie = movie.Movie('Star Wars Episodio IV', 'George Lucas', 98)

    mi_gestor.create(movie)