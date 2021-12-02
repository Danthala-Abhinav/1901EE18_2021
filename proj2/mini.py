from flask import Flask, render_template, request , flash , Markup , send_file
import flask
import os
import shutil
import csv
from fpdf import FPDF
import datetime
from datetime import datetime
from datetime import date

def function():
        grade = request.files["grades"]
        name = request.files["names_roll"]
        subject=request.files['subject_master']
        stamps=request.files['stamp']
        signature=request.files['signature']
        grade.save(os.path.join("files", (grade.filename)))
        name.save(os.path.join("files",(name.filename)))
        subject.save(os.path.join("files",(subject.filename)))
        stamps.save(os.path.join("files1",(stamps.filename)))
        signature.save(os.path.join("files2",(signature.filename)))
         #flash("Uploaded  successfully :)"  , "info")
        print(stamps.filename)
        return render_template("index.html" )


def storer():
    if(os.path.exists("files")):
        shutil.rmtree("files")
    else:
        pass
    os.mkdir("files")
    if(os.path.exists("files1")):
        shutil.rmtree("files1")
    else:
        pass
    os.mkdir("files1")
    if(os.path.exists("files2")):
        shutil.rmtree("files2")
    else:
        pass
    os.mkdir("files2")
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