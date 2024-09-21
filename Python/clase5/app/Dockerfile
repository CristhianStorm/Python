# Usamos una imagen base de Python
FROM python:3.9

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos necesarios
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando para correr tu aplicación Python
CMD ["python", "main.py"]
