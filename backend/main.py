from fastapi import FastAPI
from app.api.routes import inference, health

app = FastAPI(
    title="LLMGateway",
    description="A gateway for large language models (LLMs) that provides a unified API for various LLM providers.",
    version="0.1.0",
)

app.include_router(inference.router, prefix="/inference", tags=["Inference"])
app.include_router(health.router, prefix="/health", tags=["Health"])