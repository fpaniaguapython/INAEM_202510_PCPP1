class Pelicula:
    def __init__(self, titulo, director, ingreso):
        self.titulo = titulo
        self.director = director
        self.ingreso = ingreso

    def __add__(self, other : Pelicula):
        if (not isinstance(other, Pelicula)):
            raise TypeError(f'TypeError: can only concatenate Pelicula (not "{type(other)}") to Pelicula')
        return Pelicula(self.titulo+other.titulo, self.director+other.director, self.ingreso+other.ingreso)

    def __str__(self):
        return f'Título:{self.titulo}. Director:{self.director}, Ingresos:{self.ingreso}'

el_resplandor = Pelicula('El Replandor', 'Kubrick', 10_000_000)
et = Pelicula('E.T. El extraterrestre', 'Spielberg', 25_000_000)
rambo = Pelicula('Rambo', 'Stallone', 8_000_000)
print(el_resplandor + et + rambo + 8)

