
from urllib import response

from src.config import load_api
from google import genai


class AskLLM:
    def __init__(self,model,prompt):
        self.model = model
        self.prompt = prompt
    
    def sendRequesst(self):
        client = genai.client()
        response = client.interactions.create(

            model =self.model,
            input = self.prompt
        )
        return response.output_text