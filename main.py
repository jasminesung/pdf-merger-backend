from flask import Flask, request, send_from_directory, current_app
from flask_cors import CORS, cross_origin
from PyPDF2 import PdfFileMerger

app = Flask(__name__)
cors = CORS(app)

@app.route('/merge', methods=['POST'])
@cross_origin()
def merge():
    merger = PdfFileMerger()
    for key in request.files:
        merger.append(request.files[key], 'rb')
    merger.write('mergedPdf.pdf')
    merger.close()
    return send_from_directory(directory=current_app.root_path, filename='mergedPdf.pdf', as_attachment=True, mimetype='application/pdf')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
