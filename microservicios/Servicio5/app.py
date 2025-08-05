from flask import Flask, jsonify
import requests

app = Flask(__name__)

#Servicio /murcia/<tipo1><tipo2>/<GET>
@app.route('/murcia/<tipo1>/<tipo2>', methods=['GET'])
def get_combined_data(tipo1, tipo2):
    # Inicializamos los datos de los diferentes tipos
    combined_data = {}

    # Obtenemos el primer tipo de datos
    if tipo1 == "geo":
        response_geo = requests.get("http://geo:5001/murcia/geo")
        if response_geo.status_code == 200:
            combined_data["geo"] = response_geo.json()
        else:
            return jsonify({"error": "Error al obtener los datos geográficos"}), 501

    elif tipo1 == "meteo":
        response_meteo = requests.get("http://meteo:5002/murcia/meteo")
        if response_meteo.status_code == 200:
            combined_data["meteo"] = response_meteo.json()
        else:
            return jsonify({"error": "Error al obtener los datos meteorológicos"}), 502

    elif tipo1 == "demo":
        response_demo = requests.get("http://demo:5003/murcia/demo")
        if response_demo.status_code == 200:
            combined_data["demo"] = response_demo.json()
        else:
            return jsonify({"error": "Error al obtener los datos demográficos"}), 503

    else:
        return jsonify({"error": "Tipo1 no válido"}), 400

    # Obtenemos el segundo tipo de datos
    if tipo2 == "geo":
        response_geo = requests.get("http://geo:5001/murcia/geo")
        if response_geo.status_code == 200:
            combined_data["geo"] = response_geo.json()
        else:
            return jsonify({"error": "Error al obtener los datos geográficos"}), 501

    elif tipo2 == "meteo":
        response_meteo = requests.get("http://meteo:5002/murcia/meteo")
        if response_meteo.status_code == 200:
            combined_data["meteo"] = response_meteo.json()
        else:
            return jsonify({"error": "Error al obtener los datos meteorológicos"}), 502

    elif tipo2 == "demo":
        response_demo = requests.get("http://demo:5003/murcia/demo")
        if response_demo.status_code == 200:
            combined_data["demo"] = response_demo.json()
        else:
            return jsonify({"error": "Error al obtener los datos demográficos"}), 503

    else:
        return jsonify({"error": "Tipo2 no válido"}), 400

    # Devolvemos los datos combinados
    return jsonify(combined_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004, debug=True)