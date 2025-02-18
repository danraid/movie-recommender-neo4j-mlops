# Usar a imagem oficial do Python
FROM python:3.9

# Definir diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos do projeto para dentro do container
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta 8000 para comunicação externa
EXPOSE 8000

# Comando para iniciar a API
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
