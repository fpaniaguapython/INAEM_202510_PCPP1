class Automovil:
    def __init__(self, marca, modelo, matricula):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.activo = True

    def acelerar(self):
        print(f'Soy {self.matricula} y estoy acelerando')

mi_seat_ibiza = Automovil(marca='Seat', modelo='Ibiza', matricula='8781-KYJ')
mi_seat_ibiza.acelerar()

# Lectura de atributos
print(mi_seat_ibiza.matricula)  #8781-KYJ
print(getattr(mi_seat_ibiza, 'matricula')) #8781-KYJ
print(getattr(mi_seat_ibiza, 'acelerar')) #<bound method Automovil.acelerar of <__main__.Automovil object at 0x000001A81CE94590>>
# print(mi_seat_ibiza.numero_plazas) # AttributeError
# print(getattr(mi_seat_ibiza, 'color')) # AttributeError

# Escritura de atributos
mi_seat_ibiza.matricula='1144-JBC'
setattr(mi_seat_ibiza, 'matricula', '8788-KYZ')
mi_seat_ibiza.numero_plazas = 4
setattr(mi_seat_ibiza, 'peso', 1_200)

print('¿Tiene peso?', hasattr(mi_seat_ibiza, 'peso'))