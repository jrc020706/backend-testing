# Planora Backend 🚀

Planora es una API robusta y escalable diseñada para la gestión eficiente de eventos y personal (staff). Este proyecto está construido con **FastAPI**, siguiendo principios de **Clean Architecture** y estándares de desarrollo de nivel senior para garantizar mantenibilidad, seguridad y alto rendimiento.

## 🏛️ Arquitectura del Proyecto

El backend está organizado siguiendo una arquitectura por capas (Layered Architecture), lo que desacopla la lógica de negocio de la infraestructura y los detalles de transporte (API).

```text
src/
├── api/            # Capa de Presentación: Definición de rutas y agregación de routers.
│   └── endpoints/  # Controladores específicos (Users, Staff, Events).
├── core/           # Núcleo: Configuración global, seguridad (JWT) y constantes.
├── services/       # Capa de Aplicación: Lógica de negocio principal.
├── crud/           # Capa de Acceso a Datos: Operaciones CRUD genéricas y específicas.
├── models/         # Capa de Dominio: Entidades de base de datos (SQLAlchemy/SQLModel).
├── schemas/        # DTOs (Data Transfer Objects): Modelos de Pydantic para validación.
├── db/             # Infraestructura: Sesión de DB y configuración de motor.
├── middlewares/    # Lógica transversal (CORS, Logging, Error Handling).
└── main.py         # Punto de entrada de la aplicación.
```

## ✨ Características Principales

- **Diseño RESTful**: Endpoints consistentes siguiendo los estándares HTTP.
- **Validación Estricta**: Uso de Pydantic (Capa de Schemas) para contratos de entrada/salida claros.
- **Gestión de Usuarios**: Autenticación y autorización (preparado para JWT).
- **Control de Staff**: Módulos dedicados para la administración de personal.
- **Gestión de Eventos**: Lógica central para la creación y manejo de eventos.
- **Manejo de Errores Global**: Middleware diseñado para proporcionar respuestas consistentes.

## 🛠️ Tecnologías Utilizadas

- **FastAPI**: Framwork web moderno y de alto rendimiento.
- **Pydantic**: Validación de datos y gestión de configuraciones.
- **SQLModel / SQLAlchemy**: ORM para la interacción con la base de datos.
- **Python 3.10+**: Aprovechando tipado estático y asincronía (async/await).

## 🚀 Configuración y Ejecución

### Requisitos Previos

- Python 3.10 o superior.
- Entorno virtual (recomendado).

### Instalación

1. Clona el repositorio:
   ```bash
   git clone <repository-url>
   cd Backend-Planora
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### Ejecución en Desarrollo

Para iniciar el servidor con recarga automática:

```bash
uvicorn src.main:app --reload
```

La documentación interactiva estará disponible en:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🛡️ Estándares de Calidad

- **SOLID**: Aplicación de principios de diseño orientado a objetos.
- **Clean Code**: Código legible, autodocumentado y testeable.
- **Documentación OpenAPI**: Generación automática de especificaciones para el equipo de frontend.

---
Desarrollado con ❤️ por el equipo de Planora.
