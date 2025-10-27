class Mamifero:
    pass

def ladrar(self):
    print(f'Soy {self.nombre} y estoy ladrando. ¡Guau, guau!')

Dog = type('Dog', (Mamifero,), {'nombre':'', 'ladrar':ladrar})

el_perro = Dog()

Dog.nombre = 'Lo que sea' # Este es el atributo de clase definido en type
el_perro.nombre = 'Pluto' # Este es el atributo de instancia definido AQUÍ
el_perro.ladrar()