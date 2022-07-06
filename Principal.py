from flask import Flask, render_template

app = Flask(__name__)


# decorator (annotation)
@app.route("/")
def homepage():
    return render_template("index.html")


# caso esse documento seja importado: não teremos o código abaixo sendo executado
# caso esse documento seja executado diretamente: teremos o código abaixo sendo executado
if __name__ == "__main__":
    app.run(debug=True)
