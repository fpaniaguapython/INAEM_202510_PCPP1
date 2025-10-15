class ProductoMultimedia:
    pass

class Pelicula(ProductoMultimedia):
    pass

class Corto(Pelicula):
    pass

la_pelicula = Pelicula()

print(isinstance(la_pelicula, Pelicula)) # True
print(isinstance(la_pelicula, ProductoMultimedia)) # True
print(isinstance(la_pelicula, object)) # True

print(issubclass(Corto, Pelicula)) # True
print(issubclass(Corto, ProductoMultimedia)) # True