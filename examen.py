import requests

print('Star Wars\n=========')

personajes = {}
peliculas = requests.get('https://swapi.co/api/films/').json()

print('Películas:')
for pelicula in peliculas['results']:
    print('- {}'.format(pelicula['title']))

    print('Personajes:')
    for url_personaje in pelicula['characters']:
        if url_personaje not in personajes:
            personajes[url_personaje] = requests.get(url_personaje).json()
        print('* {}'.format(personajes[url_personaje]['name']))

    print('===')

print('Talla personajes:')
for url, personaje in personajes.items():
    print(personaje['name'])

    if personaje['height'] != 'unknown':
        talla = int(personaje['height']) // 10
    else:
        talla = 0

    print('*' * talla)

