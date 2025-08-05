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
    "geo": load_schema("json_schema_municipio_geo.json")
}

# Función para validar datos con esquema
def validate_data(schema_key, data):
    schema = schemas.get(schema_key)
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        return {"error": f"Datos no válidos: {e.message}"}, 400
    return data

# Servicio /murcia/geo/<GET>
@app.route('/murcia/geo', methods=['GET'])
def get_geo_data():
    response = requests.get('https://www.el-tiempo.net/api/json/v2/provincias/30/municipios/30030')
    if response.status_code == 200:
        api_data = response.json()
        geo_data = {
            "municipioid": 30030,
            "latitud": float(api_data["municipio"]["LATITUD_ETRS89_REGCAN95"]),
            "longitud": float(api_data["municipio"]["LONGITUD_ETRS89_REGCAN95"]),
            "altitud": float(api_data["municipio"]["ALTITUD"])
        }
        return validate_data("geo", geo_data)
    else:
        return jsonify({"error": "No se pudieron obtener datos geográficos"}), 501

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)