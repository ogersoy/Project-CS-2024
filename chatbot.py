import os
import logging
from lib.utils import process_documents, answer_question, setup_sentence_bert, create_document_embeddings
from transformers import pipeline

logger = logging.getLogger(__name__)

class HuggingFaceChatbot:
    def __init__(self, input_directory):
        """Initialize the chatbot by processing markdown documents in the input directory."""
        try:
            logger.info(f"Loading and processing documents from {input_directory}")
            # Set up Sentence-BERT for better embeddings
            self.embedding_model = setup_sentence_bert()
            
            # Load text generation model (e.g., GPT-2 or similar)
            self.generator = pipeline('text-generation', model='gpt2')  # You can choose a more suitable model
            
            # Process the documents and create embeddings
            self.chunks, self.tokenizer, self.embedding_model, self.classification_model = process_documents(input_directory)
            self.doc_embeddings = create_document_embeddings(self.chunks, self.embedding_model)
            
            logger.info(f"Documents loaded and processed successfully")
        except Exception as e:
            logger.error(f"Error initializing chatbot: {str(e)}", exc_info=True)
            raise

    def generate_answer(self, context):
        """Generate a more coherent answer based on the context."""
        prompt = f"Based on the following information, provide a concise explanation: {context}"
        generated = self.generator(prompt, max_new_tokens=100, num_return_sequences=1, do_sample=True, truncation=True)
        return generated[0]['generated_text']

    def ask_question(self, query):
        """Process a query and return a coherent answer."""
        # Handle simple queries like "hi", "hello", etc.
        if query.lower() in ["hi", "hello", "hey"]:
            return "Hello! How can I assist you with the documents?"

        try:
            logger.debug(f"Processing query: {query}")
            relevant_chunk = answer_question(
                query=query, 
                chunks=self.chunks, 
                doc_embeddings=self.doc_embeddings, 
                tokenizer=self.tokenizer, 
                embedding_model=self.embedding_model, 
                classification_model=self.classification_model
            )

            # Ensure relevant_chunk is a string before passing to the generator
            if isinstance(relevant_chunk, tuple):
                relevant_chunk = relevant_chunk[0]  # Extract the string if it's a tuple

            # Generate a coherent answer using the retrieved chunk
            answer = self.generate_answer(relevant_chunk)
            logger.debug(f"Generated coherent answer: {answer[:100]}...")  # Log first 100 chars of generated answer

            return answer
        except Exception as e:
            logger.error(f"Error processing query '{query}': {str(e)}", exc_info=True)
            return f"An error occurred: {str(e)}"
