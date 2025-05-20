from app.core.llm_registry import LLMRegistry
from app.strategies.routing_strategy import RoutingStrategy
from app.decorators.quota_tracker import track_usage
from app.schemas.llm_request import LLMRequest

class LLMFacade:
    @staticmethod
    @track_usage
    async def generate(request: LLMRequest) -> dict:
        provider_name = RoutingStrategy.select_provider(request)
        provider = LLMRegistry.get(provider_name)
        result = await provider.generate(request)
        return {"output": result}
