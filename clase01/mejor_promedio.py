cuantas_notas = int(input('cuantas notas?> '))

suma_notas = 0

for i in range(cuantas_notas):
    suma_notas += float(input('nota no {}> '.format(i + 1)))

promedio = round(suma_notas / cuantas_notas, 2)

print('Promedio: ' + str(promedio))

if promedio >= 11.0:
    print('Aprobaste el curso!')
else:
    print('No aprobaste :(')
