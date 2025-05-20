import google.generativeai as genai
from app.schemas.llm_request import LLMRequest
import os

class GeminiProvider:
    def __init__(self):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    async def generate(self, request: LLMRequest) -> str:
        model = genai.GenerativeModel(request.model or "gemini-pro")
        chat = model.start_chat(history=[])

        response = chat.send_message(
            request.prompt,
            generation_config={
                "temperature": request.temperature,
                "max_output_tokens": request.max_tokens
            }
        )
        return response.text
