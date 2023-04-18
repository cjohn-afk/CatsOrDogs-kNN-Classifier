from flask import Flask, request, render_template
from KNNProject.knn import model, cReport
import os
import datetime

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    now = datetime.datetime.now()
    image = request.files['image']
    image.save('./KNNProject/uploads/test_img_{}.jpg'.format(now.strftime('%Y%m%d_%H%M%S')))
    return render_template('upload.html')

@app.route("/")
def hello_world():
    return render_template('content.html', report=cReport)

