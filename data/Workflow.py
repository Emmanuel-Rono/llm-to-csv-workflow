
from data.QuiestionLoader import loadPromptsFromCsv
from src.config import load_model,load_output_path, load_prompt_path
from data.AskLLM import AskLLM
from data.WriteLLmResponseToCSV import WriteLLmResponseToCSV

def  run_workflow():  
     loader = loadPromptsFromCsv(load_prompt_path())
     prompt = loader.load_prompts()
     model =load_model()
     writer = WriteLLmResponseToCSV(load_output_path())


     for prompts in prompt:

          askLLm = AskLLM(model,prompts)
          response = askLLm.sendRequesst()
          print(f"Prompt: {prompts}")
          print(f"Response: {response}")
          writer.writesResponseToCSV(prompts,response)
          if writer.writesResponseToCSV(prompts, response):
               print(f"Response written to {load_output_path()}")
          
   
          
if __name__ == "__main__":
    run_workflow()

     
