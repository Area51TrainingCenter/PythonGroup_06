nota_1 = input('Nota 1> ')
nota_2 = input('Nota 2> ')
nota_3 = input('Nota 3> ')

nota_1 = float(nota_1)
nota_2 = float(nota_2)
nota_3 = float(nota_3)

promedio = round((nota_1 + nota_2 + nota_3) / 3, 2)

print('Promedio: ' + str(promedio))

if promedio >= 11.0:
    print('Aprobaste el curso!')
else:
    print('No aprobaste :(')
