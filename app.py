from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
#CORS(app, origins=["https://meu-frontend-angular.netlify.app"])

# Configuração do banco (Render injeta DATABASE_URL automaticamente)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route("/")
def home():
    return jsonify({"message": "API Flask funcionando!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
