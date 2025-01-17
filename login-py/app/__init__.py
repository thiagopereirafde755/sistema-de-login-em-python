from flask import Flask
from app.conexao import criar_conexao
import secrets

def create_app():
 
    app = Flask(__name__)

    app.secret_key = secrets.token_hex(32)


    from app.cadastrar import cadastrar_bp
    app.register_blueprint(cadastrar_bp)


    from app.login import login_bp
    app.register_blueprint(login_bp)

    from app.log_out import logout_bp
    app.register_blueprint(logout_bp)

    from app.inicio import inicio_bp
    app.register_blueprint(inicio_bp)


 

    return app
