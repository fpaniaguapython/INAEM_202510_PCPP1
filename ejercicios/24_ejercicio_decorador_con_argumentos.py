'''
Construir un decorador que genere una ficha con los nombres y los valores
de los atributos del primer argumento de la función que decora.

El decorador recibe como argumento:
0, para generar la ficha en HTML.
1, para generar la ficha en XML.

Las fichas se guardan en los ficheros 'fichas_html.txt' o 'fichas_xml.txt'
'''
def generar_ficha_html(atributos:dict):
    with open('fichas_html.txt','a',encoding='utf-8') as fichero:
        fichero.write('<tr>')
        for k,v in atributos.items():
            fichero.write(f'<td>{k}</td><td>{v}</td>')
        fichero.write('</tr>')
        fichero.write('\n')

def generar_ficha_xml(atributos:dict):
    with open('fichas_xml.txt','a',encoding='utf-8') as fichero:
        fichero.write('<registro>')
        for k,v in atributos.items():
            fichero.write(f'<{k}>{v}</{k}>')
        fichero.write('</registro>')
        fichero.write('\n')


def generar_ficha(tipo_ficha):
    def funcion_externa(funcion_a_decorar):
        def funcion_interna(*args, **kwargs):
            if len(args)>0:
                atributos = args[0].__dict__
                if tipo_ficha==0:
                    generar_ficha_html(atributos)
                elif tipo_ficha==1:
                    generar_ficha_xml(atributos)
                else:
                    raise ValueError('Opción no válida en el decorador')
            return funcion_a_decorar(*args, **kwargs)
        return funcion_interna
    return funcion_externa



class Pelicula:
    def __init__(self, titulo, director, duracion):
        self.titulo = titulo
        self.director = director
        self.duracion = duracion

et = Pelicula('ET','Spielberg',92)

@generar_ficha(1)
def cualquier_metodo(cualquier_objeto):
    pass

cualquier_metodo(et)