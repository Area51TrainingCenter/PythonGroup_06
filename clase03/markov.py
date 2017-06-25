import random
import re

archivo = open('quijote.txt',)
contenido = archivo.read()
archivo.close()

contenido = contenido.replace('\n', ' ')
contenido = re.sub(r'  +', ' ', contenido)
contenido = re.sub(r'[^\w ]', '', contenido)
contenido = contenido.lower()
contenido = contenido.split(' ')

# {'el': ['ingenioso', 'perro'],
#  'la': ['bella', ...],
#  'caballero': ['don', ..]}
palabras = {}

for posicion, palabra in enumerate(contenido[:-1]):
    if palabra not in palabras:
        palabras[palabra] = []
    palabras[palabra].append(contenido[posicion + 1])


palabra_inicial = 'el'
numero_palabras = 30

resultado = [palabra_inicial]

for numero in range(numero_palabras):
    ultima_palabra = resultado[-1]
    lista_palabras = palabras.get(ultima_palabra)
    if lista_palabras:
        resultado.append(random.choice(lista_palabras))

print(' '.join(resultado))
