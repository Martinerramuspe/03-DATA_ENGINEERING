# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala las bibliotecas necesarias
RUN pip install pandas cryptography requests

# Copia el código fuente y el archivo requirements.txt a la ubicación de trabajo en el contenedor
COPY ENCRIPTACION04.py requirements.txt /app/

# Instala las bibliotecas necesarias
RUN pip install -r requirements.txt

# Ejecuta el código cuando se inicie el contenedor
CMD ["python", "IMAGE_MODEL.py"]


