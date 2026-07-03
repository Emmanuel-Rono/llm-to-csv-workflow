
from data.QuiestionLoader import loadPromptsFromCsv
from src.config import load_model,load_output_path, load_prompt_path
from data.AskLLM import AskLLM
from data.WriteLLmResponseToCSV import WriteLLmResponseToCSV

def  run_workflow():  
     loader = loadPromptsFromCsv(load_prompt_path())
     prompt = loader.load_prompts()
     model =load_model()

    

     for prompts in prompt:

          askLLm = AskLLM(model,prompts)
          response = askLLm.sendRequesst()
          writer = WriteLLmResponseToCSV(response, load_output_path())
          print(f"Prompt: {prompts}")
          print(f"Response: {response}")
          if writer.writesResponsToCSV():
               print(f"Response written to {load_output_path()}")
          
   
          
if __name__ == "__main__":
    run_workflow()

     
