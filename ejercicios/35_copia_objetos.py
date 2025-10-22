a = 5
b = a

print(a,b) # 5 5
a = 6
print(a,b) # 6 5

nombre='Adrián'
otro_nombre=nombre
print(nombre, otro_nombre)#Adrian Adrián
nombre='Carlos'
print(nombre, otro_nombre)#Carlos Adrián

lista_1 = ['Adrian','Carlos']
lista_2 = lista_1
print(lista_1, lista_2) # ['Adrian', 'Carlos'] ['Adrian', 'Carlos']
lista_1[0]='Felipe'
print(lista_1, lista_2) # ['Felipe', 'Carlos'] ['Felipe', 'Carlos']

lista_1 = ['Adrian','Carlos']
lista_2 = lista_1[:]
print(lista_1, lista_2) # ['Adrian', 'Carlos'] ['Adrian', 'Carlos']
lista_1[0]='Felipe'
print(lista_1, lista_2) # ['Felipe', 'Carlos'] ['Adrian', 'Carlos']

lista_1 = ['Adrian',['Puyo','Sainz'],'Carlos',['Berlanga','Riesco']]
lista_2 = lista_1[:]
print(lista_1, lista_2) # ['Adrian', ['Puyo', 'Sainz'], 'Carlos', ['Berlanga', 'Riesco']] ['Adrian', ['Puyo', 'Sainz'], 'Carlos', ['Berlanga', 'Riesco']]
lista_1[0]='Adrià' # HACE EL CAMBIO ÚNICAMENTE EN lista_1
print(lista_1, lista_2) # ['Adrià', ['Puyo', 'Sainz'], 'Carlos', ['Berlanga', 'Riesco']] ['Adrian', ['Puyo', 'Sainz'], 'Carlos', ['Berlanga', 'Riesco']]
lista_1[1][0]='Pujol' # HACE EL CAMBIO EN lista_1 y lista_2
print(lista_1, lista_2) # ['Adrià', ['Pujol', 'Sainz'], 'Carlos', ['Berlanga', 'Riesco']] ['Adrian', ['Pujol', 'Sainz'], 'Carlos', ['Berlanga', 'Riesco']]