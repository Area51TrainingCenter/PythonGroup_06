# import constantes
from constantes.matematicas import PI, e
from constantes.fisicas import e as e_fisico
# from constantes.fisicas import *

def suma(primero, segundo):
    return primero + segundo

print(suma(PI, e))
print(suma(PI, e_fisico))
