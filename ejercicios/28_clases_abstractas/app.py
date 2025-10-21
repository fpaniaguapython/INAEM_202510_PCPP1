import cocinero
import factory
if __name__=='__main__':
    mi_cocinero = factory.CocineroFactory.create_cocinero()
    mi_cocinero.hacer_paella()