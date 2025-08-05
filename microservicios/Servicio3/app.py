from flask import Flask, jsonify
import json
import requests
from jsonschema import validate, ValidationError

app = Flask(__name__)

# Cargar esquemas JSON
def load_schema(schema_file):
    with open(f'schemas/{schema_file}') as file:
        return json.load(file)

schemas = {
    "meteo": load_schema("json_schema_municipio_meteo.json")
}

# Función para validar datos con esquema
def validate_data(schema_key, data):
    schema = schemas.get(schema_key)
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        return {"error": f"Datos no válidos: {e.message}"}, 400
    return data

# Servicio /murcia/meteo/<GET>
@app.route('/murcia/meteo', methods=['GET'])
def get_meteo_data():
    response = requests.get('https://www.el-tiempo.net/api/json/v2/provincias/30/municipios/30030')
    if response.status_code == 200:
        api_data = response.json()
        meteo_data = {
            "municipioid": 30030,
            "temperatura_actual": api_data["temperatura_actual"] + "°C",
            "temperaturas": {
                "max": api_data["temperaturas"]["max"] + "°C",
                "min": api_data["temperaturas"]["min"] + "°C"
            },
            "humedad": api_data["humedad"] + "%",
            "viento": api_data["viento"] + " km/h",
            "precipitacion": api_data["precipitacion"] + " mm",
            "lluvia": "Sí" if api_data["lluvia"] else "No"
        }
        return validate_data("meteo", meteo_data)
    else:
        return jsonify({"error": "No se pudieron obtener datos meteorológicos"}), 502

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)