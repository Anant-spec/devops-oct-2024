from flask import Flask, request
import json


app = Flask(__name__)





animals = {"Dog":10,"cat":8}
@app.get("/animals")
def get_animal():
    return animals


    

