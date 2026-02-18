# Mockup de Plataforma Centro de Oportunidades Digitales (COD)

Este mockup describe la experiencia clave del MVP del Centro de Oportunidades Digitales, alineado con los objetivos y requerimientos del documento funcional. Los diagramas se presentan en formato de wireframe de baja fidelidad para comunicar la estructura, jerarquía de contenido y flujos principales.

---

## Identidad Visual y Sistemas Transversales

| Elemento | Propuesta |
| --- | --- |
| **Paleta de color** | Azul petróleo `#003C57` (navegación), Verde menta `#3BB273` (llamados a la acción), Amarillo suave `#F8C045` (alertas positivas), Gris claro `#F4F7F9` (fondos), Gris oscuro `#44505A` (texto). |
| **Tipografía** | Titulares: "Poppins" Bold 600; Cuerpo: "Roboto" Regular 400; Etiquetas y microtexto: "Roboto" Medium 500. |
| **Iconografía** | Línea simple, esquinas redondeadas. Íconos de diagnóstico, marketplace, mentoría y financiación como elementos de la narrativa COD. |
| **Componentes reutilizables** | Tarjetas modulares (diagnóstico, herramientas, tickets), barra lateral colapsable, badges de progreso, "chips" para filtros, timeline vertical para planes de 90 días. |
| **Soporte de accesibilidad** | Contrastes AA (azul/verde vs fondo claro), botones con texto + ícono, descripciones aria para elementos clave, navegación por teclado con foco visible. |

---

## Estructura General de Navegación

```
┌─────────────── Navbar superior ───────────────┐
│ Logo COD │ Marketplace │ Formación │ Mentoría │ Donaciones │ Perfil ▼ │
└───────────────────────────────────────────────┘
┌─ Sidebar (colapsable) ─┐ ┌─────────────── Panel principal ────────────────┐
│ Dashboard             │ │ Contenido según sección seleccionada           │
│ Diagnóstico 360°      │ │                                                 │
│ Plan 90 días          │ │                                                 │
│ Mi comunidad          │ │                                                 │
│ Reportes e Impacto    │ │                                                 │
└───────────────────────┘ └─────────────────────────────────────────────────┘
```

La navegación global está siempre disponible, mientras que la barra lateral cambia según el rol (emprendedor, mentor, administrador) ocultando opciones irrelevantes.

---

## Pantallas Principales

### 1. Landing de Valor Inmediato (Visitante)

```
┌───────────────────────────────────────────────────────────────────────┐
│ Banner hero: "Diagnostica tu micronegocio en 5 minutos" [CTA: Empezar] │
├───────────────────────────────────────────────────────────────────────┤
│ Paso 1 │ Paso 2 │ Paso 3     │ Testimonios (carrusel)                  │
│ Icono  │ Icono  │ Icono      │                                         │
├───────────────────────────────────────────────────────────────────────┤
│ Starter Pack Destacado                                                │
│ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐                  │
│ │ Herramienta   │ │ Micro-curso   │ │ Mentoría      │                  │
│ │ recomendada   │ │ sugerido      │ │ introductoria │                  │
│ └───────────────┘ └───────────────┘ └───────────────┘                  │
├───────────────────────────────────────────────────────────────────────┤
│ Sección "Ecosistema" con logos de aliados y CTA para donantes         │
└───────────────────────────────────────────────────────────────────────┘
```

Elementos clave:
- CTA primario lleva al diagnóstico corto sin registro.
- CTA secundario: "Soy aliado / Quiero donar".
- Información resumida de beneficios diferenciados para visitantes, usuarios registrados y miembros MD.

### 2. Flujo de Diagnóstico Corto

```
┌──────────────────────────────┐
│ Barra de progreso 60%        │
├──────────────────────────────┤
│ Pregunta 3 de 5              │
│ "¿Cómo registras tus ventas?"│
│ ( ) En libreta               │
│ ( ) En Excel                 │
│ ( ) En aplicación móvil      │
│ ( ) No llevo registro        │
├──────────────────────────────┤
│ Botón Volver  │ Botón Siguiente (CTA verde) │ "Guardar y continuar luego" │
└──────────────────────────────┘
```

