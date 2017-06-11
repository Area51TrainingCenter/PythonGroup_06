for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        print('FizzBuzz')
    elif numero % 3 == 0:
        print('Fizz')
    elif numero % 5 == 0:
        print('Buzz')
    else:
        print(numero)


numero = 1
while numero < 101:
    if numero % 3 == 0 and numero % 5 == 0:
        print('FizzBuzz')
    elif numero % 3 == 0:
        print('Fizz')
    elif numero % 5 == 0:
        print('Buzz')
    else:
        print(numero)
    numero += 1
