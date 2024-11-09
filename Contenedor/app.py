from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar el modelo entrenado
modelo = joblib.load('model.pkl')

# Ruta para realizar predicciones
@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos de la solicitud
    data = request.get_json(force=True)
    # Crear un DataFrame a partir de los datos
    input_data = pd.DataFrame([data])
    # Asegurar que las columnas estén en el orden correcto
    input_data = input_data[['km4week', 'sp4week']]
    # Realizar la predicción
    prediccion = modelo.predict(input_data)
    # Devolver el resultado
    return jsonify({'MarathonTime': prediccion[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
