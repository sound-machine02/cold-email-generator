# 📧 Cold Mail Generator
A cold email generator designed for service companies utilizing Groq, Langchain, and Streamlit. This tool enables users to enter the URL of a company's careers page, from which it extracts job listings. It then creates personalized cold emails that incorporate pertinent portfolio links drawn from a vector database, tailored to the specific job descriptions.

## Tech Stack

| Component | Technology |
|------------|------------|
| Frontend | Streamlit |
| LLM | Llama 3.1 |
| Framework | LangChain |
| Vector Database | ChromaDB |
| Language | Python |
| Inference | Groq API |

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

## How It Works

1. User enters a careers page URL.
2. The application scrapes the page and extracts job descriptions.
3. Portfolio projects are embedded and stored in ChromaDB.
4. Relevant projects are retrieved through similarity search.
5. LangChain orchestrates prompts and context.
6. Llama 3.1 generates a personalized cold email.
7. The email is displayed in the Streamlit UI.

## Project Structure

```
cold-email-generator/
│
├── README.md
├── requirements.txt
├── Nike Service Required_JD.txt
│
└── app/
    │
    ├── main.py                # Streamlit UI entry point
    ├── chains.py              # LangChain + Llama 3.1 email generation logic
    ├── portfolio.py           # ChromaDB portfolio management & retrieval
    ├── utils.py               # Career page scraping/processing utilities
    │
    ├── resource/
    │   └── my_portfolio.csv   # Portfolio dataset
    │
    └── vectorstore/
        ├── chroma.sqlite3
        └── 5e1a0b80-4764-4725-9ed3-aaba1c143de0/
            ├── data_level0.bin
            ├── header.bin
            ├── length.bin
            └── link_lists.bin
```
---
