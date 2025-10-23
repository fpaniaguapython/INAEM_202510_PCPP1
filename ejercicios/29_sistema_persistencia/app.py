import factory
import movie

if __name__=='__main__':
    mi_gestor = factory.get_sistema_persistencia()
    #movie = movie.Movie('Jaws', 'John Carpenter', 90)
    #mi_gestor.create(movie)
    hw = mi_gestor.find_by_title('Jaws')
    print(hw)
    #movie = movie.Movie('Halloween', 'John Carpenter y L', 98)
    #mi_gestor.update(movie)
    #mi_gestor.delete('Halloween')
    