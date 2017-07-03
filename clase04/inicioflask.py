from flask import Flask, render_template, request
app = Flask(__name__)


# @app.route('/')
# def index():
#     return 'Hola Mundo!'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/saludar', methods=['GET', 'POST'])
def saludar_formulario():
    contexto = {}

    if request.method == 'POST':
        contexto['nombre'] = request.form['nombre']

    return render_template('saludar.html', **contexto)


@app.route('/saludar/<nombre>')
def saludar(nombre):
    contexto = {
        'nombre': nombre,
        'edad': 15,
        'hobbies': ['nadar', 'leer', 'programar']
    }
    return render_template('hola.html', **contexto)


@app.route('/calcular', methods=['GET', 'POST'])
def calcular():
    contexto = {}
    if request.method == 'POST':
        operador = request.form['operador']
        op1 = float(request.form['op1'])
        op2 = float(request.form['op2'])
        resultado = 0
        if operador == 'suma':
            resultado = op1 + op2
        elif operador == 'resta':
            resultado = op1 + op2
        elif operador == 'producto':
            resultado = op1 * op2
        elif operador == 'cociente':
            resultado = op1 / op2
        contexto['resultado'] = resultado
    return render_template('calculadora.html', **contexto)


@app.route('/calcular/<operador>/<int:op1>/<int:op2>')
def suma(operador, op1, op2):
    operaciones = {
        'suma': lambda x, y: x + y,
        'resta': lambda x, y: x - y,
        'producto': lambda x, y: x * y,
        'cociente': lambda x, y: x / y,
    }
    operacion = operaciones[operador]
    resultado = str(operacion(op1, op2))
    return resultado

app.run(debug=True)
