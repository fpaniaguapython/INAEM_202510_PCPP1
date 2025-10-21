class Movie:
    def __init__(self, titulo, director, duracion):
        self.titulo = titulo
        self.director = director
        self.duracion = duracion

    def __str__(self):
        return f'Título:{self.titulo}. Director:{self.director}. Duración:{self.duracion}'