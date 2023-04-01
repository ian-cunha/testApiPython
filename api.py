from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Bem-vindo à minha API!'


@app.route('/usuarios')
def get_usuarios():
    # código para buscar e retornar dados de usuários
    return 'Dados dos usuários'


@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    # código para criar um novo usuário
    return 'Novo usuário criado'


if __name__ == '__main__':
    app.run(debug=True)
