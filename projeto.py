from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])

def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/listar')
def listar():
    return render_template('coleta.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/editar')
def editar():
    return render_template('editar.html')



if __name__ == '__main__':
    app.run()
