from flask import Flask, render_template, request, redirect, url_for, session
from app.conexao import criar_conexao

app = Flask(__name__)


import secrets

app.secret_key = secrets.token_hex(32) 

# inicio
@app.route('/')
def index():
    return render_template('index.html')
# inicio

# ir para cadastro e form
@app.route('/cadastrar', methods=['GET', 'POST'])
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

            return redirect(url_for('index'))
        else:
            return "Erro na conexão"
    return render_template('cadastrar.html')
# ir para cadastro e form

# fazer login
@app.route('/login', methods=['GET', 'POST'])
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
                return redirect(url_for('inicio'))
            else:
                return "Email ou senha inválidos"

            cursor.close()
            conexao.close()
        else:
            return "Erro na conexão"

    return render_template('login.html')
# fazer login

# pagina inicial
@app.route('/inicio')
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
# pagina inicial

# log out
@app.route('/logout')
def logout():
    session.pop('usuario_id', None)
    return redirect(url_for('index'))
# log out


if __name__ == '__main__':
    app.run(debug=True)
