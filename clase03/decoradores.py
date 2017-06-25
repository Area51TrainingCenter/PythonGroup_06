def decorar(funcion):
    def decorador(*args):
        print('a punto de llamar a la funcion con argumentos', args)
        resultado = funcion(*args)
        print('termino llamada a funcion, resultado', resultado)
        return resultado
    return decorador


@decorar
def sumar(a, b):
    return a + b

# sumar = decorar(sumar)

print(sumar(3, 5))
