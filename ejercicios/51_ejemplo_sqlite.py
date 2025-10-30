import sqlite3

class Movie:
    def __init__(self, id, titulo, director, anyo):
        self.id = id
        self.titulo = titulo
        self.director = director 
        self.anyo = anyo

def get_connection(db_name):
    con = sqlite3.connect(db_name)
    return con

def create_database(con):
    sql = '''CREATE TABLE IF NOT EXISTS peliculas(
        id INTEGER PRIMARY KEY, 
        titulo TEXT NOT NULL,
        director TEXT NOT NULL, 
        anyo INTEGER NOT NULL
        );'''
    c=con.cursor()
    c.execute(sql)

def create(con, movie : Movie):
    cursor = con.cursor()
    # Alternativa 1, con f-string
    #sql = f'INSERT INTO peliculas (titulo, director, anyo) VALUES ("{movie.titulo}","{movie.director}",{movie.anyo});'
    #cursor.execute(sql)

    # Alternativa 2, con variables en la sentencia SQL
    sql = 'INSERT INTO peliculas (titulo, director, anyo) VALUES (?,?,?)'
    cursor.execute(sql, (movie.titulo, movie.director, movie.anyo))
    con.commit()
    cursor.close()

def read(con, id) -> Movie:
    cursor = con.cursor()
    sql = f'SELECT * FROM peliculas WHERE id={id}'
    cursor.execute(sql)
    pelicula = cursor.fetchone()
    if pelicula is None:
        raise Exception('Película no encontrada')
    pelicula = Movie(id=pelicula[0], titulo=pelicula[1], director=pelicula[2], anyo=pelicula[3])
    cursor.close()
    return pelicula

    
def update(con, movie : Movie):
    cursor = con.cursor()
    sql = 'UPDATE peliculas SET titulo=?, director=?, anyo=? WHERE id=?'
    cursor.execute(sql, (movie.titulo, movie.director, movie.anyo, movie.id))
    con.commit()
    cursor.close()

if __name__=='__main__':
    try:
        con = get_connection('peliculas.db')
        create_database(con)

        #peli = Movie(None, 'Película 2', 'Director 2', 1991)
        #create(con, peli)

        peli = read(con, 8)
        print(type(peli))
        print(peli)

        #peli = Movie(1, 'It Capítulo 2', 'Wes Craven', 2005)
        #update(con, peli)

        

    except BaseException as be:
        print('Ha ocurrido un error:', be)
    finally:
        try:
            con.close()
        except BaseException:
            print('No se ha podido cerrar la conexion')
