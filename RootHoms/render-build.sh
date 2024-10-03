#!/usr/bin/env bash

# Atualiza os pacotes e instala o ODBC Driver 17 para SQL Server
apt-get update && apt-get install -y gnupg2 curl

# Importa a chave GPG necessária para o repositório
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Adiciona o repositório ao source list
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Atualiza e instala o driver ODBC e suas dependências
apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev
