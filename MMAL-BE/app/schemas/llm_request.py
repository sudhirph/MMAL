from pydantic import BaseModel
from typing import Optional, List

class LLMRequest(BaseModel):
    provider: str
    model: str
    prompt: str
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 512
    system_prompt: Optional[str] = None
    tools: Optional[List[dict]] = None



