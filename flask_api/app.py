from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        usuario = request.form['usuario']
        senha = request.form['senha']
        confirmar_senha = request.form['confirmar_senha']
        
        if senha != confirmar_senha:
            return render_template("fail.html"), 400
        return render_template("success.html")
    
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
