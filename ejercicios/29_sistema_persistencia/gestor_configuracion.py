import enum
import json

class TipoPersistencia(enum.Enum):
    FICHERO_PLANO = 1
    JSON = 2

def get_tipo_persistencia():
    with open('config.json',mode='r',encoding='utf-8') as fichero:
        config = json.load(fichero)
    return TipoPersistencia[config['tipo_persistencia']]