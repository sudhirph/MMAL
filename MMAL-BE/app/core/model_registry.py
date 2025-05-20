import os
import openai
import requests

class ModelRegistry:
    @staticmethod
    def list_models(provider: str):
        if provider == "openai":
            return ModelRegistry._openai_models()

        elif provider == "ollama":
            return ModelRegistry._llama_models()

        elif provider == "anthropic":
            return ModelRegistry._anthropic_models()

        elif provider == "gemini":
            return ModelRegistry._gemini_models()

        raise ValueError("Unsupported provider")


    @staticmethod
    def _openai_models():
        return [
            "gpt-4o",
            "gpt-4",
            "gpt-4-0613",
            "gpt-4-32k",
            "gpt-4-32k-0613",
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-0125",
            "gpt-3.5-turbo-1106",
            "gpt-3.5-turbo-0613",
            "gpt-3.5-turbo-16k",
            "gpt-3.5-turbo-16k-0613",
            "text-davinci-003",
            "text-davinci-002",
            "text-curie-001",
            "text-babbage-001",
            "text-ada-001",
            "davinci",
            "curie",
            "babbage",
            "ada",
            "babbage-002",
            "davinci-002",
            "code-davinci-002",
            "code-cushman-001",
            "text-embedding-3-small",
            "text-embedding-3-large",
            "text-embedding-ada-002",
            "text-moderation-latest",
            "text-moderation-stable",
            "whisper-1"
        ]
        
    @staticmethod
    def _llama_models():
        return [
            "llama3",
            "llama2",
            "mistral",
            "mixtral",
            "gemma",
            "codellama",
            "dolphin-mistral",
            "orca-mini",
            "tinyllama",
            "phi",
            "llava",
            "neural-chat",
            "qwen",
            "deepseek-coder",
            "starcoder",
            "wizardcoder",
            "mistral-openorca",
            "nous-hermes2",
            "falcon",
            "zephyr",
            "openchat",
            "yi",
            "command-r",
            "stablelm-zephyr"
        ]

    @staticmethod
    def _anthropic_models():
        return [
            "claude-3-haiku-20240307",
            "claude-3-sonnet-20240229",
            "claude-3-opus-20240229"
        ]

    @staticmethod
    def _gemini_models():
        return [
            "gemini-pro",
            "gemini-1.5-pro",
            "gemini-1.5-flash"
        ]
