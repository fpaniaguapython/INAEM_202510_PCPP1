import abc

class Cocinero(abc.ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sofrito(self):
        print(f'Soy {self.nombre} y estoy haciendo un sofrito estándar')

    @abc.abstractmethod
    def hacer_paella(self):
        pass

    @abc.abstractmethod
    def asar_cochinillo(self):
        pass

class CocineroJapones(Cocinero):
    def hacer_paella(self):
        print('Soy un CocineroJaponés y estoy haciendo paella')
    
    def asar_cochinillo(self):
        print('Soy un CocineroJaponés y estoy asando un cochinillo')

class CocineroAragones(Cocinero):
    def hacer_paella(self):
        print('Soy un CocineroAragonés y estoy haciendo paella')
    
    def asar_cochinillo(self):
        print('Soy un CocineroAragonés y estoy asando un cochinillo')
