# 📧 Cold Mail Generator
A cold email generator designed for service companies utilizing Groq, Langchain, and Streamlit. This tool enables users to enter the URL of a company's careers page, from which it extracts job listings. It then creates personalized cold emails that incorporate pertinent portfolio links drawn from a vector database, tailored to the specific job descriptions.

## How to run
1. We first need to get an API_KEY from here: https://console.groq.com/keys. Inside `app/.env` update the value of `GROQ_API_KEY` with the API_KEY you created. 


2. To get started, first install the dependencies using:
    ```commandline
     pip install -r requirements.txt
    ```
   
3. Run the streamlit app:
   ```commandline
   streamlit run app/main.py
   ```
   
