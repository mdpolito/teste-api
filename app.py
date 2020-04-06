from flask import Flask, jsonify, abort, make_response, request
import socket

app = Flask(__name__)


@app.route('/produtos', methods=['GET'])
def produto():

    sec = str(request.headers.get("X-3scale-proxy-secret-token"))

    print(sec)

    if sec != "testesec":
        return jsonify({"message": "codigo errado"})

    try:

        lista = ({"codigo": "000001", "nome": "Gasolina comum - 1"},
                 {"codigo": "000002", "nome": "Gasolina aditivada"},
                 {"codigo": "000003", "nome": "Etanol"},
                 {"codigo": "000004", "nome": "Oleo diesel"})

        return jsonify(lista)

    except Exception as erro:
        abort(500, 'Ocorreu um erro interno: ' + str(erro))


@app.errorhandler(500)
def erro500(error):
    response = jsonify({'mensagem': error.description})
    return make_response(response, 500)


# Recupera o endereço IP do servidor de aplicação
hostIP = socket.gethostbyname(socket.gethostname())

# Executa a aplicação
app.run(host=hostIP, port=8080, debug=False)
