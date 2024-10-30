from flask import Flask, request
import json


app = Flask(__name__)





animals = {"Dog":10,"cat":8}
@app.get("/animals")
def get_animal():
    return animals

@app.route('/animals',methods=['POST'])
def create_animal():
    animals=request.get_json()
    data.append(animals)
    return jsonify(animals), 201

    

