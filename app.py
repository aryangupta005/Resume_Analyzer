import os
import sys
from flask import Flask, request, render_template
from pypdf import PdfReader 
import json
from resumeparser import ats_extractor

sys.path.insert(0, os.path.abspath(os.getcwd()))

UPLOAD_PATH = r"__DATA__"
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/process", methods=["POST"])
def ats():
    if 'pdf_doc' not in request.files:
        return render_template('index.html', error="No PDF file uploaded. Please upload a valid PDF.")

    doc = request.files['pdf_doc']
    
    if doc.filename == '':
        return render_template('index.html', error="No file selected. Please select a PDF file to upload.")

    # Save the uploaded PDF file
    doc.save(os.path.join(UPLOAD_PATH, "file.pdf"))
    doc_path = os.path.join(UPLOAD_PATH, "file.pdf")
    
    # Read the file and extract information
    data = _read_file_from_path(doc_path)
    json_data = ats_extractor(data)
    
    try:
        json_object = json.loads(json_data)
    except ValueError as e:
        print("Invalid JSON response:", e)
        json_object = {}

    print("Processed Data:", json_object)
    
    return render_template('index.html', data=json.dumps(json_object))

def _read_file_from_path(path):
    reader = PdfReader(path) 
    data = ""

    for page_no in range(len(reader.pages)):
        page = reader.pages[page_no] 
        data += page.extract_text()

    return data 

if __name__ == "__main__":
    app.run(port=8000, debug=True)
