import streamlit as st
from utils import fetch_news, summarize_text, analyze_sentiment, extract_topics,comparative_analysis
from utils import generate_hindi_tts

st.set_page_config(page_title="📰 News Summarization + Hindi TTS", layout="wide")

st.title("📰 News Summarization + Sentiment + Topics Analyzer")

# Company input
company_name = st.text_input("Enter Company Name", value="Tesla")

# Button to trigger the analysis
if st.button("Fetch News and Analyze"):
    with st.spinner(f"Fetching news articles for {company_name}..."):
        articles = fetch_news(company_name)

    if not articles:
        st.warning("No articles found for this company. Try another.")
    else:
        # List to store processed articles
        summarized_articles = []

        st.success(f"Fetched {len(articles)} articles! Processing...")

        # Process each article
        for idx, art in enumerate(articles):
            st.markdown(f"### Article {idx + 1}: {art['title']}")
            st.markdown(f"[Read Full Article]({art['link']})")

            # Summarize the content (using description for simplicity)
            summary = summarize_text(art['summary'])
            sentiment = analyze_sentiment(summary)
            topics = extract_topics(summary)

            # Display in Streamlit
            st.write("**Summary:**", summary)
            st.write("**Sentiment:**", sentiment)
            st.write("**Topics:**", ", ".join(topics))

            # Append to our list
            summarized_articles.append({
                'Title': art['title'],
                'Summary': summary,
                'Sentiment': sentiment,
                'Topics': topics
            })

        # Done processing all articles!
        st.success("✅ Analysis Completed!")




# Comparative Sentiment and Topic Analysis
analysis = comparative_analysis(summarized_articles)

# Show Comparative Sentiment Distribution
st.subheader("📊 Comparative Sentiment Analysis")
st.json(analysis)




# Generate a final Hindi summary text
positive = analysis['Sentiment Distribution']['Positive']
negative = analysis['Sentiment Distribution']['Negative']
neutral = analysis['Sentiment Distribution']['Neutral']

# Craft the Hindi summary sentence (you can improve this)
hindi_summary_text = f"""
{company_name} से जुड़ी खबरों का विश्लेषण इस प्रकार है।
{positive} सकारात्मक, {negative} नकारात्मक, और {neutral} तटस्थ समाचार पाए गए हैं।
कंपनी से जुड़े सामान्य विषय हैं: {', '.join(analysis['Topic Overlap']['Common Topics'])}।
"""

# Generate the Hindi speech file
audio_file_path = generate_hindi_tts(hindi_summary_text)

# Streamlit audio player
st.subheader("🔊 Hindi Audio Summary")
audio_file = open(audio_file_path, 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/wav')
