import requests
import pytesseract
from bs4 import BeautifulSoup
from PIL import Image

DNI = input('ingrese DNI> ')

sesion = requests.Session()
imagen_response = sesion.get('http://www.sunat.gob.pe/cl-ti-itmrconsruc/captcha?accion=image')
archivo = open('captcha.jpg', 'wb')
archivo.write(imagen_response.content)
archivo.close()

captcha = pytesseract.image_to_string(Image.open('captcha.jpg'))

formulario = {
    'accion': 'consPorTipdoc',
    'razSoc': '',
    'nroRuc': '',
    'nrodoc': DNI,
    'contexto': 'ti-it',
    'search1': '',
    'codigo': captcha,
    'tQuery': 'on',
    'tipdoc': '1',
    'search2': DNI,
    'coddpto': '',
    'codprov': '',
    'coddist': '',
    'search3': ''
}

sunat_response = sesion.post('http://www.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias', data=formulario)

soup = BeautifulSoup(sunat_response.content, 'html.parser')
segunda_tabla = soup.find_all('table')[1]
ultima_fila = segunda_tabla.find_all('tr')[-1]
print(ultima_fila.text.strip())
