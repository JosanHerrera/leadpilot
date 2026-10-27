# Punto de entrada de la API de LeadPilot
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import Base, motor, obtener_sesion
from app.models import Lead
from app.schemas import LeadCrear, LeadRespuesta


@asynccontextmanager
async def ciclo_de_vida(app: FastAPI):
    # Al arrancar la API: crea las tablas que no existan todavía
    Base.metadata.create_all(bind=motor)
    yield


# Creamos la aplicación (el "camarero")
app = FastAPI(
    title="LeadPilot API",
    description="Agente comercial con IA para Nexora Solutions S.L. (empresa ficticia)",
    version="0.1.0",
    lifespan=ciclo_de_vida,
)


# Comprobar que la API está viva (health check)
@app.get("/")
def inicio():
    return {"mensaje": "LeadPilot API funcionando"}


# Guardar un lead nuevo
@app.post("/leads", response_model=LeadRespuesta, status_code=201)
def crear_lead(datos: LeadCrear, sesion: Session = Depends(obtener_sesion)):
    lead = Lead(**datos.model_dump())
    sesion.add(lead)
    sesion.commit()
    sesion.refresh(lead)
    return lead


# Listar todos los leads (los más recientes primero)
@app.get("/leads", response_model=list[LeadRespuesta])
def listar_leads(sesion: Session = Depends(obtener_sesion)):
    consulta = select(Lead).order_by(Lead.fecha_creacion.desc())
    return sesion.scalars(consulta).all()