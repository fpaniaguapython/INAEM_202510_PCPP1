class Alumno:
    def __init__(self, nombre, capital):
        self.nombre = nombre
        self.capital = capital

    def __str__(self):
        return(f'Nombre:{self.nombre}#Capital:{self.capital}')
    
    def __len__(self):
        return len(self.nombre)*self.capital

alumno_1 = Alumno('Alumno 1', 200)
print(alumno_1)

print(len(alumno_1))