Al finalizar se muestra un modal con resumen y CTA para guardar resultados creando una cuenta (registro ligero: teléfono o correo + contraseña).

### 3. Dashboard "Mi progreso" (Usuario Registrado)

```
┌─────────────────────── Header con saludo y badges ──────────────────────┐
│ Hola, Andrea │ Badge: Diagnóstico Básico ✔ │ Recordatorio: 2 tareas     │
├────────────────────────────────────────────────────────────────────────┤
│ Métricas principales (tarjetas)                                        │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐                     │
│ │ Score    │ │ Plan 90d │ │ Cursos   │ │ Tickets  │                     │
│ │ 62/100   │ │ 30%      │ │ 1/3      │ │ 1 activo │                     │
│ └──────────┘ └──────────┘ └──────────┘ └──────────┘                     │
├────────────────────────────────────────────────────────────────────────┤
│ Plan de 90 días (timeline)                                            │
│ Semana 1 ────● Crear catálogo digital  ── [Check]                      │
│ Semana 2 ────○ Configurar pagos digitales ── [CTA ver guía]            │
│ Semana 3 ────○ Publicar promoción en redes ── [Agregar evidencia]      │
├────────────────────────────────────────────────────────────────────────┤
│ Recomendaciones personalizadas                                        │
│ Tarjeta herramienta + Tarjeta curso + Tarjeta mentor sugerido          │
├────────────────────────────────────────────────────────────────────────┤
│ Zona de comunidad (micro foro + próximos eventos)                      │
└────────────────────────────────────────────────────────────────────────┘
```

### 4. Diagnóstico 360° (Desktop)

```
┌────────── Tabs temáticos ──────────┐
│ [Finanzas] [Marketing] [Operaciones] [Formalización] [Talento]         │
└────────────────────────────────────┘
┌───────────────────────────────────────────────────────────────────────┐
│ Puntuación general: 58/100  │ Semáforo: Amarillo                       │
├───────────────────────────────────────────────────────────────────────┤
│ Radar de capacidades (gráfico)                                         │
├───────────────────────────────────────────────────────────────────────┤
│ Lista priorizada de brechas                                            │
│ 1. Formalización pendiente → CTA "Agendar mentoría legal"              │
│ 2. Baja adopción de herramientas digitales → CTA "Ver herramientas"    │
└───────────────────────────────────────────────────────────────────────┘
```

Incluye botón "Actualizar diagnóstico" y capacidad de descargar PDF.

### 5. Marketplace de Soluciones

```
┌──── Filtros ────┐
│ Categoría ▼     │ Sector ▼ │ Ubicación ▼ │ Precio ▼ │ Chips activos     │
└─────────────────┘
┌───────────────────────────────────────────────────────────────────────┐
│ Tarjeta herramienta                                                    │
│ ┌─────────────────────────────────────────────────────────┐            │
│ │ Logo proveedor │ Puntuación usuarios ★★★★☆ │ Beneficio COD          │
│ │ Nombre herramienta                               │ Gratuita          │
│ │ Descripción breve (2 líneas)                                         │
│ │ Botones: [Saber más] [Agregar a mi plan] [Contactar aliado]          │
│ └─────────────────────────────────────────────────────────┘            │
├───────────────────────────────────────────────────────────────────────┤
│ Tarjeta curso (cuando filtro = Formación)                              │
└───────────────────────────────────────────────────────────────────────┘
```

A la derecha (desktop) o en un bottom sheet (mobile) se muestra un resumen del perfil del negocio para contextualizar las recomendaciones.

### 6. Módulo de Mentoría

