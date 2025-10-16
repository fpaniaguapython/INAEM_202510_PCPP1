# MRO
class A:
    def saludar(self):
        print("Hola, soy A")

class B(A):
    def saludar(self):
        print("Hola, soy B")

class C(A):
    def saludar(self):
        print("Hola, soy C")

class D(C,A):#NOVEDAD
    def xsaludar(self):
        print("Hola, soy D")

d = D()
d.saludar()#TypeError: Cannot create a consistent method resolution order (MRO) for bases A, C