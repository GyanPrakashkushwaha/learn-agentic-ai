from langchain_community.document_loaders.text import TextLoader

loader = TextLoader(
    file_path = r'document-loader\cricket.txt',
    encoding= 'utf-8',
    autodetect_encoding=True)

docs = loader.load()
print(docs)
print('==============================================')
print(docs[0])
print('==============================================')
print(docs[0].page_content)
print('--------------------------------------')
print(docs[0].metadata)