def calculadora(operador):
    def suma(a, b):
        return a + b

    def resta(a, b):
        return a - b

    def producto(a, b):
        return a * b

    def cociente(a, b):
        return a / b

    dict_operaciones = {
        '+': suma,
        '-': resta,
        '*': producto,
        '/': cociente
    }

    return dict_operaciones[operador]

operacion = calculadora('*')
print(operacion(3, 5))
