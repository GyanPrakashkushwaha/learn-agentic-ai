from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# llm = HuggingFaceEndpoint(
#     repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task = "text-generation"
# ) 1


llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",  # let Hugging Face choose the best provider for you
)


model = ChatHuggingFace(llm = llm)
result = model.invoke('What is capital of india')
print(result.content)