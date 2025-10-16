class Pelicula:
    def __init__(self, titulo, director, recaudacion):
        self.titulo = titulo
        self.director = director
        self.recaudacion = recaudacion

    def __lt__(self, other : Pelicula):
         if (not isinstance(other, Pelicula)):
            raise TypeError(f'TypeError: can only concatenate Pelicula (not "{type(other)}") to Pelicula')
         return self.recaudacion<other.recaudacion

    def __gt__(self, other : Pelicula):
        print('gt')

    def __eq__(self, other : Pelicula):
        print('eq')

    def __str__(self):
        return self.titulo
    
    def __repr__(self):
        return self.__str__()

p1 = Pelicula('Alien', 'Ridley', 30_000)
p2 = Pelicula('E.T.', 'Spielberg', 40_000)
p3 = Pelicula('Blade Runner', 'Ridley', 25_000)

peliculas = [p1, p2, p3]

peliculas.sort()

print(peliculas[0])
print(peliculas)