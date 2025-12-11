from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='document-loader\\Social_Network_Ads.csv')

docs = loader.load()

print(type(docs))
print(type(docs[1]))