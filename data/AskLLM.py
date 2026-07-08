
from src.config import load_api
from google import genai
from src.config import load_api
from google import genai
from google.genai import types


class AskLLM:
    def __init__(self,model,prompt):
        self.model = model
        self.prompt = prompt
    
    def sendRequesst(self):

        client = genai.Client(api_key=load_api())

        try:
            response = client.interactions.create(
                model =self.model,
                input = self.prompt,
                response_format ={
                    "type": "text",
                    "mime_type": "application/json",
                    "schema": TicketClassification.model_json_schema(),
                    },
            )
            return response.output_text
        
        except Exception as e:
            return f"[LLM error: {e}]"


class AskLLM:
    def __init__(self,model,prompt):
        self.model = model
        self.prompt = prompt
    
    def sendRequesst(self):

        client = genai.Client(api_key=load_api())
        try:
            response = client.interactions.create(
                model =self.model,
                input = self.prompt,
                response_format ={
                    "type": "text",
                    "mime_type": "application/json",
                    # "schema": TicketClassification.model_json_schema(),
                    },
            )
            return response.output_text
        
        except Exception as e:
            return f"[LLM error: {e}]"