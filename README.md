# 🎬 Movie Recommender System with Neo4j & MLOps 🚀

Este projeto implementa um **Sistema de Recomendação de Filmes** utilizando **bancos de dados em grafos (Neo4j)** e **Machine Learning**. O objetivo é criar um sistema eficiente de recomendação baseado em dados de usuários, interações e características dos filmes.

## 📌 Estrutura do Projeto

```
movie-recommender-neo4j-mlops/
│-- data/               # Diretório de datasets e processamento
│   │-- load_data.py    # Script para carregar os dados
│   │-- preprocess.py   # Script para pré-processamento dos dados
│-- deployments/        # Arquivos de implantação
│   │-- docker-compose.yml    # Configuração para Docker
│   │-- k8s-deployment.yaml   # Configuração para Kubernetes
│-- models/             # Modelos treinados
│   │-- recommender.pkl # Modelo salvo
│-- notebooks/          # Jupyter notebooks para exploração e testes
│-- src/                # Código-fonte principal do projeto
│   │-- api.py          # Implementação da API
│   │-- data_ingestion.py  # Funções para ingestão de dados
│   │-- graph_model.py  # Modelo baseado em grafos
│   │-- train.py        # Código para treinar modelos de ML
│-- mlflow_tracking.py  # Monitoramento de modelos via MLflow
│-- .dockerignore       # Arquivo para ignorar arquivos no Docker
│-- .gitignore          # Arquivo para ignorar arquivos no Git
│-- CONTRIBUTING.md     # Guia de contribuição
│-- Dockerfile          # Arquivo Docker para containerização
│-- LICENSE             # Licença do projeto
│-- README.md           # Documentação do projeto
│-- requirements.txt    # Dependências do projeto
│-- setup.py            # Script de configuração do projeto
```

## 🛠️ Tecnologias Utilizadas

### Linguagens de Programação
![Python](https://img.shields.io/badge/Python-3.9-blue)

### Banco de Dados
![Neo4j](https://img.shields.io/badge/Neo4j-Graph_DB-blue)

### Machine Learning & Data Science
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-yellow)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep_Learning-orange)

### APIs e Frameworks
![FastAPI](https://img.shields.io/badge/FastAPI-API_Framework-green)
![GraphQL](https://img.shields.io/badge/GraphQL-Query_Language-pink)

### Ferramentas DevOps e MLOps
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![MLflow](https://img.shields.io/badge/MLflow-Model_Tracking-lightblue)

## 🚀 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/movie-recommender-neo4j-mlops.git
   cd movie-recommender-neo4j-mlops
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o Neo4j e inicialize o banco de dados.

4. Treine o modelo de recomendação:
   ```bash
   python src/train.py
   ```

5. Inicie a API para fornecer recomendações:
   ```bash
   uvicorn src.api:app --reload
   ```

## 🌐 Testando a API (Deploy no Railway)
A API está disponível publicamente no Railway:

🔗 **Acesse a API:** [https://movie-recommender-neo4j-mlops-production.up.railway.app/](https://movie-recommender-neo4j-mlops-production.up.railway.app/)

### 🔹 Teste a API no navegador:
Para verificar se a API está rodando:
```
https://movie-recommender-neo4j-mlops-production.up.railway.app/
```
Você verá a resposta:
```json
{"message": "API de recomendação de filmes está ativa!"}
```

### 🔹 Testar uma recomendação de filme:
```
https://movie-recommender-neo4j-mlops-production.up.railway.app/recommend/10/5
```
Ou no terminal:
```bash
curl https://movie-recommender-neo4j-mlops-production.up.railway.app/recommend/10/5
```
Se estiver funcionando, verá uma resposta como esta:
```json
{
    "user_id": 10,
    "movie_id": 5,
    "predicted_rating": 3.77
}
```

## 📊 Fluxo do Sistema

1. **Coleta de Dados** → Importação de datasets de filmes e usuários.
2. **Processamento e Armazenamento** → Estruturação dos dados no Neo4j.
3. **Treinamento do Modelo** → Algoritmos de recomendação usando aprendizado de máquina.
4. **API de Recomendações** → Servindo recomendações em tempo real via FastAPI.

## 🏆 Contribuições
Sinta-se à vontade para abrir *issues* e enviar *pull requests* para melhorias!

## 📜 Licença
Este projeto é distribuído sob a licença MIT.

