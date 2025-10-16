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

class D(B,C):
    def xsaludar(self):
        print("Hola, soy D")

d = D()
d.saludar()