# Modelos: las tablas de la base de datos, escritas en Python
from datetime import datetime

from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Lead(Base):
    """Un posible cliente que ha contactado con Nexora Solutions."""

    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255))
    empresa: Mapped[str] = mapped_column(String(150))
    mensaje: Mapped[str] = mapped_column(Text)
    origen: Mapped[str] = mapped_column(String(20), default="formulario")
    estado: Mapped[str] = mapped_column(String(20), default="nuevo")
    fecha_creacion: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )