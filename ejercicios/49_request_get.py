import requests

respuesta = requests.get('http://localhost:3000')

if (respuesta.status_code==requests.codes.OK):
    print('OK')
    # print(respuesta.headers) # Cabecera HTTP
    print(respuesta.content) # Content
else:
    print('ERROR:', respuesta.status_code)

# print(type(respuesta))
# print(respuesta.__dict__)

