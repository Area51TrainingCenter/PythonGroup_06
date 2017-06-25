def calcular(operacion, *valores):
    return operacion(*valores)

resultado = calcular(lambda a, b: a - b, 5, 6)
print(resultado)
