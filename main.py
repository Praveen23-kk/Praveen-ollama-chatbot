from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

template="""
Answer the question below.

Here is the converstion history:{context}

Question:{question}

Answer:

"""



model=Ollama(model="llama3.2:1b")
prompt=ChatPromptTemplate.from_template(template)
chain=prompt | model

def handel_conversation():
    context=""
    print("Welcome  to Praveen's AI chat BOT! type'exit' to to leave")
    while True:
        user_input=input("You: ")
        if user_input.lower() =="exit":
            break
        
        result=chain.invoke({"context":context, "question":user_input})
        print("Bot:",result)
        context==f"\nUser:{user_input}\nAI:{result}"
        
if __name__=="__main__":
    handel_conversation()        
    



