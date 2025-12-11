from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.graph.messasges import add_messages
from langgraph.graph import START, END, StateGraph
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()


llm = ChatGoogleGenerativeAI(model = "models/gemini-2.5-flash-lite")

class BotMemory(TypedDict):
    messages: Annotated[list[str], add_messages]
    
def my_bot(state: BotMemory):
    res = llm.invoke(state['messages'])
    return {"messages": [res.content]}

graph = StateGraph(BotMemory)

graph.add_node("bot", my_bot)
graph.add_edge(START, "bot")
graph.add_edge('bot', END)

# checkpointer
check_point = InMemorySaver()
workflow = graph.compile(checkpointer=check_point)