```
┌─────────────── Buscador de mentores ────────────────┐
│ Filtros: Área experta, Sector, Disponibilidad        │
├──────────────────────────────────────────────────────┤
│ Lista de mentores (cards)                            │
│ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐    │
│ │ Foto         │ │ Foto         │ │ Foto         │    │
│ │ Nombre       │ │ Nombre       │ │ Nombre       │    │
│ │ Habilidades  │ │ Habilidades  │ │ Habilidades  │    │
│ │ CTA: Solicitar│ │ CTA: Solicitar│ │ CTA: Solicitar│ │
│ └──────────────┘ └──────────────┘ └──────────────┘    │
├──────────────────────────────────────────────────────┤
│ Panel de sesión activa                               │
│ Próxima reunión: 12 mayo 4:00 p.m. [Agregar al calendario]            │
│ Registro de acuerdos (textarea + botón guardar)                       │
└──────────────────────────────────────────────────────┘
```

Mensajería interna se ubica en un panel lateral tipo chat para mantener la comunicación en contexto.

### 7. Donaciones por Tickets

```
┌───────────────────────────── Tabs ─────────────────────────────┐
│ [Apoyar un caso] [Fondo común] [Historial]                     │
└────────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────────┐
│ Tarjeta ticket individual                                      │
│ ┌─────────────────────────────────────────────────────────┐    │
│ │ Foto del negocio │ "Ticket: Kit de formalización"       │    │
│ │ Monto: $150.000  │ Barra de progreso 60%                 │    │
│ │ Impacto esperado │ Botón: "Donar ahora" (verde)         │    │
│ └─────────────────────────────────────────────────────────┘    │
├────────────────────────────────────────────────────────────────┤
│ Modal post-donación: resumen, agradecimiento, CTA "Seguir caso"│
└────────────────────────────────────────────────────────────────┘
```

Los donantes registrados acceden a un dashboard con métricas de impacto (tickets financiados, evidencias, historias).

---

## Flujos de Usuario Clave

1. **Visitante → Diagnóstico → Registro → Dashboard**
   - Landing (CTA) → Diagnóstico corto (5 preguntas) → Modal resultados → Registro (correo/WhatsApp OTP) → Dashboard con starter pack.
2. **Usuario registrado → Completar Diagnóstico 360° → Plan 90 días**
   - Dashboard CTA → Wizard diagnóstico 360° (por secciones) → Resultados + recomendaciones → Plan generado automáticamente (tareas editables).
3. **Emprendedor → Seleccionar herramienta → Integrar en plan**
   - Marketplace filtrado → Tarjeta herramienta → "Agregar a mi plan" → Selección de tarea/semana → Confirmación + link a herramienta.
4. **Emprendedor → Solicitar mentoría → Seguimiento**
   - Módulo mentoría → Filtros → Solicitar mentor → Aprobación coordinador → Chat y agenda → Registro de sesiones.
5. **Donante → Financiar ticket → Ver evidencias**
   - Donaciones → Seleccionar ticket → Pasarela de pago → Confirmación → Dashboard donante (timeline de evidencias y documentos).

---

## Consideraciones Responsive

- **Mobile first**: la navegación superior se convierte en menú hamburguesa; el dashboard reorganiza métricas en carrusel horizontal; timeline del plan se vuelve lista vertical con tarjetas colapsables.
- **Carga progresiva**: uso de placeholders "skeleton" mientras se consulta el backend.
- **Acceso offline parcial**: formularios del diagnóstico guardan localmente hasta reconexión.

---

## Próximos Entregables de Diseño

1. Sistema de diseño en Figma con componentes documentados.
2. Prototipo interactivo de los flujos descritos para pruebas de usabilidad con microempresarios.
3. Guía de contenido (microcopy) en español claro y tono cercano.
4. Lineamientos para ilustraciones y fotografías inclusivas (diversidad de género, edad y territorio).

---

Este mockup servirá de referencia para el equipo de desarrollo y stakeholders, permitiendo validar la propuesta de experiencia antes de avanzar a prototipos de alta fidelidad.
