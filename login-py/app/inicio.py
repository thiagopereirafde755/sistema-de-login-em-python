from flask import Blueprint, render_template, redirect, url_for, session
from app.conexao import criar_conexao


inicio_bp = Blueprint('inicio', __name__)

@inicio_bp.route('/inicio')
def inicio():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    usuario_id = session['usuario_id']

    conexao = criar_conexao()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT nome FROM user WHERE id = %s", (usuario_id,))
        usuario = cursor.fetchone()

        if usuario:
            nome_usuario = usuario[0]  
        else:
            nome_usuario = None

        cursor.close()
        conexao.close()

        return render_template('inicio.html', nome=nome_usuario)

    return "Erro na conexão"
