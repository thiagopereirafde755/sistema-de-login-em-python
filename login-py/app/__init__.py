from flask import Flask
from app.conexao import criar_conexao
import secrets

def create_app():
 
    app = Flask(__name__)

    app.secret_key = secrets.token_hex(32)


    from app.cadastrar import cadastrar_bp
    app.register_blueprint(cadastrar_bp)

 

    return app
