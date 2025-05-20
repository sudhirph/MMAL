import anthropic
from app.schemas.llm_request import LLMRequest

class AnthropicProvider:
    async def generate(self, request: LLMRequest) -> str:
        client = anthropic.Anthropic()
        response = client.messages.create(
            model=request.model,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
            messages=[{"role": "user", "content": request.prompt}]
        )
        return response.content[0].text
