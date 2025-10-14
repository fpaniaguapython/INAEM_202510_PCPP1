def comprobar_ventana(id):
    print(f'Comprobando ventana {id}')
    if id==2: 
        return False
    return True

if (comprobar_ventana(1) and comprobar_ventana(2) and comprobar_ventana(3)):
    print('Están todas OK')
else:
    print('Hay una ventana abierta')

print('*************')

if (comprobar_ventana(1) & comprobar_ventana(2) & comprobar_ventana(3)):
    print('Están todas OK')
else:
    print('Hay una ventana abierta')