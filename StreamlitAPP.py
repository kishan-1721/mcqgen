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

from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

#loading json file
with open("C:\Users\kisha\Projects\Generative_AI\mcqgen\Response.json", 'r') as file:
    RESPONSE_JSON = json.load(file)

#Creating Title for the App
st.title("MCQ Creator Application with Langchain")

# #Create a form using st.form
# with st.form('user_inputs'):
#     #File Upload
