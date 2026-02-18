from fastapi import FastAPI
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(
    title="IA for Dummies Backend",
    description="Simulador de acciones del asistente IA for Dummies",
    version="2.0"
)


class BORRequest(BaseModel):
    eps_objetivo: List[str] = Field(default_factory=list)
    campos_formulario: List[str] = Field(default_factory=list)
    url_proveedor: Optional[str] = None
    region: str = "Colombia"


class StitchMockupRequest(BaseModel):
    eps_objetivo: List[str] = Field(default_factory=list)
    campos_formulario: List[str] = Field(default_factory=list)
    incluir_diagrama_mermaid: bool = True

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


@app.post("/bor-eps")
def generar_bor_eps(payload: BORRequest):
    eps = payload.eps_objetivo or ["EPS_A", "EPS_B"]
    campos = payload.campos_formulario or [
        "nombres",
        "apellidos",
        "fecha inicio incapacidad",
        "tiempo incapacidad",
        "EPS",
        "tipo de incapacidad",
        "diagnóstico",
        "recomendaciones"
    ]

    return {
        "resumen_ejecutivo": {
            "viabilidad": "Alta con enfoque API-first + RPA UI como respaldo.",
            "condiciones_criticas": [
                "Gobierno de datos sensibles y trazabilidad completa.",
                "Modelo operativo continuo para mantenimiento por cambios de portales.",
                "Gestión de excepciones con human-in-the-loop."
            ],
            "eps_objetivo": eps,
            "region": payload.region
        },
        "precedentes": [
            {
                "sector": "Salud",
                "hallazgo": "RPA en procesos de claims y backoffice reduce tiempos operativos cuando no hay APIs maduras.",
                "resultado_referencial": "Reducciones de ciclo de proceso entre 30% y 90% según madurez operativa."
            },
            {
                "sector": "Seguros",
                "hallazgo": "Automatización UI para captura y validación de formularios con evidencia de auditoría.",
                "resultado_referencial": "Menor backlog y mejora de cumplimiento de SLA."
            }
        ],
        "comparativa_modelos": {
            "modelo_ui_rpa": {
                "beneficios": [
                    "Funciona sin API del tercero.",
                    "Implementación rápida para pilotos por EPS."
                ],
                "riesgos": [
                    "Fragilidad ante cambios de interfaz.",
                    "Bloqueos por MFA/CAPTCHA.",
                    "Mayor costo de mantenimiento."
                ],
                "cumplimiento_salud": "Requiere minimización de datos, cifrado, acceso por roles y logs auditables."
            },
            "modelo_api": {
                "beneficios": [
                    "Mayor robustez y escalabilidad.",
                    "Mejor control de seguridad con tokens y scopes."
                ],
                "riesgos": [
                    "Dependencia de disponibilidad y cobertura de API por EPS.",
                    "Onboarding técnico y contractual más largo."
                ],
                "cumplimiento_salud": "Más alineado a privacy-by-design y trazabilidad transaccional."
            },
            "recomendacion": "Arquitectura híbrida: API-first y conectores UI-RPA por EPS sin API."
        },
        "complejidad_tecnica": {
            "nivel": "Alta",
            "factores": [
                "Variabilidad de formularios por EPS.",
                "Validaciones dinámicas y cambios frecuentes de UI.",
                "Autenticación variable (incluyendo MFA).",
                "Manejo de errores e idempotencia para evitar doble radicación."
            ]
        },
        "costos_implicitos": {
            "directos": [
                "Desarrollo de conectores por EPS.",
                "Licenciamiento/orquestación RPA.",
                "Infraestructura, vault y observabilidad."
            ],
            "indirectos": [
                "Mantenimiento evolutivo por cambios de portal.",
                "Soporte operativo y atención de excepciones.",
                "Cumplimiento normativo y auditorías."
            ]
        },
        "cronograma_referencial": {
            "piloto_2_eps": "8-14 semanas",
            "por_eps_adicional": "4-8 semanas",
            "fases": [
                "Precondiciones de seguridad/compliance",
                "Descubrimiento por EPS",
                "Construcción de conector y framework",
                "Testing/UAT",
                "Piloto productivo y estabilización"
            ]
        },
        "flujo_e2e": {
            "pasos": [
                "Ingreso de solicitud a cola",
                "Validación previa",
                "Obtención segura de credenciales desde vault",
                "Ejecución worker (login, formularios, adjuntos, envío)",
                "Persistencia y auditoría",
                "Notificación de resultado",
                "Gestión de excepciones",
                "Cierre y métricas"
            ],
            "campos_formulario": campos
        },
        "evaluacion_proveedor": {
            "url_proveedor": payload.url_proveedor,
            "criterios": [
                "Casos de éxito documentados en salud.",
                "Capacidad de operación con SLAs y runbooks.",
                "Prácticas de seguridad: vault, cifrado, segregación de accesos.",
                "Evidencia de mantenimiento continuo ante cambios UI."
            ]
        },
        "recomendaciones_finales": [
            "Iniciar con Sanitas y Compensar en piloto controlado.",
            "Diseñar con idempotencia, reintentos con backoff y DLQ.",
            "Mantener evidencia mínima auditable: radicado, timestamp, hash y respuesta del portal."
        ]
    }


