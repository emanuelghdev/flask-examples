from flask import Flask
import json
from jsonschema import validate, ValidationError

app = Flask(__name__)

# Cargar esquemas JSON
def load_schema(schema_file):
    with open(f'schemas/{schema_file}') as file:
        return json.load(file)

schemas = {
    "municipio": load_schema("json_schema_municipio.json")
}

# Función para validar datos con esquema
def validate_data(schema_key, data):
    schema = schemas.get(schema_key)
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        return {"error": f"Datos no válidos: {e.message}"}, 400
    return data

# Servicio /murcia/<GET>
@app.route('/murcia/', methods=['GET'])
def get_local_data():
    with open('data/murcia.json') as file:
        data = json.load(file)
    return validate_data("municipio", data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)