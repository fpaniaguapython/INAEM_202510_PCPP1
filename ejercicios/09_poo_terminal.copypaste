class Pato:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso
    def saltar(self):
        pass
lucas = Pato('Lucas',2)
print(lucas.__dict__) # {'nombre': 'Lucas', 'peso': 2}
print(Pato.__dict__) # mappingproxy({'__module__': '__main__', '__firstlineno__': 1, '__init__': <function Pato.__init__ at 0x00000259D5C28D50>, 'saltar': <function Pato.saltar at 0x00000259D5C28F60>, '__static_attributes__': ('nombre', 'peso'), '__dict__': <attribute '__dict__' of 'Pato' objects>, '__weakref__': <attribute '__weakref__' of 'Pato' objects>, '__doc__': None})
lucas.edad = 3
donald = Pato('Donald', 4)
print(lucas.__dict__) # {'nombre': 'Lucas', 'peso': 2, 'edad': 3}
print(donald.__dict__) # {'nombre': 'Donald', 'peso': 4}
