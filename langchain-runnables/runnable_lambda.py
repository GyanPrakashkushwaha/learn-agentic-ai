from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda, RunnableSequence, RunnablePassthrough

load_dotenv()

prompt = PromptTemplate(
    template = 'write a joke about {topic}',
    input_variables = ['topic']
)

model = ChatGoogleGenerativeAI(model = 'models/gemini-2.0-flash')
parser = StrOutputParser()

def word_count(text):
    return len(text.split())

prompt2 = PromptTemplate(
    template = 'write the detailed explanation about the joke {topic}',
    input_variables = ['topic']
)

joke_gen_chain = RunnableSequence(prompt, model, parser)
explain_chain = RunnableSequence(
    RunnableLambda(lambda joke: {"joke": joke}),
    prompt2,
    model,
    parser
)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'lenght': RunnableLambda(word_count),
    # 'explanation': explain_chain
})

chain = RunnableSequence(joke_gen_chain, parallel_chain)
res = chain.invoke({'topic': 'AI'})
print(res)