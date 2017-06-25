import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.kitco.com/', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'})
soup = BeautifulSoup(response.content, 'html.parser')

precio_maximo = soup.find(attrs={'id': 'AU-high'}).text
precio_minimo = soup.find(attrs={'id': 'AU-low'}).text

print('PRECIO DEL ORO:')
print('maximo: {}'.format(precio_maximo))
print('minimo: {}'.format(precio_minimo))
