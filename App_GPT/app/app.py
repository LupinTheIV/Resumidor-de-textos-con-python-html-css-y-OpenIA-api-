import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role":"system","content":"Eres un "},
        {"role":"user","content":"Instruccion"}
    ]
)

responces = response.choices[0].message["content"]
print(responces)
client.close()