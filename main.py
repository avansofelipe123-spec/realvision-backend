
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI(
    title="RealVision AI",
    description="API oficial do RealVision AI",
    version="1.0.1"
)

# Permitir comunicação com o aplicativo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    prompt: str = Field(min_length=5, max_length=1000)
    duration: Literal[10, 30, 60] = 60
    quality: Literal["720p", "1080p"] = "1080p"
    style: Literal[
        "realista",
        "cinematografico",
        "documentario",
        "natureza"
    ] = "realista"


@app.get("/")
def home():
    return {
        "app": "RealVision AI",
        "status": "online",
        "version": "1.0.1"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/generate")
def generate_video(request: VideoRequest):
    return {
        "status": "waiting_for_engine",
        "message": "Solicitação recebida. Motor de vídeo ainda não conectado.",
        "prompt": request.prompt,
        "duration": request.duration,
        "quality": request.quality,
        "style": request.style
    }
