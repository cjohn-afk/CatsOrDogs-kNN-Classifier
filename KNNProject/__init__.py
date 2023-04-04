from flask import Flask, render_template
from KNNProject.knn import model, cReport

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('content.html', report=cReport);
