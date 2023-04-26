import os
from flask import Flask, make_response, jsonify
from faker import Faker

app = Flask(__name__)
PORT = os.getenv('PORT', 5050)
fake = Faker()

def generate_fake_data():
    fake_pessoa = {
        "tipo": fake.random_element(elements=("Física", "Jurídica")),
        "codigo": fake.random_number(digits=5),
        "identificacao": fake.ssn(),
        "nome": fake.name(),
        "contato": {
            "ddd": fake.numerify(text="###"),
            "telefone": fake.numerify(text="#########"),
            "email": fake.email()
        }
    }
    return {"pessoa": fake_pessoa}

@app.route('/ok', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def ok():
    resp = make_response(jsonify(generate_fake_data()))
    resp.headers['Content-Type'] = 'application/json'
    resp.headers["X-Custom-Header"] = "Custom value"
    return resp


@app.route('/ok-empty', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def ok_empty():
    resp = make_response()
    resp.headers['Content-Type'] = 'application/json'
    resp.headers["X-Custom-Header"] = "Custom value"
    return resp


@app.route('/not-ok', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def not_ok():
    resp = make_response('{\n"pessoa": {\n"tipo": "Física",\n"codigo": "33898",\n"identificacao": "00599211105",\n"nome": "EDUARDO ARAUJO DA SILVA",\n"contato": {\n"ddd": "061 ",\n"telefone": " 2107401",\n"email": "eduardo.araujo@crediembrapa.co",\n}\n}\n}')
    resp.headers['Content-Type'] = 'application/json'
    resp.headers["X-Custom-Header"] = "Custom value"
    return resp


@app.route('/ok-no-header', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def ok_no_header():
    resp = make_response(jsonify(generate_fake_data()))
    resp.headers['Content-Type'] = 'text/plain'
    resp.headers["X-Custom-Header"] = "Custom value"
    return resp


@app.route('/ok-string', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def ok_string():
    data = [
        generate_fake_data(),
        generate_fake_data(),
        generate_fake_data()
    ]
    response = make_response(jsonify(data))
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == '__main__':
    app.run(port=PORT,host=0.0.0.0)
