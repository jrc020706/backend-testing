# Planora Backend 🚀

Planora es una API robusta y escalable para la gestión integral de eventos y personal (staff). Diseñada bajo principios de **Clean Architecture**, garantiza seguridad de nivel producción y una alta mantenibilidad.

## 🏛️ Arquitectura del Proyecto

El backend sigue una arquitectura por capas (Layered Architecture), desacoplando la lógica de negocio de la infraestructura:

```text
src/
├── api/            # Capa de Presentación: Routes y Dependency Injection.
│   └── endpoints/  # Controladores: Auth, Users, Staff, Events.
├── core/           # Núcleo: Configuración global, Seguridad (JWT & Hashing).
├── services/       # Capa de Aplicación: Lógica de negocio (ej. validación de fechas).
├── crud/           # Capa de Acceso a Datos: Operaciones SQL optimizadas.
├── models/         # Capa de Dominio: Entidades de SQLAlchemy (Integer PKs para SQLite).
├── schemas/        # DTOs: Modelos de Pydantic para validación y contratos.
├── db/             # Infraestructura: Sesión y configuración del motor de DB.
└── main.py         # Punto de entrada y configuración de Middlewares (CORS).
```

## ✨ Características Principales

- **Seguridad Avanzada**:
  - Hashing de contraseñas con **Bcrypt** (Passlib).
  - Autenticación mediante **JWT (JSON Web Tokens)**.
  - Protección de rutas mediante dependencias de usuario actual.
- **Base de Datos**: SQLite optimizado con tipos `Integer` para garantizar autoincremento automático.
- **Diseño RESTful**: Endpoints consistentes con respuestas estandarizadas y códigos de estado HTTP correctos.
- **Documentación Interactiva**: Swagger UI con soporte para **HTTP Bearer Authorization**.

## 🚀 Configuración y Ejecución

### Requisitos Previos
- Python 3.12+
- Entorno virtual (venv)

### Instalación rápido
```bash
# 1. Clonar el repositorio
git clone https://github.com/jrc020706/backend-testing.git
cd backend-testing

# 2. Configurar entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

### Ejecución en Desarrollo
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

## 🛠️ Cómo Probar la API (Swagger UI)

Accede a: [http://localhost:8000/docs](http://localhost:8000/docs)

1. **Crear Rol**: Usa `POST /roles/` para crear el rol "Admin" (obtendrás ID 1).
2. **Registro**: Crea un usuario en `POST /users/` asociándolo al rol creado.
3. **Login**: Ve a `POST /auth/login`, introduce tus credenciales y **copia el access_token**.
4. **Autorizar**: Haz clic en el botón verde **Authorize** arriba a la derecha, pega el token en el campo **Value** y pulsa Authorize.
5. **Operar**: Ahora todos los candados aparecerán cerrados 🔒 y podrás gestionar Staff y Eventos libremente.

## 🛡️ Estándares y Buenas Prácticas
- **SOLID & Clean Code**: Separación estricta de responsabilidades.
- **CORS Configurado**: Preparado para conexiones seguras con frontends (ej. Lovable.dev).
- **Type Hinting**: Uso extensivo de tipado de Python para reducir errores en tiempo de ejecución.

---
Desarrollado con Profesionalismo por el equipo de Planora.
