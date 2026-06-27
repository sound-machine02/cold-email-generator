import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    # Set up page configuration    
    # Main title and description
    st.title("📧 Cold Mail Generator")
    st.subheader("Generate professional cold emails tailored to service requirement postings.")
    st.write("Enter the URL to generate a personalized cold email. ")

    # URL input field
    url_input = st.text_input(
        label="🔗 Job Posting URL",
        placeholder="e.g., https://jobs.nike.com/job/R-43826",
        help="Paste the URL of the job posting here."
    )
    
    # Submission button
    submit_button = st.button("Generate Email ✉️")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)


