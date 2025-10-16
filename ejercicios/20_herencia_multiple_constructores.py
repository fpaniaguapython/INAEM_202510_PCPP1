class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self, peso):
        A.__init__(self)
        print("B")

class C(A):
    def __init__(self, ancho, alto):
        A.__init__(self)
        print("C")

class D(B,C):
    def __init__(self, peso, ancho, alto):
        #super().__init__(peso, ancho, alto) # Error
        B.__init__(self, peso)
        C.__init__(self, ancho, alto)
        print("D")

d = D(100, 25, 250)