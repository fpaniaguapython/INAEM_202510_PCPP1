def decorador(funcion):
    def inner(self, *args, **kwargs):
        print('Función:', funcion)
        print('*args:', *args)
        print('**kwargs:', **kwargs)
        funcion(self, *args, **kwargs)
    return inner

class Enemigo:
    @decorador
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud
    
    @decorador
    def atacar(self, danyo):
        print(f'Soy {self.nombre} y te hago daño:', danyo)

sauron = Enemigo('Sauron',100)
sauron.atacar(10)


