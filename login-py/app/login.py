from flask import Blueprint, render_template, request, redirect, url_for, session
from app.conexao import criar_conexao


login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        conexao = criar_conexao()

        if conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM user WHERE email = %s AND senha = %s", (email, senha))
            usuario = cursor.fetchone()

            if usuario:
                session['usuario_id'] = usuario[0] 
               
                return '<script>alert("Acesso Permitido!");window.location.href = "/inicio"; </script>'
            else:
                 return '<script>alert("Email ou senha incorretos!"); window.location.href = "/";</script>'
 

            cursor.close()
            conexao.close()
        else:
            return "Erro na conexão com o banco de dados"  

    return render_template('login.html')
