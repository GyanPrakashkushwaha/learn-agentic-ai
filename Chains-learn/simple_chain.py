from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template = 'Generate 5 Intersting facts ablout {topic}',
    input_variables = ['topic']
)

model = ChatGoogleGenerativeAI(model='models/gemini-2.0-flash')
parser = StrOutputParser()

chain = prompt | model | parser

res = chain.invoke({'topic': 'Cricket'})
print(res)
