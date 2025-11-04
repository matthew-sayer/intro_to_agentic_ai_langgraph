from langchain_ollama import ChatOllama

model_name = "tinyllama:latest" #Replace with the model of your choice (as above in the pull)

llm = ChatOllama(model=model_name, temperature=0.5)

print(f"Initialised {model_name}.")