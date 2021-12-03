from flask import Flask, render_template, request , flash , Markup , send_file
import flask
import os
import shutil
import csv
from fpdf import FPDF
import datetime
from datetime import datetime
from datetime import date
import helper
import helper2
import mini
app = Flask(__name__)
app.secret_key = b'pavansai@1916'

@app.route('/')
def get():
    return render_template('index.html')

def storer_1():
        if(os.path.exists("./templates/output")):
            shutil.rmtree("./templates/output")
        else:
            pass
        os.mkdir("./templates/output")
        if(os.path.exists("generated")):
            shutil.rmtree("generated")
        else:
            pass
        os.mkdir("generated")




@app.route("/Range" ,methods=['POST' , "GET"])
def generate_marksheet():
    return helper.function_1()



@app.route("/all" , methods=["POST","GET"])
def generate_all_sheets():
    if flask.request.method=='POST':
        storer_1()

    helper2.function_2()
    return render_template("index.html")



@app.route("/data" , methods=["POST", "GET"])
def data():
    mini.storer()
    if flask.request.method == 'POST':
        return mini.function()



if __name__ == '__main__':
    app.run(debug=True)


