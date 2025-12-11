from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate a detailed report for the {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate 5 Intersting facts ablout {topic}',
    input_variables = ['topic']
)

model = ChatGoogleGenerativeAI(model='models/gemini-2.0-flash')
parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser
res = chain.invoke({'topic': 'Cricket'})
print(res)
chain.get_graph().print_ascii()