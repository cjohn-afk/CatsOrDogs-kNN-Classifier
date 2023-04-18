from flask import Flask, request, render_template, url_for
from KNNProject.knn import model, cReport, sp
from KNNProject.imageclassifier.testimage.simpletestimageloader import SimpleTestImageLoader
import os
import datetime

app = Flask(__name__)

# @app.route('/upload', methods=['POST'])
# def upload():
#     now = datetime.datetime.now()
#     image = request.files['image']
#     image.save('./KNNProject/uploads/test_img_{}.jpg'.format(now.strftime('%Y%m%d_%H%M%S')))
#     return render_template('upload.html')

@app.route("/", methods=['GET','POST'])
def index():
    classname = None
    pictureurl  = None
    if request.method == 'POST':
        now = datetime.datetime.now()
        image = request.files['image']
        filename = 'uploads/test_img_{}.jpg'.format(now.strftime('%Y%m%d_%H%M%S'))
        image.save('./KNNProject/static/' + filename)
        pictureurl = url_for('static', filename=filename)
        classname = classify_image('./KNNProject/static/' + filename)


    return render_template('content.html', report=cReport, pictureurl=pictureurl, classname=classname)


def classify_image(filename):
    stil = SimpleTestImageLoader(preprocessors=[sp])
    data = stil.load(filename)
    data = data.reshape(data.shape[0], 3072)

    return 'cat' if model.predict(data)[0] == 0 else 'dog'
