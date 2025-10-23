import gestor_configuracion
import gestor_fichero_plano
import gestor_json
import gestor_pickle

def get_sistema_persistencia():
    tipo_persistencia = gestor_configuracion.get_tipo_persistencia()
    if (tipo_persistencia==gestor_configuracion.TipoPersistencia.FICHERO_PLANO):
        return gestor_fichero_plano.GestorFicheroPlano()
    elif (tipo_persistencia==gestor_configuracion.TipoPersistencia.JSON):
        return gestor_json.GestorJSON()
    elif (tipo_persistencia==gestor_configuracion.TipoPersistencia.PICKLE):
        return gestor_pickle.GestorPickle()
    