import json
import emoji
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
base_de_datos = {}

def carregar_dados():
    try:
        with open("base_de_dados.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

base_de_datos = carregar_dados()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def login():
    try:
        email = request.form.get('email_login')
        senha = request.form.get('senha_login')

        if email in base_de_datos and base_de_datos[email] == senha:
            # Mostrar mensaje de inicio de sesión
            mensaje = emoji.emojize("Bienvenido, has iniciado sesión exitosamente." ":grinning_face_with_big_eyes:")
            
            # Redirigir al usuario a la página protegida
            return redirect(url_for('pagina_protegida', mensaje=mensaje))
        else:
            raise ValueError (emoji.emojize("Error: El Email indicano no existe" ":zipper-mouth_face:"))

    except Exception:
        return (emoji.emojize("Error: E-mail o contraseña incorrectos. Por favor, intenta de nuevo." ":zipper-mouth_face:"))

def abrir_pagina_web(url):
    # Utilizar JavaScript para abrir la página web en una nueva ventana o pestaña
    script = f"window.open('{url}', '_blank');"
    return f'<script>{script}</script>'

@app.route('/pagina_protegida')
def pagina_protegida():
    
    mensaje = request.args.get('mensaje', 'Bienvenido, has iniciado sesión exitosamente.')
    return f"<p>{mensaje}</p>{abrir_pagina_web('https://blogpers0nal.netlify.app/')}"

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/registro', methods=['POST'])
def cadastrar():
    try:
        email = request.form.get('email')
        senha = request.form.get('senha')

        if email in base_de_datos:
            raise ValueError(emoji.emojize("Error: Este email ya está registrado." ":winking_face_with_tongue:"))

        base_de_datos[email] = senha
        salvar_dados()
        return (emoji.emojize("Usuario registrado con éxito." ":grinning_face_with_big_eyes:"))

    except ValueError as e:
        return str(e)  # Mostrar mensaje de error al usuario

    except Exception as e:
        return f"Error en el registro: {str(e)}"

def salvar_dados():
    with open("base_de_dados.json", "w") as arquivo:
        json.dump(base_de_datos, arquivo)

if __name__ == '__main__':
    app.run(debug=True)
