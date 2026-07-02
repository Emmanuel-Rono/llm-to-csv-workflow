from pathlib import Path
import os
from dotenv import load_dotenv

def load_api() -> str:
     env_path = Path(__file__).resolve().parent.parent / ".env"
     load_dotenv(env_path)
     api_key = os.getenv("gemini_API_KEY")
     if not api_key:
          raise ValueError("Check api key if present")
     
     return api_key

def load_prompts() -> str:
     env_path = Path(__file__).resolve().parent.parent / ".env"
     load_dotenv(env_path)
     promptPath = os.getenv("CSV_INPUT_PATH", "data/prompts.csv")
     if not [promptPath]:
          raise ValueError("Check csv input path if present")
     
     return promptPath

def load_output_path() -> str:
     env_path = Path(__file__).resolve().parent.parent / ".env"
     load_dotenv(env_path)
     outputPath = os.getenv("CSV_OUTPUT_PATH", "data/llmResponses.csv")
     if not [outputPath]:
          raise ValueError("Check csv output path if present")
     
     return outputPath

def load_model() -> str:
     env_path = Path(__file__).resolve().parent.parent / ".env"
     load_dotenv(env_path)
     model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")
     if not [model]:
          raise ValueError("Check model if present")
     
     return model