from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)

ingredientes = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ingrediente = request.form['ingrediente']
        ingredientes.append(ingrediente)

    contexto = {
        'ingredientes': enumerate(ingredientes)
    }
    return render_template('lista_ingredientes.html', **contexto)


@app.route('/quitar/<int:id>')
def quitar(id):
    del ingredientes[id]
    return redirect('/')


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        ingredientes[id] = request.form['ingrediente']
        return redirect('/')
    contexto = {
        'ingrediente': ingredientes[id]
    }
    return render_template('editar_ingrediente.html', **contexto)


@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        asunto = request.form['asunto']
        mensaje = request.form['mensaje']

        requests.post(
            'https://api.mailjet.com/v3/send',
            auth=('f52dc6d0ebd73d4e9bc070872eced633', '3d39f856891a4b5788a6c17297a44d45'),
            json={
                'FromEmail': 'mcachayt@gmail.com',
                'FromName': 'Formulario de Contacto',
                'Subject': '{} ({}) te ha enviado un mensaje: {}'.format(nombre, email, asunto),
                'Text-part': mensaje,
                'Html-part': mensaje,
                'Recipients': [{'Email': 'mcachayt@gmail.com'}]
            }
        )
    return render_template('contacto.html')

app.run(debug=True)
