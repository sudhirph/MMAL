import os
from openai import OpenAI
from app.schemas.llm_request import LLMRequest

class OpenAIProvider:
    async def generate(self, request: LLMRequest) -> str:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        messages = [{"role": "user", "content": request.prompt}]
        if request.system_prompt:
            messages.insert(0, {"role": "system", "content": request.system_prompt})
        response = client.chat.completions.create(
            model=request.model,
            messages=messages,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        return response.choices[0].message.content
