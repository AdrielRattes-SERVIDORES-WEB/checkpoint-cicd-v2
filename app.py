from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    # Rota principal de boas-vindas
    return "Hello, CI/CD!"


@app.route("/status")
def status():
    # Endpoint de healthcheck usado pelo pipeline de CI/CD
    return {"status": "ok", "service": "checkpoint-cicd"}


@app.route("/about")
def about():
    return {"project": "checkpoint-cicd", "team": "Pessoa A & Pessoa B"}


if __name__ == "__main__":
    app.run(debug=True)
