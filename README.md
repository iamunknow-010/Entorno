# Entorno
## 🚀 Descripción del Proyecto
Este repositorio contiene la configuración de un entorno de desarrollo estandarizado, utilizando herramientas de vanguardia para garantizar la reproducibilidad y el despliegue automático.

---

## 🛠️ Justificación Técnica (Evaluación)

### 1. Lenguaje y Entorno (Desafío 1 y 2)
Se utiliza **Python 3.12** por ser el estándar actual en proyectos de IA y Data Science. El uso de **venv** asegura que las dependencias estén aisladas, evitando conflictos entre proyectos.

### 2. Gestión de Dependencias (Desafío 3)
El archivo `requirements.txt` permite que cualquier desarrollador pueda replicar exactamente las librerías necesarias con un solo comando: `pip install -r requirements.txt`.

### 3. Contenerización con Docker (Desafío 4)
Se ha implementado un **Dockerfile** basado en la imagen ligera `python:3.12-slim`. Esto garantiza la **portabilidad**: el código funcionará igual en mi laptop TUF Gaming como en cualquier servidor de producción.

### 4. Automatización CI/CD (Desafío 5)
Se configuró **GitHub Actions** (`main.yml`) para realizar Integración Continua. Cada vez que se sube código, GitHub valida automáticamente que el entorno se construya sin errores (como lo demuestra el check verde ✅ en los commits).

### 5. Seguridad y Buenas Prácticas (Desafío 6)
* **.gitignore:** Configurado para no subir el entorno virtual (`venv/`), manteniendo el repositorio ligero.
* **.env.example:** Se incluye un archivo de ejemplo para la configuración de variables de entorno, protegiendo credenciales sensibles.

---

## 📦 Cómo ejecutar este proyecto
1. Clonar el repositorio.
2. Crear entorno virtual: `python3 -m venv venv`
3. Activar y cargar: `source venv/bin/activate` y `pip install -r requirements.txt`
4. Docker (Opcional): `docker build -t mi-entorno .`