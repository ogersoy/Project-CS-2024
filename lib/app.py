from flask import Flask, render_template, request, jsonify
from chatbot import ALBERTChatbot
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Initialize the chatbot
chatbot = ALBERTChatbot()

# Set the input directory
input_directory = 'D:/Python/TsLLM/TSpec-LLM/3GPP-clean/Rel-8/21_series'

# Load documents
try:
    if not os.path.exists(input_directory):
        raise FileNotFoundError(f"Directory not found: '{input_directory}'")

    md_files = [f for f in os.listdir(input_directory) if f.endswith('.md')]
    if not md_files:
        raise FileNotFoundError(f"No markdown files found in '{input_directory}'")

    logger.info(f"Found {len(md_files)} markdown files in {input_directory}")
    chatbot.load_documents(input_directory)
    logger.info(f"Documents loaded successfully from {input_directory}")
except Exception as e:
    logger.error(f"Error loading documents: {str(e)}")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    try:
        answer, relevance = chatbot.ask_question(question)
    except Exception as e:
        logger.error(f"Error processing question: {str(e)}")
        answer = f"An error occurred: {str(e)}"
        relevance = "Error"
    return jsonify({'answer': answer, 'relevance': relevance})


if __name__ == '__main__':
    app.run(debug=True)