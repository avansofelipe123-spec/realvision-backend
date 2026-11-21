
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI(
    title="RealVision AI",
    description="API oficial do RealVision AI",
    version="1.1.0"
)

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

    # Configuração de áudio
    audio_mode: Literal["all"] = "all"

    # Configuração de voz
    voice_selection: Literal["choose"] = "choose"

    voice_gender: Literal[
        "masculina",
        "feminina"
    ] = "masculina"

    language: Literal[
        "pt-BR",
        "pt-PT",
        "en",
        "de"
    ] = "pt-BR"

    accent: Literal[
        "brasileiro",
        "portugal",
        "americano",
        "britanico",
        "alema"
    ] = "brasileiro"


@app.get("/")
def home():
    return {
        "app": "RealVision AI",
        "status": "online",
        "version": "1.1.0"
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
        "message": (
            "Solicitação recebida. "
            "Motor de geração de vídeo e áudio ainda não conectado."
        ),

        "prompt": request.prompt,
        "duration": request.duration,
        "quality": request.quality,
        "style": request.style,

        "audio": {
            "mode": request.audio_mode
        },

        "voice": {
            "selection": request.voice_selection,
            "gender": request.voice_gender,
            "language": request.language,
            "accent": request.accent
        }
    }
