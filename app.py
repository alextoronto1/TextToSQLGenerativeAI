# Install the pre-built tokenizers package
!pip install tokenizers==0.10.3

# Import necessary libraries
from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import sqlite3

from transformers import pipeline  # Import pipeline from transformers package

# Load the ChatGPT pipeline
chatgpt = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")

# Define a function to generate responses
def generate_response(input_text, max_length=100):
    response = chatgpt(input_text, max_length=max_length)[0]['generated_text']
    return response

# Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

# Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("ChatGPT App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# If submit is clicked
if submit:
    response = generate_response(question)
    st.subheader("The Response is")
    st.write(response)