from transformers import pipeline
from keybert import KeyBERT
import requests
from bs4 import BeautifulSoup
import re
import os
from gtts import gTTS


def clean_html(raw_html):
    """Removes HTML tags and extracts clean text from a summary."""
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text(separator=" ", strip=True)  # Extracts text without tags

def fetch_news(company_name, max_articles=10):
    """
    Fetches news articles from Google News RSS feed for a given company.
    Cleans up summary to remove HTML elements.
    """
    query = company_name.replace(' ', '+')
    rss_url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"

    try:
        response = requests.get(rss_url)
        response.raise_for_status()  # Raise exception for HTTP errors
        soup = BeautifulSoup(response.content, 'lxml-xml')

        items = soup.findAll('item')
        articles = []

        for item in items[:max_articles]:
            raw_summary = item.description.text if item.description else "No summary available"
            cleaned_summary = clean_html(raw_summary)  # Remove HTML tags

            articles.append({
                'title': item.title.text,
                'link': item.link.text,
                'pubDate': item.pubDate.text,
                'summary': cleaned_summary
            })

        return articles

    except Exception as e:
        print(f"Error fetching news: {e}")
        return None


# Load the summarization model once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    """
    Summarizes the input text.
    """
    # Avoid errors for very short texts
    if len(text.split()) < 50:
        return text

    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']



# Load the sentiment analysis model once
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """
    Analyzes sentiment of the input text.
    Returns Positive, Negative, or Neutral.
    """
    result = sentiment_pipeline(text)[0]
    label = result['label']

    if label == 'POSITIVE':
        return 'Positive'
    elif label == 'NEGATIVE':
        return 'Negative'
    else:
        return 'Neutral'


# Load KeyBERT model once
kw_model = KeyBERT(model='distilbert-base-nli-mean-tokens')

def extract_topics(text, top_n=3):
    """
    Extracts key topics from the text.
    """
    keywords = kw_model.extract_keywords(text, top_n=top_n)
    topics = [kw[0] for kw in keywords]
    return topics


def comparative_analysis(articles_data):
    """
    Performs comparative sentiment analysis and topic overlap.
    """
    sentiments = {"Positive": 0, "Negative": 0, "Neutral": 0}
    all_topics = []

    # Tally sentiments and collect all topics
    for article in articles_data:
        sentiments[article['Sentiment']] += 1
        all_topics.extend(article['Topics'])

    # Get common and unique topics
    topic_counts = {}
    for topic in all_topics:
        topic_counts[topic] = topic_counts.get(topic, 0) + 1

    common_topics = [topic for topic, count in topic_counts.items() if count > 1]
    unique_topics = [topic for topic, count in topic_counts.items() if count == 1]

    # Build an insights summary (basic version)
    insights = [
        {
            "Comparison": "Some articles highlight growth, others mention risks.",
            "Impact": "Mixed reactions are possible from investors and stakeholders."
        }
    ]

    return {
        "Sentiment Distribution": sentiments,
        "Topic Overlap": {
            "Common Topics": common_topics,
            "Unique Topics": unique_topics
        },
        "Coverage Differences": insights
    }



# Load Hindi TTS model once
def generate_hindi_tts(text, file_path='assets/summary.mp3'):
    """
    Converts the provided text to Hindi speech and saves it as an MP3 file.
    """
    if not os.path.exists('assets'):
        os.makedirs('assets')

    # Generate speech in Hindi
    tts = gTTS(text=text, lang='hi')
    tts.save(file_path)

    return file_path