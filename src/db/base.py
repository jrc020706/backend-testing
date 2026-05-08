from sqlalchemy.ext.declarative import declarative_base
from typing import Any

Base: Any = declarative_base()

# No importar modelos aquí para evitar importaciones circulares.
# Los modelos se importan en main.py antes de crear las tablas.
