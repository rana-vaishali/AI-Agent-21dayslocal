from openai import OpenAI
from dotenv import load_dotenv
import os

#load env
load_dotenv()

#client to connect with ollama
client= OpenAI(
    base_url= os.getenv("BASE_URL"),
    api_key= os.getenv("API_KEY")
)

# welcome message
print("="*40)
print("AI Assistant")
print("="*40)

#continuous looping to prompt user for input and keep the conversation going
while True:
    user_input = input("\n You: ")
    if user_input.lower() == "quit":
        print("\n AI Assistant:  Goodbye! Have a great day.")
        break
    
    response = client.chat.completions.create(
        model = os.getenv("MODEL"),
        messages= [
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    print("\n AI Assistant: ",response.choices[0].message.content)