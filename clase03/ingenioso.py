import re

archivo = open('quijote.txt')
contenido = archivo.read()
archivo.close()

resultado = re.findall(r'(\w*oso)', contenido.lower())
print(len(resultado))
