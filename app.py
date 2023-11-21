from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulación de una base de datos de usuarios (en una aplicación real, se usaría una base de datos real)
users = {
    'usuario1': 'contrasena1',
    'usuario2': 'contrasena2'
}

@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify({'message': 'Autenticación satisfactoria'})
    else:
        return jsonify({'error': 'Error en la autenticación'}), 401

if __name__ == '__main__':
    app.run(debug=True)
