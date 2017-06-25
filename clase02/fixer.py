import requests

cantidad = float(input('ingrese cantidad (EUR)> '))
response = requests.get('http://api.fixer.io/latest').json()
resultado = round(cantidad * response['rates']['USD'], 3)

print('USD: ', resultado)
