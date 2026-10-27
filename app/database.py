# Conexión con la base de datos PostgreSQL
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import config

# Motor: la conexión con PostgreSQL, usando la dirección del .env
motor = create_engine(config.database_url)

# Fábrica de sesiones: cada sesión es una "conversación" con la base de datos
SesionLocal = sessionmaker(bind=motor)


# Clase base: todas nuestras tablas heredarán de ella
class Base(DeclarativeBase):
    pass


# Abre una sesión para cada petición a la API y la cierra al terminar
def obtener_sesion():
    sesion = SesionLocal()
    try:
        yield sesion
    finally:
        sesion.close()