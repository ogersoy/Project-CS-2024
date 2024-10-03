from utils import process_documents, answer_question
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class ALBERTChatbot:
    def __init__(self):
        self.chunks = None
        self.doc_embeddings = None
        self.tokenizer = None
        self.embedding_model = None
        self.classification_model = None

    def load_documents(self, input_directory):
        logger.info(f"Loading and processing documents from {input_directory}...")
        input_directory = Path(input_directory)
        try:
            self.chunks, self.doc_embeddings, self.tokenizer, self.embedding_model, self.classification_model = process_documents(input_directory)
            logger.info(f"Documents loaded, cleaned, and processed. Number of chunks: {len(self.chunks)}")
        except Exception as e:
            logger.error(f"Error in load_documents: {str(e)}")
            raise

    def ask_question(self, query):
        if self.chunks is None or len(self.chunks) == 0:
            logger.warning("No documents loaded or processed. Cannot process the query.")
            return "Please load documents first.", "No documents loaded"

        try:
            answer, relevance = answer_question(query, self.chunks, self.doc_embeddings,
                                                self.tokenizer, self.embedding_model, self.classification_model)
            logger.info(f"Processed query: '{query}'. Relevance: {relevance}")
            return answer, relevance
        except Exception as e:
            logger.error(f"Error processing query '{query}': {str(e)}")
            return f"An error occurred while processing your question: {str(e)}", "Error"