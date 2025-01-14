from flask import Flask, request, jsonify
from transformers import pipeline
import requests
from bs4 import BeautifulSoup

# Initialize Flask app
app = Flask(__name__)


# Load a prebuilt transformer model for question answering
qa_pipeline = pipeline("question-answering")

# Documentation URLs
doc_urls = {
    "Segment": "https://segment.com/docs/?ref=nav",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

# Function to fetch and index documentation
def fetch_documentation():
    indexed_docs = {}

    for platform, url in doc_urls.items():
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text(" ", strip=True)
            indexed_docs[platform] = text

    return indexed_docs

# Index the documentation
indexed_docs = fetch_documentation()

# Helper function to process questions
def process_question(question):
    # Check for platform-specific keywords
    platform = None
    for key in doc_urls.keys():
        if key.lower() in question.lower():
            platform = key
            break

    if not platform:
        return "Sorry, I can only assist with Segment, mParticle, Lytics, and Zeotap-related questions."

    # Retrieve the relevant documentation
    documentation_text = indexed_docs.get(platform, "")

    if not documentation_text:
        return "Documentation for the selected platform is not available."

    # Use the QA pipeline to get the answer
    try:
        result = qa_pipeline({
            "context": documentation_text,
            "question": question
        })
        return result['answer']
    except Exception as e:
        return f"Error processing the question: {str(e)}"

# Flask routes
@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')

    if not question:
        return jsonify({"error": "No question provided."}), 400

    response = process_question(question)
    return jsonify({"response": response})

@app.route('/')
def home():
    return "CDP Support Agent Chatbot is running. Use the /ask endpoint to interact."

if __name__ == '__main__':
    app.run(debug=True)