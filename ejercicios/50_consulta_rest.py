import requests
import json

# Obtenemos el id
id = None
while True:
    id = input('Introduce un identificador numérico entero:')
    if (not id.isdigit()):
        continue
    else:
        id=int(id)
        break

# Función de procesado de content
def procesar_content(content):
    str_content = content.decode("utf-8")
    dict_content = json.loads(str_content)
    print('Identificador:',dict_content['id'])
    print('Marca:',dict_content['brand'])
    print('Modelo:',dict_content['model'])

# Función de procesado de response
def procesar_response(response):
    dict_content = response.json() # Proporciona un dict con los datos del content
    print('Identificador:',dict_content['id'])
    print('Marca:',dict_content['brand'])
    print('Modelo:',dict_content['model'])

# Función de procesado de 404
def procesar_404(identificador):
    print(f'No se ha encontrado el automóvil {identificador}')
    
# Construir la URL
try:
    URL = f'http://localhost:3000/cars/{id}'
    respuesta = requests.get(URL)
    if (respuesta.status_code==requests.codes.OK):
        # Procesar respuesta
        # procesar_content(respuesta.content)
        procesar_response(respuesta)
    elif (respuesta.status_code==requests.codes.not_found):
        # Procesar no encontrado
        procesar_404(id)
    else:
        # Procesar error
        pass
except requests.RequestException as rre:
    print('Ha ocurrido un error al realizar la petición:',rre)





