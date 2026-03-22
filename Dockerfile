# Usamos una imagen oficial y estable
FROM python:3.12-slim

# Variables de entorno para optimizar Python en contenedores
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Instalación de dependencias del sistema con limpieza de logs para reducir tamaño
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiamos solo requerimientos primero (Aprovechamiento de Caché de capas)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiamos el resto del código
COPY . .

# Seguridad: No correr como root (Opcional pero muy profesional)
# RUN useradd -m myuser
# USER myuser

CMD ["python", "app.py"]