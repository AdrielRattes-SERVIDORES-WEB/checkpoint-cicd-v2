from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, CI/CD!"


@app.route("/status")
def status():
    return {"status": "ok", "service": "checkpoint-cicd"}


if __name__ == "__main__":
    app.run(debug=True)
