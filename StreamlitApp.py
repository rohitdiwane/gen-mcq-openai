import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenrator.utils import read_file
from src.mcqgenrator.utils import get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.mcqgenrator.mcqgenrator import generate_evaluate_chain
from src.mcqgenrator.logger import logging

#loading json file
with open(r"D:\NLP_Specialization\Gen_AI\LangChain_LLM\mcq_gen_project-main\mcq_gen_project-main\Response.json", 'r') as file:
    RESPONSE_JSON = json.load(file)


#creating a title for the app
st.title("🎯MCQ's Generator Application with LangChain 🐦📝🔗")


with st.form("user input"):
    uploaded_file=st.file_uploader("upload pdf or text")

    mcq_count=st.number_input("no of mcq's", min_value=3, max_value=50)

    subject=st.text_input("Insert Subject",max_chars=20)

    tone=st.text_input("Complexity Level Of Questions", max_chars=20, placeholder="Simple")

    button=st.form_submit_button("Create MCQs")

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text=read_file(uploaded_file)
                #Count tokens and the cost of API call
                with get_openai_callback() as cb:
                    response=generate_evaluate_chain(
                        {
                        "text": text,
                        "number": mcq_count,
                        "subject":subject,
                        "tone": tone,
                        "RESPONSE_JSON": json.dumps(RESPONSE_JSON)
                            }
                    )
                #st.write(response)

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")

            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")
                if isinstance(response, dict):
                    #Extract the quiz data from the response
                    quiz=response.get("quiz", None)
                    if quiz is not None:
                        table_data=get_table_data(quiz)
                        if table_data is not None:
                            df=pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)
                            #Display the review in atext box as well
                            st.text_area(label="Review", value=response["review"])
                        else:
                            st.error("Error in the table data")

                else:
                    st.write(response)