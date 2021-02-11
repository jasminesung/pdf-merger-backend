import os
from flask import Flask, make_response, request
from flask_cors import CORS, cross_origin
from PyPDF2 import PdfFileMerger

app = Flask(__name__)
cors = CORS(app)

@app.route('/merge', methods=['POST'])
@cross_origin()
def merge():
    merger = PdfFileMerger()
    # r = make_response('hihi')
    print(request.files)
    for key in request.files:
        print(key, ':',  request.files[key])
        merger.append(request.files[key])
    merger.write('./temp/mergedPdf.pdf')
    merger.close()
    return 'hihi'
