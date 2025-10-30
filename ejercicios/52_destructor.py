class Pelicula:
    def __init__(self): # 'Constructor' o 'Inicializador'
        print('Init')

    def __del__(self): # 'Destructor'
        print('Del')

o = Pelicula()