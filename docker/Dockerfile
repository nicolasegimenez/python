# Usa una imagen base de Python 2.7
FROM python:2.7-slim

# Actualiza el índice de paquetes y instala Tkinter
RUN apt-get update && \
    apt-get install -y python-tk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Comando predeterminado para ejecutar cuando se inicie el contenedor
CMD ["python2.7"]

