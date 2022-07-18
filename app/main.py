from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home() :
    return jsonify({
        "author":"Jovan",
        "Project": "simple flask api"
        })