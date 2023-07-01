import hashlib
import sqlite3
from getpass import getpass
from flask import Flask, request

app = Flask(__name__)

# Función para almacenar un usuario y contraseña en hash en la base de datos
def guardar_usuario(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    conn.close()

# Función para validar un usuario y contraseña ingresados
def validar_usuario(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE username = ? AND password = ?', (username, hashed_password))
    result = cursor.fetchone()
    conn.close()
    return result is not None

# Ruta para el formulario de registro
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        guardar_usuario(username, password)
        return 'Registro exitoso'
    return '''
        <form method="POST">
            <input type="text" name="username" placeholder="Nombre de usuario" required><br>
            <input type="password" name="password" placeholder="Contraseña" required><br>
            <input type="submit" value="Registrarse">
        </form>
    '''

# Ruta para el formulario de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if validar_usuario(username, password):
            return 'Inicio de sesión exitoso'
        else:
            return 'Credenciales incorrectas'
    return '''
        <form method="POST">
            <input type="text" name="username" placeholder="Nombre de usuario" required><br>
            <input type="password" name="password" placeholder="Contraseña" required><br>
            <input type="submit" value="Iniciar sesión">
        </form>
    '''

if __name__ == '__main__':
    # Crear la base de datos si no existe
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (username TEXT, password TEXT)')
    conn.close()

    # Ejecutar la aplicación en el puerto 4850
    app.run(port=4850)
