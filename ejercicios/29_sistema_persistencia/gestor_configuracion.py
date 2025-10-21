import enum

class TipoPersistencia(enum.Enum):
    FICHERO_PLANO = 1
    JSON = 2

def get_tipo_persistencia():
    return TipoPersistencia.FICHERO_PLANO