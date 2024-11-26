from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from flask_cors import CORS
from flask import send_from_directory


# Crear la app Flask
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
# Cargar el modelo entrenado
modelo = tf.keras.models.load_model('modelo.h5')

# Ruta de prueba para verificar que la API funciona
@app.route('/')
def home():
    return "¡La API está funcionando!"

# Ruta para predecir
@app.route('/frontend')
def serve_frontend():
    return send_from_directory('.', 'index.html')

"""   
@app.route('/predict_get', methods=['GET'])
def predict_get():
    try:
        # Obtener el parámetro de la URL
        celsius_value = request.args.get('celsius', type=float)

        # Verificar que el parámetro no sea nulo
        if celsius_value is None:
            return jsonify({'error': 'Falta el parámetro "celsius"'}), 400

        # Hacer la predicción
        prediction = modelo.predict([[celsius_value]])

        fahrenheit = float(prediction[0][0]) 

        # Responder con la predicción
        return jsonify({'celsius': celsius_value, 'fahrenheit': fahrenheit})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
