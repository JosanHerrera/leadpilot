# Esquemas: qué datos acepta y devuelve la API
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class LeadCrear(BaseModel):
    """Datos que llegan cuando un cliente contacta (desde n8n o /docs)."""

    nombre: str = Field(min_length=2, max_length=100)
    email: EmailStr
    empresa: str = Field(min_length=2, max_length=150)
    mensaje: str = Field(min_length=5)
    origen: Literal["formulario", "email"] = "formulario"


class LeadRespuesta(LeadCrear):
    """Datos que devuelve la API: lo de arriba + lo que añade el sistema."""

    id: int
    estado: str
    fecha_creacion: datetime

    model_config = ConfigDict(from_attributes=True)