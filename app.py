import os
import logging
from flask import Flask, render_template, request, jsonify
from chatbot import HuggingFaceChatbot

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set Hugging Face token
os.environ['HUGGINGFACE_TOKEN'] = 'Your own token'
# For example: os.environ['HUGGINGFACE_TOKEN'] = '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'

# Check for Hugging Face token
if 'HUGGINGFACE_TOKEN' not in os.environ:
    raise ValueError("HUGGINGFACE_TOKEN environment variable is not set")

# Initialize Flask application
app = Flask(__name__)

# Set the input directory for documents
input_directory = os.path.join('C:', 'Users', 'Mahta', 'projectcs', 'TSpec-LLM', 'test')

# in window yixin'example
#input_directory = r'D:\Python\TsLLM\TSpec-LLM\3GPP-clean\Rel-8\21_series'

# Convert Windows path to WSL path if necessary
if os.name == 'posix' and input_directory.startswith('C:'):
    input_directory = '/mnt/c' + input_directory[2:].replace('\\', '/')

# Initialize the chatbot with self-RAG
try:
    chatbot = HuggingFaceChatbot(input_directory=input_directory)
    logger.info("Chatbot initialized successfully")
except Exception as e:
    logger.error(f"Error initializing chatbot: {str(e)}", exc_info=True)
    raise


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    """Process the user's question using self-RAG and return an answer."""
    question = request.form['question']
    try:
        logger.debug(f"Received question: {question}")

        # Use the chatbot to process the question with self-RAG
        answer = chatbot.ask_question(question)

        logger.debug(f"Generated answer: {answer[:100]}...")  # Log the first 100 characters of the generated answer
    except Exception as e:
        logger.error(f"Error processing question: {str(e)}", exc_info=True)
        answer = f"An error occurred: {str(e)}"

    return jsonify({'answer': answer})


@app.route('/system_message', methods=['GET'])
def get_system_message():
    """Retrieve a system message."""
    try:
        return jsonify({'system_message': "This is the system message."})
    except Exception as e:
        logger.error(f"Error reading system message: {str(e)}", exc_info=True)
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
