from transformers import AlbertTokenizer, AlbertModel
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline

# 1. Tokenization
tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')

# 2. Text splitting
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
)
chunks = text_splitter.split_text(your_cleaned_text)

# 3. Embedding generation
embeddings = HuggingFaceEmbeddings(model_name="albert-base-v2")

# 4. Vector store creation
vectorstore = Chroma.from_texts(chunks, embeddings)

# 5. Retriever setup
retriever = vectorstore.as_retriever()

# 6. LLM setup
model = AlbertModel.from_pretrained('albert-base-v2')
llm = HuggingFacePipeline.from_model_id(
    model_id="albert-base-v2",
    task="text-generation",
    model_kwargs={"temperature": 0.7, "max_length": 64},
)

# 7. Chain creation
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
)

# Example usage
query = "Your question here"
response = qa_chain.run(query)
print(response)