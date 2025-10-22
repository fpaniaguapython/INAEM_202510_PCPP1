try:
    resultado = 100 / 0
    print(resultado)
except ZeroDivisionError as zde:
    print('No se puede dividir entre 0:', zde)
except ValueError as ve:
    pass
except NotImplementedError as nie:
    pass
except BaseException as e:
    pass
else:
    print('Ha ido todo bien')
finally:
    print('Esto se ejecuta siempre')


def sumar(s1 : int, s2 : int):
    if (not isinstance(s1, int) or not isinstance(s2, int)):
        raise TypeError('Los sumandos deben ser enteros')
    if (s1<0 or s2<0):
        raise ValueError('Los sumandos deben ser positivos')
    return s1+s2

try:
    sumar(3,-2)
except TypeError as te:
    pass
except ValueError as ve:
    pass
