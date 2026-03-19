#1. imagen de python oficial como base
FROM phyton:3.12-slim

#2. Directorio de trabjo dentro del contenedor
WORKDIR /app

#3. Copiamos archivo de dependencias y se instalan
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirments.txt

#4. Se copia el resto de codigo
COPY . .

# 5. Comando por defecto al iniciar el contenedor
CMD ["python", "--version"]
