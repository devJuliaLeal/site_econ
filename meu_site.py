from flask import Flask

app = Flask(__name__)


# criar a primeira página
# route -> meusite.com/contatos
# função -> o que você vai exibir naqula página

@app.route("/")
def homepage():
    return "Esse é meu primeiro site"


# colocar o site no ar
app.run()
