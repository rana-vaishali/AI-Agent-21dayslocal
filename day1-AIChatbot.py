from openai import OpenAI
from dotenv import load_dotenv
import os

#load env
load_dotenv()

#client to connect with ollama
client = OpenAI(
    base_url= os.getenv("BASE_URL"),
    api_key= os.getenv("API_KEY")
)

#send a question to AI model
response = client.chat.completions.create(
    model = os.getenv("MODEL"),
    messages = [
        {
            "role": "user",
            "content": "what is artificial intelligence?"
        }
    ]
)

#display the response
print(response.choices[0].message.content)