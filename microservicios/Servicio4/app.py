from flask import Flask
import json
from jsonschema import validate, ValidationError

app = Flask(__name__)

# Cargar esquemas JSON
def load_schema(schema_file):
    with open(f'schemas/{schema_file}') as file:
        return json.load(file)

schemas = {
    "demo": load_schema("json_schema_municipio_demo.json")
}

# Función para validar datos con esquema
def validate_data(schema_key, data):
    schema = schemas.get(schema_key)
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        return {"error": f"Datos no válidos: {e.message}"}, 400
    return data

#Servicio /murcia/demo/<GET>
@app.route('/murcia/demo', methods=['GET'])
def get_demo_data():
    with open('data/murcia_demo.json') as file:
        demo_data = json.load(file)
    return validate_data("demo", demo_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug=True)