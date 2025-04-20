import os
from dotenv import load_dotenv
from pathlib import Path

# Carga el .env desde la raíz del proyecto
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

class Config:
    # Esta es la sintaxis CORRECTA que funciona con las últimas versiones
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:3306/{os.getenv('DB_NAME')}"
        "?charset=utf8mb4"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    SECRET_KEY = os.getenv('SECRET_KEY', 'una-clave-secreta-por-defecto')
    DEBUG = True
    TESTING = True