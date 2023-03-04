from flask import Flask

app = Flask(__name__)


# criar a primeira página
# route -> meusite.com/contatos
# função -> o que você vai exibir naqula página

@app.route("/")
def homepage():
    return "Esse é meu primeiro site."

# cria outra página


@app.route("/contatos")
def contatos():
    return "<p>Contatos: email</p><p>: e telefone (xx)</p>"


# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
