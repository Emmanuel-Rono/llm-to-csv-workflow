
from  data.QuiestionLoader import loadPromptsFromCsv
from src.config import load_model, load_prompts, load_output_path
from data.AskLLM import AskLLM
from data.WriteLLmResponseToCSV import WriteLLmResponseToCSV
from data.WriteLLmResponseToCSV import writeResponsToCSV

def  run_workflow():  
     loader = loadPromptsFromCsv(load_prompts())
     prompts = loader.load_prompts()

     model =load_model()
     prompt = load_prompts()
     askLLm = AskLLM(model,prompt)

     for prompt in prompts:
          response = askLLm.sendRequesst()
          WriteLLmResponseToCSV.writeResponsToCSV(response,load_output_path())

          
if __name__ == "__main__":
    run_workflow()

     
