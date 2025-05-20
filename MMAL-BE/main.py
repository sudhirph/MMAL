import os
from fastapi import FastAPI
from app.schemas.llm_request import LLMRequest
from app.core.llm_facade import LLMFacade
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from app.core.model_registry import ModelRegistry



load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5000",],  # or ["http://localhost:3000"] for stricter control
    allow_credentials=True,
    allow_methods=["*"],  # Needed to support OPTIONS, POST, GET etc.
    allow_headers=["*"],  # Needed for Content-Type, Authorization etc.
)

@app.post("/api/generate")
async def generate_text(request: LLMRequest):
    return await LLMFacade.generate(request)




@app.get("/api/models/{provider}")
def get_models(provider: str):
    try:
        return {"models": ModelRegistry.list_models(provider)}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid provider")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
