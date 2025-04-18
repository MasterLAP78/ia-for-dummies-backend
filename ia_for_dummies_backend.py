from fastapi import FastAPI, Query
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="IA for Dummies Backend",
    description="Simulador de acciones del asistente IA for Dummies",
    version="2.0"
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
    return [{
        "titulo": f"Nueva tendencia en {tema}",
        "resumen": f"Resumen de cómo la IA está impactando {tema}.",
        "fuente": "El País Tecnología",
        "url": "https://elpais.com/tecnologia"
    } for _ in range(cantidad)]

@app.get("/linea-tiempo")
def consultar_linea_de_tiempo(formato: Optional[str] = "resumen", idioma: Optional[str] = "es"):
    eventos = [
        {"año": 1950, "hito": "Test de Turing", "descripcion": "Evaluación de IA por Alan Turing"},
        {"año": 2023, "hito": "Explosión de modelos generativos", "descripcion": "Popularización de ChatGPT, Bard y Claude"}
    ]
    return {"eventos": eventos if formato == "detallado" else eventos[:1]}

@app.get("/estadisticas-adopcion")
def consultar_estadisticas(sector: Optional[str] = "educación", fuente: Optional[str] = "Stanford", año: Optional[int] = 2024):
    return {
        "sector": sector,
        "adopcion_porcentaje": 74.3,
        "fuente": fuente,
        "año": año
    }

@app.get("/ia-radar")
def consultar_radar(sector: Optional[str] = "salud", region: Optional[str] = "Latinoamérica", año: Optional[int] = 2024, formato: Optional[str] = "resumen"):
    return {
        "sector": sector,
        "region": region,
        "avance": "Alto"
    }

@app.get("/ruta-aprendizaje")
def generar_ruta(nivel_usuario: str, perfil: str, objetivo: Optional[str] = None, idioma: Optional[str] = "es"):
    return {
        "temas": ["Fundamentos de IA", "Modelos Generativos", "Ética de la IA"],
        "recursos": ["https://coursera.org", "https://stanfordonline.ai"]
    }

@app.get("/riesgos-eticos")
def riesgos_eticos(caso_uso: str, tipo_impacto: Optional[str] = None, profundidad: Optional[str] = "básico"):
    return {
        "caso_uso": caso_uso,
        "riesgos": [
            "Sesgo algorítmico",
            "Falta de transparencia",
            "Violación de privacidad"
        ] if profundidad == "avanzado" else ["Sesgo algorítmico"]
    }

@app.get("/futuro-ia")
def simular_futuro(entorno: str, intensidad_adopcion: Optional[str] = "media", escenario: Optional[str] = "optimista"):
    return {
        "año_proyectado": 2030,
        "descripcion_escenario": f"En un escenario {escenario}, el entorno {entorno} se transforma gracias a la IA con adopción {intensidad_adopcion}."
    }

@app.get("/empleabilidad-ia")
def empleabilidad(profesion: str, nivel: Optional[str] = None, region: Optional[str] = None, fuente_datos: Optional[str] = "WEF"):
    return {
        "riesgo_automatizacion": 62.5,
        "habilidades_requeridas": ["Pensamiento computacional", "Análisis de datos", "Creatividad digital"],
        "demanda_futura": "Alta"
    }
