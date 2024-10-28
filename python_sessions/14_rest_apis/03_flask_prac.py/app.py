from flask import Flask, request
import json


app = Flask(__name__)





animals = {"Dog":10,"cat":8}
@app.get("/animals")
def get_animal():
    return animals

<<<<<<< HEAD

=======
@app.get("/animals", method=["POST"])

def add_animals():
    animals.append(request.get_json())
    return "", 204
>>>>>>> b409c71 (Add New)
    

