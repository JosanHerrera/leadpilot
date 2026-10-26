# Punto de entrada de la API de LeadPilot
from fastapi import FastAPI

# Creamos la aplicación (el "camarero")
app = FastAPI(
    title="LeadPilot API",
    description="Agente comercial con IA para Nexora Solutions S.L. (empresa ficticia)",
    version="0.1.0",
)


# Primer endpoint: comprobar que la API está viva
@app.get("/")
def inicio():
    return {"mensaje": "LeadPilot API funcionando"}