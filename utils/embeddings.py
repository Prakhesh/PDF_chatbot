from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from utils.chunking import docs


embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-V2")

vectorstore = FAISS.from_documents(docs,embeddings)
