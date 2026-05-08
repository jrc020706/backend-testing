from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.api import api_router
from src.db.base import Base
from src.db.session import engine

# Importar modelos para que Base.metadata los reconozca
from src.models.role import Role
from src.models.user import User
from src.models.staff import Staff
from src.models.event import Event
from src.models.event_staff import EventStaff
from src.models.refresh_token import RefreshToken

# Crear las tablas en la base de datos (SQLite en este caso)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Planora API",
    description="Backend para gestión de eventos y staff",
    version="1.0.0",
    swagger_ui_parameters={"persistAuthorization": True}
)

# --- CONFIGURACIÓN DE MIDDLEWARES ---

# Configuración de CORS para que Lovable pueda conectarse
# Configuración de CORS permisiva para desarrollo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- CONEXIÓN DE RUTAS ---

# Todas tus APIs colgarán de /api/v1
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "API de Logística funcionando correctamente"}