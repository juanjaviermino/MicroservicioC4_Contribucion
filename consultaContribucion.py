from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_response(cedula):
    base_url = "https://srienlinea.sri.gob.ec/sri-catastro-sujeto-servicio-internet/rest/ConsolidadoContribuyente/existePorNumeroRuc"
    numero_ruc = f"{cedula}001"

    try:
        response = requests.get(f"{base_url}?numeroRuc={numero_ruc}")
        response.raise_for_status()
        return response.json()  # Assuming the response is in JSON format
    except requests.RequestException as e:
        return {"Error": str(e)}

@app.route('/verify_contributor', methods=['GET'])
def verify_contributor():
    cedula = request.args.get('cedula')
    if not cedula:
        return jsonify({"Error": "Cedula is required"}), 400
    result = get_response(cedula)
    return jsonify(result)

if __name__ == '__main__':
    app.run()
