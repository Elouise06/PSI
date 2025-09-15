from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  return 'Essa é minha primeira aplicação em Flask!'

@app.route('/contato')
def contato():
  return 'elouise.costa@escolar.ifrn.edu.br'

if __name__ == '__main__':
    app.run()