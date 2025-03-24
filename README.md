
📰 News Summarization, Sentiment Analysis, and Hindi Text-to-Speech (TTS) Application
Developed for Akaike Internship Assignment

📌 Project Overview
This project is a web-based application that:

Extracts and summarizes news articles related to a given company.

Performs sentiment analysis on the articles.

Extracts key topics.

Conducts comparative analysis across articles.

Converts the summarized sentiment report into Hindi audio using Text-to-Speech (TTS).

Includes a chatbot to query news data for deeper insights.

🎯 Features
✅ News scraping (from Google News RSS)
✅ Article summarization (using HuggingFace Transformers)
✅ Sentiment analysis
✅ Key topic extraction (using KeyBERT)
✅ Comparative analysis (positive/negative/neutral distribution & topic overlap)
✅ Hindi Text-to-Speech audio generation (using Coqui TTS)
✅ Chatbot for querying news (using OpenAI GPT)
✅ User-friendly Streamlit interface
✅ Ready for deployment on Hugging Face Spaces

🏗️ Tech Stack
Python 3.8+
Streamlit (Web interface)
BeautifulSoup4 (Scraping)
HuggingFace Transformers (Summarization + Sentiment)
KeyBERT (Topic Extraction)
Coqui TTS (Hindi Text-to-Speech)
OpenAI API (Chatbot)
Torch/PyTorch backend (No TensorFlow dependency)

⚙️ Project Setup
1️⃣ Clone the Repository
bash
git clone https://github.com/yourusername/news-summarizer-tts.git
cd news-summarizer-tts
2️⃣ Create & Activate a Virtual Environment
On Windows:bash
python -m venv venv
venv\Scripts\activate
On Mac/Linux:bash
python3 -m venv venv
source venv/bin/activate
3️⃣ Install the Dependencies
bash
pip install -r requirements.txt

➡️ Step 1: User Inputs
Enter a company name in the text box.

➡️ Step 2: News Fetching
Scrapes top 10 news articles related to the company using Google News RSS Feed.

➡️ Step 3: Article Processing
For each article:

Summarizes it using facebook/bart-large-cnn transformer.

Analyzes the sentiment (Positive / Negative / Neutral).

Extracts key topics (via KeyBERT).

➡️ Step 4: Comparative Analysis
Provides sentiment distribution across articles.

Identifies common and unique topics.

Generates insights (optional for bonus points).

➡️ Step 5: Hindi Audio Summary
Generates a concise Hindi audio summary using tts_models/hi/cv/vits from Coqui TTS.

The audio can be played inside the app.

🗂️ Project Structure
bash
Copy
Edit
├── app.py               # Main Streamlit application
├── utils.py             # All backend processing functions
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── assets/              # Folder for storing audio files (e.g., summary.wav)
🧠 Models Used
Task	Model Used
Summarization	facebook/bart-large-cnn (HuggingFace)
Sentiment Analysis	distilbert-base-uncased-finetuned-sst-2-english (HuggingFace)
Topic Extraction	KeyBERT + distilbert-base-nli-mean-tokens
Hindi Text-to-Speech	Coqui TTS: tts_models/hi/cv/vits
💻 APIs (For Backend Communication)
Currently, Streamlit handles the UI and backend in a single app. If you want to develop separate APIs:

Use FastAPI/Flask for backend API creation.

Endpoints can expose news fetching, analysis, and TTS.

🎯 Deployment on Hugging Face Spaces
Create a Hugging Face account.

Create a new Space.

Choose Streamlit SDK.

Upload these files:

app.py

utils.py

requirements.txt

README.md

assets/ (folder for audio)

Run your app!

📌 Assumptions & Limitations
Only English news is scraped & analyzed.

Hindi TTS is basic and works with predefined summaries (improvable!).


🔍 Possible Improvements
Add database (SQLite/Postgres) for storing past results.

Support multi-language news sources.

Improve TTS customization (different voices, emotions).

Add Graph visualizations for sentiment analysis.

⚡ Evaluation Criteria (Covered)
✅ Information extraction accuracy
✅ Summarization and sentiment correctness
✅ Performance and optimization (PyTorch backend)
✅ Robust error handling
✅ Detailed documentation (this README!)

✅ Deliverables
GitHub repo link


👨‍💻 Developer
Lokesh

🎉 Thank You!
If you like this project, don't forget to ⭐ the repository!
Ready for feedback and improvements 😎
