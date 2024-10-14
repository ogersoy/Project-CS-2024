# Project Modifications

**Author**: Yixin Huang
**Date**: 2024-10-14

## Summary of Modifications
The following components of the project were modified or enhanced to support the self-RAG functionality:

### 1. `Chatbot.py`
- **Purpose**: Modified to implement self-RAG for enhanced document retrieval and response generation.
- **Changes**:
  - Integrated the retrieval of relevant document chunks using `answer_question`.
  - Implemented GPT-2 to generate responses based on the retrieved document chunks.
  - Added detailed logging to track the process of retrieving document chunks and generating answers.
- **Key Functions**:
  - `ask_question`: Handles user queries, retrieves relevant document chunks using Sentence-BERT embeddings, and generates responses with GPT-2.
  - `generate_answer`: Generates coherent answers based on the context retrieved from the document chunks.

### 2. `utils.py`
- **Purpose**: Updated to support document chunk retrieval for self-RAG using Sentence-BERT and cosine similarity.
- **Changes**:
  - Refined the `find_most_relevant_chunk` function to identify the most relevant document chunk based on cosine similarity.
  - Added an optional relevance classification step (`classify_relevance`) using BERT to ensure that retrieved chunks are closely related to the query.
  - Adjusted the `answer_question` function to integrate the retrieval and classification logic for self-RAG.
- **Key Functions**:
  - `find_most_relevant_chunk`: Finds the most relevant document chunk based on cosine similarity of Sentence-BERT embeddings.
  - `classify_relevance`: Optionally classifies the relevance of a document chunk to the query.
  - `answer_question`: Handles the overall retrieval and response generation process, used by `Chatbot.py`.

### 3. `App.py`
- **Purpose**: Adjusted the application to process user queries using the newly integrated self-RAG mechanism.
- **Changes**:
  - Updated the `/ask` route to process questions with the self-RAG flow.
  - Kept the overall structure of the application, including logging and error handling, while ensuring self-RAG compatibility.

## How to Run

Follow the steps below to configure and run the project:

1. **Modify the `app.py` file**:
   - Locate and open the `app.py` file in the project directory.
   - **Line 11**: Replace the `HUGGINGFACE_TOKEN` with your own Hugging Face access token. Example code:
     ```python
     HUGGINGFACE_TOKEN = 'your_own_token_here'
     ```

   - **Line 24**: Replace the file path with your own Windows file address. Example code:
     ```python
     file_path = r'your_windows_file_path_here'
     ```

2. **Run the application**:
   - Open the terminal and navigate to the project directory.
   - Execute the following command to run the application:
     ```bash
     python app.py
     ```

   This will start the program based on your configuration.

---

Make sure to install all the necessary dependencies and set up your Python environment correctly before running the application.
