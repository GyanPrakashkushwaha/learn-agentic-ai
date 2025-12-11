from langchain_core.runnables import RunnableParallel, RunnableLambda,  RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser



retriever = vector_store.as_retriever(search_type = 'mmr', search_kwargs={"k": 3, "lambda_mult": 0.5})

def myfunc(doc):
    return "\n\n".join(content.page_content for content in doc)

retriever_chain = retriever | RunnableLambda(myfunc)

augmentation_chain = RunnableParallel({
    "query": RunnablePassthrough(),
    "context": retriever_chain
})

model_chain = augmentation_chain | model | StrOutputParser()