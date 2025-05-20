from app.adapters.openai_adapter import OpenAIProvider
from app.adapters.anthropic_adapter import AnthropicProvider
from app.adapters.gemini_provider import GeminiProvider
from app.adapters.ollama_provider import OllamaProvider

class LLMRegistry:
    providers = {
        "openai": OpenAIProvider(),
        "anthropic": AnthropicProvider(),
        "gemini": GeminiProvider(),
        "ollama": OllamaProvider()
    }

    @staticmethod
    def get(name: str):
        if name not in LLMRegistry.providers:
            raise ValueError(f"Unsupported provider: {name}")
        return LLMRegistry.providers[name]
