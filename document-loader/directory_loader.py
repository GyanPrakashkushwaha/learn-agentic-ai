from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='document-loader\\books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()
# print(docs)
# for document in docs:
#     print(document.metadata)
print(next(docs))