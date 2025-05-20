import requests
from app.schemas.llm_request import LLMRequest

class OllamaProvider:
    async def generate(self, request: LLMRequest) -> str:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": request.model,
                "prompt": request.prompt,
                "options": {
                    "temperature": request.temperature
                },
                "stream": False
            }
        )
        result = response.json()
        return result.get("response", "").strip()
