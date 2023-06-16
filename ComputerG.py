import streamlit as st

st.set_page_config(page_title="ComputerG", page_icon="🚀", layout="wide", )   

@st.cache(suppress_st_warning=True,show_spinner=False,allow_output_mutation=True) 

def get_info(prompt):

    code = ''

    from bardapi import Bard

    import os

    os.environ['_BARD_API_KEY']="XQgxyJ_-9p24OKrA5P1qvezYq80Ip6QLB7PKx9aDEVLS2y_--rnWOUmh_J1s5WkE3e0PAg."

    return Bard().get_answer(prompt)['content']

st.title("ComputerG")

prompt = st.text_input("Paste your prompt here 👇", placeholder='Prompt')

if prompt:

    code = get_info(prompt)

    with st.container():

        st.code(code,language='python')
