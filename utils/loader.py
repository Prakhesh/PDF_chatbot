from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
directory_path = "data/"
loader = DirectoryLoader(directory_path, glob="*.pdf", loader_cls=PyPDFLoader, silent_errors=True)
documents = loader.load()

