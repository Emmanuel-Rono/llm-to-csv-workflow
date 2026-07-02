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