@app.post("/stitch-blueprint-eps")
def generar_blueprint_stitch(payload: StitchMockupRequest):
    eps = payload.eps_objetivo or ["Sanitas", "Compensar"]
    campos = payload.campos_formulario or [
        "nombres",
        "apellidos",
        "fecha inicio incapacidad",
        "tiempo incapacidad",
        "EPS",
        "tipo de incapacidad",
        "diagnóstico",
        "recomendaciones"
    ]

    diagrama = """
flowchart LR
    A[Ingreso solicitud] --> B[Validación previa]
    B -->|OK| C[Vault credenciales]
    B -->|Business exception| G[Requiere intervención]
    C --> D[Worker EPS]
    D --> E[Persistencia y auditoría]
    D -->|System exception| H[Reintento/Escalación]
    E --> F[Notificación éxito]
    F --> I[Cierre y métricas]
    G --> I
    H --> I
""".strip()

    return {
        "objetivo": "Mockup en Stitch para demostrar viabilidad operativa de radicación automática en EPS.",
        "pantallas": [
            "Queue/Intake",
            "Pre-validation",
            "Credentials/Vault",
            "Worker Run",
            "Audit & Evidence",
            "Notifications",
            "Exceptions Center",
            "Metrics & Ops",
            "EPS Connector Config"
        ],
        "entradas": {
            "eps_objetivo": eps,
            "campos_formulario": campos
        },
        "conexiones_y_logica": {
            "triggers": ["Manual trigger", "Cola de mensajes", "Webhook"],
            "validaciones": [
                "Formato y tamaño de adjuntos",
                "Completitud de formulario",
                "Detección de duplicidad probable"
            ],
            "manejo_excepciones": {
                "business": "No reintentar automáticamente; asignar a operador.",
                "system": "Reintento con backoff (5m, 30m, 2h) y escalación a RPA engineer."
            }
        },
        "seguridad_y_conformidad": [
            "Pseudonimización del paciente (subject_ref).",
            "Credenciales solo desde vault, nunca en texto plano.",
            "Logging sin PII/PHI y trazabilidad por trace_id.",
            "Retención y custodia según políticas de datos sensibles en salud."
        ],
        "configuracion_stitch_recomendada": {
            "componentes": [
                "Sidebar + topbar",
                "Stepper de proceso",
                "Tabla de jobs",
                "Timeline de auditoría",
                "Tarjetas KPI"
            ],
            "conectores_reales_sugeridos": [
                "Queue (Pub/Sub o RabbitMQ)",
                "Vault (Secret Manager/Vault)",
                "Storage cifrado",
                "Base de auditoría"
            ],
            "rate_limiting": "Configurar límite por EPS y concurrencia por worker para evitar bloqueos de portal."
        },
        "diagrama_mermaid": diagrama if payload.incluir_diagrama_mermaid else None
    }
