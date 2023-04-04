from flask import Flask
from KNNProject.knn import model, cReport

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>" + str(cReport) + "</p>"
