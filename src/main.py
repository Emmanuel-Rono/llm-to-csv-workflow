from google import genai
from config import load_api


api_key = load_api()

client = genai.Client()

response  = client.interactions.create(
    model="gemini-3.5-flash",
    input = "Hello, are you set ?"

)

print(response.output_text)


