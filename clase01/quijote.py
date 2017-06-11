archivo = open('quijote.txt')
contenido = archivo.read().lower()
archivo.close()

# {'a': 100, 'b': 333, 'c':...}

letras = {}

for letra in contenido:
    if letra in letras:
        letras[letra] += 1
    else:
        letras[letra] = 1

for letra, cantidad in letras.items():
    print('letra: {} cantidad: {}'.format(letra, cantidad))
