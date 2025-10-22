class Pelicula:
    pass

class ListaPelicula(list):
    def __init__(self, *args, **kwargs):
        print('Inicializando...')
        for item in args[0]:
            if not isinstance(item, Pelicula):
                raise TypeError('Solo se admiten películas')
        super().__init__(*args, **kwargs)

    def append(self, value):
        if not isinstance(value, Pelicula):
            raise TypeError('Solo se admiten películas')
        return super().append(value)
    
    def insert(self, index, object):
        if not isinstance(object, Pelicula):
            raise TypeError('Solo se admiten películas')
        return super().insert(index, object)
    
    def __setitem__(self, index, object):
        if not isinstance(object, Pelicula):
            raise TypeError('Solo se admiten películas')
        super().__setitem__(index, object)
    
# peliculas = ListaPelicula() # lista = list()
# peliculas = ListaPelicula(['grillo', Pelicula()])
peliculas = ListaPelicula([Pelicula(), Pelicula()])

peliculas.append(Pelicula())
peliculas.insert(0,Pelicula())
peliculas[1]=Pelicula()

print(peliculas)


