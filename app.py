import os
from flask import Flask, make_response,jsonify

app = Flask(__name__)
PORT = os.getenv('PORT', 5050)

@app.route('/ok', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def ok():
  resp = make_response('{\n"pessoa": {\n"tipo": "Física",\n"codigo": "33898",\n"identificacao": "00599211105",\n"nome": "EDUARDO ARAUJO DA SILVA",\n"contato": {\n"ddd": "061 ",\n"telefone": " 2107401",\n"email": "eduardo.araujo@crediembrapa.co"\n}\n}\n}')
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
  resp = make_response('{\n"pessoa": {\n"tipo": "Física",\n"codigo": "33898",\n"identificacao": "00599211105",\n"nome": "EDUARDO ARAUJO DA SILVA",\n"contato": {\n"ddd": "061 ",\n"telefone": " 2107401",\n"email": "eduardo.araujo@crediembrapa.co"\n}\n}\n}')
  resp.headers['Content-Type'] = 'text/plain'
  resp.headers["X-Custom-Header"] = "Custom value"
  return resp


if __name__ == '__main__':
  app.run(port=PORT)
