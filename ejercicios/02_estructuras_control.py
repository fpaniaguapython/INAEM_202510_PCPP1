nombre='Python'
if nombre=='Python':
    print('Es Python')
elif nombre=='Java':
    print('Es Java')
else:
    print('No sé qué es')

match nombre:
    case 'Python':
        print('Es Python')
    case 'Java':
        print('Es Java')
    case _:
        print('No sé qué es')

lista = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
for dia in lista:
    print(dia)

for numero in range(10):
    print(numero)    

numero_secreto = 5
numero_introducido=0
while numero_secreto!=numero_introducido:
    numero_introducido = int(input('Número:'))
print('¡Lo adivinaste!')

for numero in range(0,10,2):
    print(numero)
    if (numero==4):
        break
else:
    print('He terminado')


