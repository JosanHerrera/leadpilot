# Apuntes de LeadPilot

Conceptos y herramientas aprendidos durante el proyecto.

## Fase 1 — Entorno, base de datos y API

### Git y GitHub
- **Git**: guarda el historial de cambios del proyecto.
- **Commit**: una "foto" del proyecto en un momento dado. Permite volver atrás.
- **Rama `main`**: la línea principal del proyecto (nombre por defecto en GitHub).
- **.gitignore**: lista de archivos que Git nunca debe subir (`.venv`, `.env`, temporales).

### Entorno virtual (.venv)
- "Caja" con las librerías de este proyecto, separadas de las de otros proyectos.
- Se activa con `.\.venv\Scripts\Activate.ps1` (se ve `(.venv)` en la terminal).

### PostgreSQL
- Base de datos que guarda información en **tablas** (como un Excel muy potente).
- Diferencia con ChromaDB: ChromaDB busca textos "por significado" (RAG); PostgreSQL guarda datos estructurados.
- Estructura: **servidor** (edificio) → **bases de datos** (pisos) → **esquemas** (carpetas, por defecto `public`) → **tablas**.
- **Puerto**: la "puerta" por la que se conecta un programa. Usamos el **5433**.
- **UTF8**: codificación que admite ñ, tildes y emojis.
- **SQL**: el idioma de las bases de datos. Ej.: `CREATE DATABASE leadpilot;`
- **psql**: programa para hablar con PostgreSQL desde la terminal.
  - `\l` lista las bases de datos · `\q` sale · `q` sale de una lista larga.
- **pgAdmin 4**: programa visual para ver la base de datos.
- **Usuario `postgres`**: administrador (prompt `=#`). Solo para tareas de administración.
- **Usuario `leadpilot_app`**: usuario propio de la API (prompt `=>`), dueño de la base `leadpilot`.
- **Principio de mínimo privilegio**: cada programa solo con los permisos que necesita. Si roban la contraseña de la API, solo afecta a `leadpilot`.

### FastAPI
- Herramienta de Python para crear **APIs**.
- **API**: el "camarero" que recibe pedidos de otros programas (n8n, el panel) y devuelve respuestas.
- **Endpoint**: cada "plato de la carta". Ej.: `POST /leads` (guardar un lead), `GET /leads` (listarlos).
- Ventajas: documentación automática para probar la API, comprueba los datos que recibe, rápida y con soporte de streaming.
- **Uvicorn**: el programa que pone la API en marcha ("abre el restaurante").