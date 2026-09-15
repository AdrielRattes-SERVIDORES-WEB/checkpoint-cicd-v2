from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    # Rota principal com mensagem unificada pós-conflito
    return "Mensagem unificada pelas Pessoas A e B"


@app.route("/status")
def status():
    # Endpoint de healthcheck usado pelo pipeline de CI/CD
    return {"status": "ok", "service": "checkpoint-cicd"}


@app.route("/about")
def about():
    return {"project": "checkpoint-cicd", "team": "Pessoa A & Pessoa B"}


@app.route("/version")
def version():
    return {"version": "1.0.0"}


if __name__ == "__main__":
    app.run(debug=True)
