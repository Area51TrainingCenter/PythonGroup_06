lo_que_el_usuario_ingreso = input('nota 1> ').lower()
cuantas_notas = 0
suma_notas = 0

while lo_que_el_usuario_ingreso != 'salir':
    suma_notas += float(lo_que_el_usuario_ingreso)
    cuantas_notas += 1
    # cuantas_notas = cuantas_notas + 1
    lo_que_el_usuario_ingreso = input('nota {}> '.format(cuantas_notas + 1)).lower()

promedio = round(suma_notas / cuantas_notas, 2)
print('Promedio: ' + str(promedio))

if promedio >= 11.0:
    print('Aprobaste el curso!')
else:
    print('No aprobaste :(')

