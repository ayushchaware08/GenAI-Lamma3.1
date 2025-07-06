# Dummy UI
# import streamlit as st

# st.title("Cold Email Generator")
# jobPostUrl = "https://www.google.com/about/careers/applications/jobs/results/110690555461018310-software-engineer-iii-infrastructure-core" 
# url_input = st.text_input("Enter the URL:" , value=jobPostUrl)

# submit_button = st.button("Submit")

# if submit_button:
#     st.code("Hello Hiring Manager, I am Ayush, Junior SDE", language = 'markdown')

# run streamlit app: streamlit run .\app\main.py

import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text

# To resolve the USER_AGENT environment variable not set warning, set the USER_AGENT environment variable before making any web requests.
import os
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"



def createStreamlitApp(llm, portfolio, clean_text):
    st.title("Cold Email Generator")

    # this block: to initialize the chat model only once (avoid caching issues)
    if "chat_model" not in st.session_state:
        from langchain_groq import ChatGroq
        import os
        st.session_state.chat_model = ChatGroq(
            model='deepseek-r1-distill-llama-70b',
            temperature=0.1,
            api_key=os.environ["GROQ_API_KEY"]
        )
    model = st.session_state.chat_model

    url_input = st.text_input("Enter the URL:", value="https://www.google.com/about/careers/applications/jobs/results/110690555461018310-software-engineer-iii-infrastructure-core")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader(url_input)
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_job(data)
            for job in jobs:
                skills = job.get('skills', [])
                if isinstance(skills, str):
                    skills = [skills]
                links = portfolio.query_links(skills)
                email = llm.generate_email(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    st.set_page_config(page_title="Cold Email Generator", page_icon="✉️", layout="wide")
    createStreamlitApp(Chain(), Portfolio(), clean_text)
