from typing import List

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
def validateResponse(raw_json:dict):

    try:
        response = llmResponseValidator.model_validate(raw_json)
        return response
    
    except Exception as e:
        print(f"Error validating response: {e}")