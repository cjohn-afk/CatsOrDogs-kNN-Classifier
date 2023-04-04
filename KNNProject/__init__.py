from flask import Flask
from KNNProject.knn import model, cReport

app = Flask(__name__)

def generate_report_table():
    report_table=""
    for s in cReport.splitlines():
        report_table += s + "<br>"

    return report_table

report_table = generate_report_table()

@app.route("/")
def hello_world():
    return "<p>" + report_table + "</p>"
