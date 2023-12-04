import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

load_dotenv(find_dotenv())

client = OpenAI(api_key=os.getenv("GPT_KEY"))

prompt = "hello"

response = client.completions.create(model="text-davinci-002", prompt=prompt, max_tokens=100)

answer = response["choices"][0]["text"].strip()
print(answer)
