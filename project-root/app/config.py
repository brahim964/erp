import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'erogestoria')  # Usa 'erogestoria' como valor por defecto
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///site.db')  # Usa 'sqlite:///site.db' como valor por defecto
    SQLALCHEMY_TRACK_MODIFICATIONS = False
