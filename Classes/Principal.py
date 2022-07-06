from flask import Flask

app = Flask(__name__)


# decorator (annotation)
@app.route("/")
def homepage():
    return "Pedalaaas!"

@app.route("/findall")
def top10_produtos_mais_vendidos():
    return

# caso esse documento seja importado: não teremos o código abaixo sendo executado
# caso esse documento seja executado diretamente: teremos o código abaixo sendo executado
if __name__ == "__main__":
    app.run(debug=True)
