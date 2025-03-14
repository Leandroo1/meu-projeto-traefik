# Escolhendo a imagem base
FROM python:3.9-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando o arquivo requirements.txt para dentro do container
COPY requirements.txt /app/

# Instalando as dependências
RUN pip install -r requirements.txt

# Copiando o código da aplicação para dentro do container
COPY . /app/

# Definindo o comando para rodar a aplicação Flask
CMD ["python", "app.py"]