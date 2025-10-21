import gestor_configuracion
import gestor_fichero_plano

def get_sistema_persistencia():
    tipo_persistencia = gestor_configuracion.get_tipo_persistencia()
    if (tipo_persistencia==gestor_configuracion.TipoPersistencia.FICHERO_PLANO):
        return gestor_fichero_plano.GestorFicheroPlano()