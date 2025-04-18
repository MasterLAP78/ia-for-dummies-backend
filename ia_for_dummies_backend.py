from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI(
    title="IA for Dummies API",
    description="Simulación de backend para pruebas de un GPT personalizado con acciones de IA.",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/noticias")
def buscar_noticias_ia(tema: str, idioma: Optional[str] = "es", cantidad: Optional[int] = 3):
    noticias = [
        {
            "titulo": f"Últimos avances en {tema} con IA",
            "resumen": f"Resumen breve sobre cómo la IA está impactando el área de {tema}.",
            "fuente": "AI News Today",
            "url": "https://ainews.today/noticia/123"
        }
        for _ in range(min(cantidad, 10))
    ]
    return noticias

@app.get("/linea-tiempo")
def consultar_linea_de_tiempo(formato: Optional[str] = "resumen", idioma: Optional[str] = "es"):
    eventos = [
        {"año": 1950, "hito": "Test de Turing", "descripcion": "Alan Turing propone un criterio para evaluar inteligencia artificial."},
        {"año": 1997, "hito": "Deep Blue vs Kasparov", "descripcion": "La IA vence por primera vez a un campeón mundial de ajedrez."},
        {"año": 2022, "hito": "Lanzamiento de ChatGPT", "descripcion": "Modelo generativo de OpenAI con capacidad conversacional avanzada."}
    ]
    return {"eventos": eventos if formato == "detallado" else eventos[:1]}
