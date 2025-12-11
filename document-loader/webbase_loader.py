from langchain_community.document_loaders.web_base import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda, RunnableSequence, RunnablePassthrough

load_dotenv()

url = "https://www.flipkart.com/proelite-flip-cover-motorola-pad-60-neo-11-inch-cover-smart-case-translucent-back-stylus-pen/p/itm9636f9d3f2b4a"
loader = WebBaseLoader(
    web_path= url
)

doc = loader.load()

prompt = PromptTemplate(
    template = "Answer the question \n {question} \n from the text \n {text}",
    input_variables = ['question', 'text']
)

model = ChatGoogleGenerativeAI(model = 'models/gemini-2.0-flash')

parser = StrOutputParser()

chain = prompt | model | parser

res = chain.invoke({
    "question": "what's the price and rating of the backcover",
    "text": doc[0].page_content
})

print(res)
# print(doc)