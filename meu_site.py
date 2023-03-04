from flask import Flask

app = Flask(__name__)


# criar a primeira página
# route -> meusite.com/contatos
# app foi definido anteriormente

@app.route()
# função -> o que vose vai exibir naqula página
def homepage():
    return "Esse é meu primeiro site"


# colocar o site no ar
app.run()
