import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_table_data
from src.mcqgenerator.logger import logging
import streamlit as st
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain 

# Importing necessary packages from langchain
# from langchain.chat_models import ChatOpenAI

from langchain_openai import ChatOpenAI


# from langchain_community.chat_models import ChatOpenAI

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_community.callbacks import get_openai_callback

#loading json file
with open(r"C:\Users\kisha\Projects\Generative_AI\mcqgen\Response.json", 'r') as file:
    RESPONSE_JSON = json.load(file)

#Creating Title for the App
st.title("MCQ Creator Application with Langchain")


# Create a form using st.form
with st.form("user_inputs"):
    # File Uploader
    uploaded_file = st.file_uploader("Upload a PDF or txt file")

    # Input Fields
    mcq_count = st.number_input("No. of MCQs", min_value=3, max_value=50)
    subject = st.text_input("Insert Subject", max_chars=20)
    tone = st.text_input("Complexity Level of Questions", max_chars=20, placeholder="Simple")

    # Button
    button = st.form_submit_button("Create MCQs")

    # Check if the button is clicked and all fields have input
    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Loading..."):
            try:
                # Read file
                text = read_file(uploaded_file)
                #Count Tokens and the cost of API call
                #How to setup Token Usage Tracking in LangChain
                
                with get_openai_callback() as cb:
                    response=generate_evaluate_chain(
                        {
                            "text": text,
                            "number": mcq_count,
                            "subject":subject,
                            "tone": tone,
                            "response_json": json.dumps(RESPONSE_JSON)
                        }
                        )


                # Display success message or result
                # st.success("MCQs created successfully!")

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")


