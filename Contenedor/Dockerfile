# Utilizar una imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación
COPY . .

# Exponer el puerto que utiliza Flask
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
