
class Alumno:
    bolsa = 100
    def __init__(self, nombre, capital):
        self.nombre = nombre
        self.capital = capital

carlos = Alumno('Carlos', 30)
juan_jose = Alumno('Juan José', 50)
fernando = Alumno('Fernando', 500)

print(carlos.capital) # 30
print(Alumno.bolsa) # 100
print(carlos.bolsa) # 100
Alumno.bolsa-=10
print(Alumno.bolsa) # 90
print(carlos.bolsa) # 90
carlos.bolsa=120 # ¡ATENCIÓN! Crea un nuevo atributo
print(Alumno.bolsa) # 90
print(carlos.bolsa) # 120
Alumno.bloqueado = True
print(Alumno.bloqueado) # True
print(carlos.bloqueado) # True

print(Alumno.__dict__) 
print(carlos.__dict__) # {'nombre': 'Carlos', 'capital': 30, 'bolsa': 120}
