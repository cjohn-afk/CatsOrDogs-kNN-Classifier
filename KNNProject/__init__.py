from flask import Flask, request, render_template
from KNNProject.knn import model, cReport
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['image'];
    image.save('./upload/test.jpg')
    return 'success!'

@app.route("/")
def hello_world():
    return render_template('content.html', report=cReport);

