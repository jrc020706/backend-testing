from fastapi import APIRouter
from src.api.endpoints import events, users, staff, roles, auth

api_router = APIRouter()

# Aquí conectas cada módulo de rutas con un prefijo y etiquetas para el Swagger
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(events.router, prefix="/events", tags=["Events"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(staff.router, prefix="/staff", tags=["Staff"])
api_router.include_router(roles.router, prefix="/roles", tags=["Roles"])