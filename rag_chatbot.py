import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from wxai_langchain import LangChainInterface

# Load and split document
def load_and_split_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter()
    chunks = splitter.split_documents(documents)
    return chunks

# Create a vector store and QA chain
def create_retrieval_qa_chain(chunks):
    embeddings = HuggingFaceEmbeddings()
    index_creator = VectorstoreIndexCreator(embeddings=embeddings)
    index = index_creator.create_index(chunks)
    chain = RetrievalQA(index=index, retriever=index_creator.get_retriever())
    return chain

# Define Streamlit interface
def main():
    st.title("Chatbot Interface")
    
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    
    if uploaded_file:
        st.write("Processing your document...")
        chunks = load_and_split_pdf(uploaded_file)
        chain = create_retrieval_qa_chain(chunks)
        
        question = st.text_input("Ask a question:")
        if question:
            answer = chain.run(question)
            st.write("Answer:", answer)

if __name__ == "__main__":
    main()
