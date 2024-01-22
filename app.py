from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import io
import base64

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemeni_response(input, pdf_content, prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        
        ## convert the PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path=r'C:\Program Files (x86)\poppler-23.11.0\Library\bin')
        
        first_page = images[0]
        
        # convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
    

## streamlit app
st.set_page_config(page_title="ATS Resume Expert", page_icon=":robot:")
st.header("ATS Resume Expert")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume: ", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF uploaded Sucessfully")
    
submit1=st.button("Tell me about the resume")
sumbit2=st.button("How can I improve my skills")
# submit3=st.button("What are the keywords that are missing")
submit3=st.button("Percentage match")

input_prompt1="""
You are an experienced Technical Human resource manager in the field of data science, your task is to review the provided resume againt the job description.
Please share your professional evaluation on wheather the candidate profile aligns with the role.
Highlight the strengths and weaknesses of the candidate in relation to the specified job role
"""

input_prompt2="""
You are an experienced Technical Human resource manager in the field of data science, your role is to scruthinze the resume in the light \
    of the job description and suggest improvements to the resume. Share your insights on the candidates sutiablity for the role \
        from an HR prespective. Additionally, offer the advice on enhancing the candidates skills and identify areas of improvements
"""

input_prompt3="""
You are an skilled ATS (applicant tracking system) scanner with a deep understanding of data science and ATS functionality.
you task is to evaluate the resume againt the job description and give me percentage match to the job description.
First the output should come as percentage and then keyword missing and last final thoughts
"""

if submit1:
    if uploaded_file is not None:
        pdf_parts = input_pdf_setup(uploaded_file)
        response = get_gemeni_response(input_prompt1, pdf_parts, input_text)
        st.subheader("The response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file")
        
elif sumbit2:
    if uploaded_file is not None:
        pdf_parts = input_pdf_setup(uploaded_file)
        response = get_gemeni_response(input_prompt2, pdf_parts, input_text)
        st.subheader("The response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file")  
        
elif submit3:
    if uploaded_file is not None:
        pdf_parts = input_pdf_setup(uploaded_file)
        response = get_gemeni_response(input_prompt3, pdf_parts, input_text)
        st.subheader("The response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file")

