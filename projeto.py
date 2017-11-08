from flask import Flask, render_template

app = Flask(__name__)

inst = {'inst1', 'inst2', 'inst3'}

@app.route('/',methods = ['GET','POST'])

def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/listar')
def listar():
    return render_template('pontosColeta.html', instituicoes=inst)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')



if __name__ == '__main__':
    app.run()
