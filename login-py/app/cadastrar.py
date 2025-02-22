from flask import Blueprint, render_template, request, redirect, url_for
from app.conexao import criar_conexao


cadastrar_bp = Blueprint('cadastrar', __name__)


@cadastrar_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        conexao = criar_conexao()

        if conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO user (nome, email, senha) VALUES (%s, %s, %s)",
                (nome, email, senha)
            )
            conexao.commit()  
            cursor.close()
            conexao.close()

            return '<script>alert("Cadastro realizado!");window.location.href = "/"; </script>'
        else:
            return '<script>alert("Erro!"); window.location.href = "/cadastrar";</script>'
    return render_template('cadastrar.html')
