
from data.QuiestionLoader import loadPromptsFromCsv
from src.config import load_model,load_output_path, load_prompt_path
from data.AskLLM import AskLLM
from data.WriteLLmResponseToCSV import WriteLLmResponseToCSV
from data.llmResponseValidator import validateResponse
import json


def  run_workflow():  
     loader = loadPromptsFromCsv(load_prompt_path())
     prompt = loader.load_prompts()
     model =load_model()
     writer = WriteLLmResponseToCSV(load_output_path())


     for prompts in prompt:

          askLLm = AskLLM(model,prompts)
          responseFromLlm = askLLm.sendRequesst()
          print("RAW RESPONSE:")
          print(responseFromLlm)
           #Pass it to json validator
          #raw_json = coerce_to_dict(responseFromLlm)
          #validated_response = validateResponse(raw_json)
        
          if responseFromLlm:
               writer.writesResponseToCSV(prompts, responseFromLlm)
               print(f"Response written to {load_output_path()}")
          


def coerce_to_dict(response_text):
    if isinstance(response_text, dict):
        return response_text

    if isinstance(response_text, str):
        text = response_text.strip()

        if text.startswith("```"):
            text = text.strip("`")
            if text.lower().startswith("json"):
                text = text[4:].strip()

        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return None

    return None
          

if __name__ == "__main__":
    run_workflow()

     
