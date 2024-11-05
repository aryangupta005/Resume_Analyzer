# Resume Analyzer Using Gemini

## Overview

The Resume Parser is a powerful tool designed to automate the extraction and analysis of key information from resumes. By leveraging the Gemini API, this application converts unstructured resume data into structured formats, enabling efficient data processing. The parser provides personalized job role and certification recommendations based on extracted data.

## Steps to Run the App (Locally) :-

### 1. Clone the repository:
```
git clone https://github.com/GDGouravDey/Resume_Analyzer.git
cd Resume_Analyzer
```
### 2. Set up a virtual environment:
```
python -m venv venv
source venv/bin/activate
On Windows, use `venv\Scripts\activate`
```
### 3. Install the dependencies:
```
pip install -r requirements.txt
```
### 4. Configure environment variables:
```
Enter your GEMINI API KEY in the .env file in the root directory.
```
### 5. Run the Flask App
```
flask --app main run
```


