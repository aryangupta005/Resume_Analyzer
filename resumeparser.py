import google.generativeai as genai
import json
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

api_key = config['GEMINI_API_KEY']
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def ats_extractor(resume_data):
    """
    Extracts information from a resume using Gemini

    Args:
        resume_data: String containing the resume content

    Returns:
        dict: Extracted information in JSON format
    """
    
    prompt = """
    You are an AI trained to extract information from resumes. Given a resume, identify and return the following details in JSON format:

    1. Full Name
    2. Email Address
    3. GitHub Profile URL
    4. LinkedIn Profile URL
    5. Education Details (degree, institution, dates)
    6. Employment History (company, position, dates)
    7. Project Details in Short
    8. Certifications
    9. Achievements and Awards
    10. Technical Skills
    11. Soft Skills
    12. Other Relevant Details
    
    Note:- In case of email address, an extra 'pe' is coming at the start in some cases. Ignore irrelevant 'pe' before email address. 
    """

    response = model.generate_content(prompt + resume_data)
    response_text = response.text.strip()
    if response_text.startswith("```json"):
        response_text = response_text[7:].strip()  
    if response_text.endswith("```"):
        response_text = response_text[:-3].strip()
    print(response.text)
    return response_text
