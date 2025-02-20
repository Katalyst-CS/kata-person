# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Instala dependencias del sistema necesarias para psycopg2
RUN apt-get update && apt-get install -y libpq-dev

# Copia los archivos de la aplicación
COPY . /app/

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto para Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "src/core/main.py"]