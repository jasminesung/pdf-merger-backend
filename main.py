from flask import Flask, request, send_from_directory, current_app
from flask_cors import CORS, cross_origin
import PyPDF2

app = Flask(__name__)
cors = CORS(app)

@app.route('/merge', methods=['POST'])
@cross_origin()
def merge():
    if checkPdfValid(request.files):
        merger = PyPDF2.PdfFileMerger()
        for key in request.files:
            merger.append(request.files[key], 'rb')
            merger.write('mergedPdf.pdf')
            merger.close()
        return send_from_directory(directory=current_app.root_path, filename='mergedPdf.pdf', as_attachment=True, mimetype='application/pdf')
    else:
        return "Invalid PDF File.", 400

def checkPdfValid(fileList):
    print(fileList)
    for key in fileList:
        try:
            PyPDF2.PdfFileReader(fileList[key])
        except Exception as e:
            return False
        return True
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
