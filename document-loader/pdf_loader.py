from langchain_community.document_loaders.pdf import PyPDFLoader

loader = PyPDFLoader(
    file_path= "document-loader\\dl-curriculum.pdf"
)

docs = loader.load()
print(docs)