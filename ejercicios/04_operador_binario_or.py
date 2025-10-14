# or 
# |

# Programar las funciones calcular(), imprimir() y generar()
# Llamarlas y evaluar si alguna de ellas devuelve True
# Si True --> Mensaje 'OK'
# Si no --> Mensaje 'KO'
# Realizar la evaluación con or y con |

def calcular():
    print('Calculando...')
    return False

def imprimir():
    print('Imprimiendo...')
    return True

def generar():
    print('Generando...')
    return False

if calcular() or imprimir() or generar():
    print('OK')
else:
    print('KO')

print('***************')

if calcular() | imprimir() | generar():
    print('OK')
else:
    print('KO')    