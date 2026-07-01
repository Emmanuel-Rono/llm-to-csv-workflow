from openai import OpenAI

from config import load_api

api_key = load_api()
client = OpenAI(api_key = api_key)

response  = client.responses.create(
    model="gpt-5.5",
    input = "Hello, are you set ?"

)

print(response.text)



