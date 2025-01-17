from flask import Flask, render_template, request, redirect, url_for, session
from app.conexao import criar_conexao
from app.cadastrar import cadastrar_bp
from app.login import login_bp 
from app.log_out import logout_bp
from app.inicio import inicio_bp 

app = Flask(__name__)

import secrets
app.secret_key = secrets.token_hex(32) 


app.register_blueprint(cadastrar_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(inicio_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
