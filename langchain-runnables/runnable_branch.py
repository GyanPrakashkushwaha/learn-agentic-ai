

# topic-> prompt-> llm -> parse -> >500 words
                              # -> <= 500 words

# generate a detailed report on {topic}

# template,llm , parser, chain, runnable
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnableLambda, RunnablePassthrough
load_dotenv()


def word_count(txt):
    return len(txt.split(' '))

prompt1 = PromptTemplate(
    template = "Generate a detailed report on {topic}",
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = "summarize the following text within 100 words \n {text}",
    input_variables = ['text']
)

llm = ChatGoogleGenerativeAI(model = 'models/gemini-2.0-flash')

parser = StrOutputParser()

report_chain = RunnableSequence(prompt1, llm, parser)

choice_chain = RunnableBranch(
    (lambda x: len(x.split()) > 100, RunnableSequence(RunnableLambda(lambda txt: {"text": txt}), prompt2, llm, parser)),
    (RunnablePassthrough())
)

chain = RunnableSequence(report_chain, choice_chain)
res = chain.invoke({"topic": 'ai'})

print(res)




