from flask import Flask, Blueprint
from flask_restplus import Api


class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        # doc = caminho da documentação da API
        self.api = Api(self.blueprint, doc = '/doc', title='Sample Flask-SQLAlchemy')
        self.app.register_blueprint(self.blueprint)

        # configurações do banco de dados 
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['PROPAGATE_EXEPTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # instanciando o books 
        self.book_ns = self.book_ns()

    # retorna um namespace de API
    def book_ns(self, ):
        return self.api.namespace(name='Books', description ='books related operations', path ='/')

    #  método run responsável por iniciar a aplicação 
    def run(self, ):
        self.app.run(
            port = 5000,
            debug = True,
            host = '0.0.0.0'
        )

server = Server()

