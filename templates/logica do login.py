import os
from flask import Flask, render_template, request, url_for, redirect, flash
import flask_login
app = Flask(__name__)
app.secret_key = 'super secret string'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresl://postgres:alunoifro@localhost/flask-teste'

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

users = {'teste@teste.com': {'password': 'secret'}}


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        if request.form['password'] == users[email]['password']:
            user = User()
            user.id = email
            flask_login.login_user(user)
            return redirect(url_for('protected'))

        flash('Usuário e/ou Senha incorreto(s)')
        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/protected')
@flask_login.login_required
def protected():
    flash('Olá {}, seu Login foi feito com sucesso!'.format(flask_login.current_user.id))
    return redirect(url_for('index'))


@app.route('/')
@flask_login.login_required
def index():
    return render_template('index.html')


@login_manager.unauthorized_handler
def unauthorized_handler():
    flash('Por favor, faça Login')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('login'))


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user


########################

if __name__ == '__main__':
    app.run(debug=True)