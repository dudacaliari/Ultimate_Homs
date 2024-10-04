# Base image com Python e suporte ao Microsoft SQL Server ODBC Driver
FROM python:3.11-slim

# Instala dependências necessárias para ODBC e outros pacotes
RUN apt-get update && \
    apt-get install -y curl apt-transport-https gnupg2 && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Cria e define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Instala as dependências do projeto
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expõe a porta para o servidor Django (ajuste se necessário)
EXPOSE 8000

# Comando padrão para iniciar o servidor (ajuste conforme o projeto)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "HOMS.wsgi:application"]
