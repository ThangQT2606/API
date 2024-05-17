from app import Application
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.post("/countries")

def appli():
    application = Application()
    if request.is_json:
        country = request.get_json()
        tmp = country["name_country"]
        return application.find(tmp)
    return {"error" : "Request must be json"}, 415

app.run(host = 'localhost', port = 6000, debug=True)