#!/bin/bash
ENV_NAME=".venv"

# Criar ambiente virtual
echo "Criando ambiente virtual..."
virtualenv $ENV_NAME

# Ativar ambiente virtual
echo "Ativando ambiente virtual..."
. $ENV_NAME/bin/activate

# Instalar requisitos
echo "Instalando requisitos..."
pip install -r requirements.txt

echo "Todos os requisitos foram instalados com sucesso no ambiente virtual."
