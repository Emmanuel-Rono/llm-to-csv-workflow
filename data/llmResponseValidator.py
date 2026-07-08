from typing import List
import json

from pydantic import BaseModel,Field

class llmResponseValidator(BaseModel):
    
    engagement_id: str = Field(
        ...,
        pattern =r"TW-2026-Q2-\d{4}",
        description = "Engagement ID must follow the format TW-2026-Q2-XXXX",
        min_length=15,
        max_length=20
    )

    project_name : str = "NORTHGATE"
    summary : str
    action_taken : str
    compliance_checks : List[str] 



#Validate Logic
def validateResponse(raw_json):
    if isinstance(raw_json, str):
        try:
            raw_json = json.loads(raw_json)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e}")

    if not isinstance(raw_json, dict):
        raise TypeError("Expected a JSON object/dict")

    try:
        return llmResponseValidator.model_validate(raw_json)
    except Exception as e:
        print(f"Error validating response: {e}")
        return None