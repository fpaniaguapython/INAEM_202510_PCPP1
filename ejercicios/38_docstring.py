"""Funciones de ejemplo de docstring"""


def calcular(numero: int) -> int:
    """Calcula un número

    :param numero -> Número a calcular
    :type numero -> int
    :return -> int -> Valor calculado
    """
    return numero


print(calcular.__doc__)
