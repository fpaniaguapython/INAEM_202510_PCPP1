class Vehiculo:
    def __init__(self, nombre):
        self.nombre = nombre

class Terrestre(Vehiculo):
    # Opción 1
    def __init__(self, nombre, marca):
        super().__init__(nombre) # Llamando al __init__ de la clase base
        self.marca=marca

    # Opción 2 (hace lo mismo que Opción 1)
    #def __init__(self, nombre, marca):
    #    Vehiculo.__init__(self, nombre)
    #    self.marca=marca

class Acuatico(Vehiculo):
    pass

mi_auto = Terrestre('Z5','BMW')
print(mi_auto.nombre)