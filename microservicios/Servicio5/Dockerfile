# Usamos una imagen base de Python
FROM python:3.10-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos el archivo de requisitos
COPY requirements.txt /app/

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código fuente
COPY . /app/

# Exponemos el puerto de la aplicación
EXPOSE 5004

# Comando para ejecutar la app
CMD ["python", "app.py"]