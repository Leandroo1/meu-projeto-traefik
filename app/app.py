from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá, mundo! Este é o serviço web Flask rodando com Traefik!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)