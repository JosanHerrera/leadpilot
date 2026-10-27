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

### Cómo funciona una API (pantalla /docs)
- **/docs**: página automática para probar la API sin n8n. También sirve para enseñarla o pasarla a otros desarrolladores.
- **Health check** (`GET /`): "timbre" para comprobar que la API está viva. Azure lo usará para reiniciarla si falla.
- **Métodos HTTP**: `GET` = dame datos (leer) · `POST` = toma datos (crear).
- **Códigos de respuesta**: `200` bien · `201` creado · `404` no existe · `422` datos no válidos · `500` error en nuestro código.
- **JSON**: formato estándar para intercambiar datos entre programas. Parejas `"clave": "valor"` entre `{ }`. Una lista va entre `[ ]`.
- **Response body**: los datos devueltos · **Headers**: información técnica · **Curl**: el mismo pedido como comando de terminal.

### Secretos (.env)
- **.env**: guarda contraseñas y claves. NUNCA se sube a GitHub (está en `.gitignore`).
- **.env.example**: plantilla sin secretos que sí se sube, para saber qué variables hacen falta.
- **DATABASE_URL**: `postgresql+psycopg://usuario:contraseña@servidor:puerto/base_de_datos`
- Si una contraseña se ve (captura, chat...), se cambia. En psql: `\password usuario` (no se muestra al escribir).
- Nunca hacer capturas con el `.env` abierto.

### Conexión Python ↔ PostgreSQL
- **psycopg**: el "cable" entre Python y PostgreSQL.
- **SQLAlchemy (ORM)**: trabajar con la base de datos usando Python en vez de SQL. Crea las tablas a partir de clases.
- **Motor**: la "línea de teléfono" con la base de datos (se crea una vez).
- **Sesión**: una "llamada" por esa línea para cada pedido. Siempre se cierra al terminar.
- **Base**: el "molde" del que heredan todas las tablas.
- `add` prepara · `commit` guarda de verdad · `refresh` recupera lo que puso PostgreSQL (id, fecha).
- **Clave primaria (`id`)**: número único de cada fila.
- **pydantic-settings**: lee el `.env` y avisa si falta alguna variable.

### Models vs Schemas (pregunta de entrevista)
- **models.py**: cómo se GUARDA un lead en la base de datos.
- **schemas.py** (Pydantic): qué datos ACEPTA y DEVUELVE la API.
- Se separan para que el cliente no pueda decidir campos del sistema (id, estado, fecha).
- **Pydantic** valida solo: formato de email, longitudes, valores permitidos. Si falla → `422` y no se guarda nada.

### Estructura del proyecto
- `app/__init__.py`: marca la carpeta `app` como **paquete** de Python (permite `from app.config import ...`).
- `app/config.py` (secretos) · `database.py` (conexión) · `models.py` (tablas) · `schemas.py` (validación) · `main.py` (endpoints).
- **requirements.txt**: lista de librerías con versiones. Se crea con `pip freeze > requirements.txt` y se instala con `pip install -r requirements.txt`.
- ⚠️ En PowerShell, `>` guarda en UTF-16: cambiarlo a **UTF-8** (abajo a la derecha en VS Code).