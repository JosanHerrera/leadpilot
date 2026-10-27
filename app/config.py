# Configuración de LeadPilot: lee los secretos del archivo .env
from pydantic_settings import BaseSettings, SettingsConfigDict


class Configuracion(BaseSettings):
    # Dirección de la base de datos (viene de DATABASE_URL en el .env)
    database_url: str

    # Le decimos dónde está el archivo de secretos
    model_config = SettingsConfigDict(env_file=".env")


# Creamos la configuración una sola vez para usarla en todo el proyecto
config = Configuracion()