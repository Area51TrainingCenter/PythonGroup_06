def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def producto(a, b):
    return a * b


def cociente(a, b):
    return a / b


def calcular(operacion, *valores):
    return operacion(*valores)

resultado = calcular(resta, 5, 6)
print(resultado)
