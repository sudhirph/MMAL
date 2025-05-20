from app.schemas.llm_request import LLMRequest

class RoutingStrategy:
    @staticmethod
    def select_provider(request: LLMRequest) -> str:
        # Simplified: could route based on cost/latency/etc.
        return request.provider
