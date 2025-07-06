## web Scrapper for creating cold email wrt job description provided

LLM API: GroqCloud
vectorDatabase: chromadb / pinecone
scrap data from website > using langchain web_base_Loader
streamlit


- [Web Base Loader](https://python.langchain.com/docs/integrations/document_loaders/web_base/#loader-features)
- [ChromaDB](https://docs.trychroma.com/docs/overview/getting-started)
- Streamlit
- [dot environment](https://pypi.org/project/python-dotenv/)

# Cold Email Generator for Job Descriptions 

This project is a **web scraper and cold email generator** that leverages LLMs (via GroqCloud API), vector databases (ChromaDB), and Streamlit for a seamless user experience. It scrapes job descriptions from the web, extracts structured job information, matches your portfolio, and generates a personalized cold email for recruiters. Usefull tool for the job applicant to write cold Emails.

---

## Features

- **Web Scraping:** Extracts job descriptions from any public job posting using [LangChain's WebBaseLoader](https://python.langchain.com/docs/integrations/document_loaders/web_base/#loader-features).
- **LLM Integration:** Uses GroqCloud's LLM API for job extraction and email generation.
- **Portfolio Matching:** Stores your tech stack and portfolio links in [ChromaDB](https://docs.trychroma.com/docs/overview/getting-started) for relevant matching.
- **Streamlit UI:** Simple web interface for inputting job URLs and viewing generated emails.
- **Environment Management:** Uses `.env` for secure API key management.

---

## How It Works

1. **Input:** Enter a job posting URL in the Streamlit app.
2. **Scraping:** The app scrapes and cleans the job description.
3. **Extraction:** An LLM extracts structured job data (role, experience, skills, description).
4. **Portfolio Match:** Your portfolio is queried for relevant projects/skills.
5. **Email Generation:** The LLM generates a tailored cold email using the job info and your portfolio.
6. **Output:** The email is displayed in the Streamlit app, ready to copy and send.

---

## Setup

1. **Clone the repository**
    ```bash
    git clone <repo-url>
    cd ColdEmailUsingGroq
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your environment variables**
    - Create a `.env` file in the root directory:
        ```
        GROQ_API_KEY=your_groq_api_key_here
        ```

4. **Prepare your portfolio**
    - Place your `my_portfolio.csv` in `app/resource/` with columns: `Techstack`, `Links`.

5. **Run the Streamlit app**
    ```bash
    streamlit run [main.py](http://_vscodecontentref_/0)
    ```

---

## Tech Stack

- [LangChain](https://python.langchain.com/) (WebBaseLoader, Prompting)
- [GroqCloud LLM API](https://groq.com/)
- [ChromaDB](https://www.trychroma.com/) (vector database)
- [Streamlit](https://streamlit.io/) (UI)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (env management)
- [pandas](https://pandas.pydata.org/) (portfolio CSV handling)

---

## References

- [LangChain WebBaseLoader Docs](https://python.langchain.com/docs/integrations/document_loaders/web_base/#loader-features)
- [ChromaDB Docs](https://docs.trychroma.com/docs/overview/getting-started)
- [Streamlit Docs](https://docs.streamlit.io/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## License

MIT License

---
