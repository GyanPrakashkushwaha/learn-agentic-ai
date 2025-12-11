from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='models/gemini-2.0-flash', temperature = 1.9)
result = model.invoke("tell me 10 indian funny name")
print(result.content)