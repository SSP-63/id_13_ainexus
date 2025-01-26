import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Azure Text Analytics API Setup
API_KEY = "5Phr7UTKDnI4T8i3IlnvFNTf2vxjctS7mgSQ2diNbUDdm5Pl5oXMJQQJ99BAACYeBjFXJ3w3AAAaACOGa7G3"
ENDPOINT = "https://hackassp.cognitiveservices.azure.com/"

def authenticate_client():
    """Authenticate Azure Text Analytics client."""
    credentials = AzureKeyCredential(API_KEY)
    client = TextAnalyticsClient(endpoint=ENDPOINT, credential=credentials)
    return client

def analyze_sentiments(client, feedback_list):
    """Analyze sentiments using Azure Text Analytics API."""
    try:
        response = client.analyze_sentiment(documents=feedback_list)
        return response
    except Exception as e:
        st.error(f"Error during sentiment analysis: {e}")
        return []

def plot_pie_chart(sentiment_counts):
    """Plot a pie chart of sentiment counts."""
    fig, ax = plt.subplots()
    labels = ["Satisfactory", "Needs Improvement", "Neutral"]  # Updated labels
    sizes = [
        sentiment_counts.get("positive", 0),
        sentiment_counts.get("negative", 0),
        sentiment_counts.get("neutral", 0)
    ]
    colors = ['#2ecc71', '#e74c3c', '#f1c40f']
    explode = (0.1, 0, 0)  # Explode the satisfactory slice slightly
    ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    ax.set_title("Sentiment Distribution")
    st.pyplot(fig)

def plot_wordcloud(words, title):
    """Plot a word cloud for a given set of words."""
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(words)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    ax.set_title(title, fontsize=16)
    st.pyplot(fig)

def main():
    st.set_page_config(page_title="Feedback Analysis", layout="wide")
    st.title("📈 Student Feedback Analysis")

    # Sidebar for file upload
    st.sidebar.header("Upload Feedback Data")
    uploaded_file = st.sidebar.file_uploader("Upload your feedback CSV file", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        # Extract feedback text from the second column
        feedback_text = df.iloc[:, 1].tolist()
        st.subheader("Uploaded Feedback Data")
        st.dataframe(df, use_container_width=True)

        # Authenticate and analyze sentiment
        client = authenticate_client()
        sentiment_results = analyze_sentiments(client, feedback_text)

        # Process sentiment results
        sentiments = [result.sentiment for result in sentiment_results]
        sentiment_counts = Counter(sentiments)

        # Display sentiment distribution
        st.subheader("Sentiment Analysis Results")
        col1, col2 = st.columns([2, 3])

        with col1:
            st.markdown("### Sentiment Distribution")
            plot_pie_chart(sentiment_counts)

        with col2:
            st.markdown("### Sentiment Counts")
            sentiment_table = pd.DataFrame(
                {"Sentiment": ["Satisfactory", "Needs Improvement", "Neutral"],
                 "Count": [
                     sentiment_counts.get("positive", 0),
                     sentiment_counts.get("negative", 0),
                     sentiment_counts.get("neutral", 0)]}
            )
            st.write(sentiment_table)

        # Extract common keywords from feedback
        positive_feedback = [feedback_text[i] for i, result in enumerate(sentiment_results) if result.sentiment == "positive"]
        negative_feedback = [feedback_text[i] for i, result in enumerate(sentiment_results) if result.sentiment == "negative"]

        positive_keywords = Counter(" ".join(positive_feedback).split())
        negative_keywords = Counter(" ".join(negative_feedback).split())

        # Remove common stopwords (optional)
        stopwords = set(["the", "and", "is", "to", "in", "of", "a", "this", "it", "for", "was"])
        positive_keywords = {word: count for word, count in positive_keywords.items() if word.lower() not in stopwords}
        negative_keywords = {word: count for word, count in negative_keywords.items() if word.lower() not in stopwords}

        # Display word clouds
        st.subheader("Keyword Analysis")
        col3, col4 = st.columns(2)

        with col3:
            st.markdown("### Positive Feedback Keywords")
            plot_wordcloud(positive_keywords, "Positive Feedback")

        with col4:
            st.markdown("### Negative Feedback Keywords")
            plot_wordcloud(negative_keywords, "Negative Feedback")

    else:
        st.warning("Please upload a CSV file to proceed.")

if __name__ == "__main__":
    main()
