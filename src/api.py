from fastapi import FastAPI
import joblib
import numpy as np

# Inicializar a API
app = FastAPI()

# Carregar o modelo treinado
model_path = "models/recommender.pkl"
try:
    model = joblib.load(model_path)
    print("✅ Modelo carregado na API!")
except Exception as e:
    print(f"❌ Erro ao carregar o modelo na API: {e}")

# Endpoint para recomendações
@app.get("/recommend/{user_id}/{movie_id}")
def recommend(user_id: int, movie_id: int):
    try:
        predicted_rating = model.predict(np.array([[user_id, movie_id]]))
        return {"user_id": user_id, "movie_id": movie_id, "predicted_rating": round(predicted_rating[0], 2)}
    except Exception as e:
        return {"error": str(e)}

# Endpoint para verificar se a API está rodando
@app.get("/")
def home():
    return {"message": "API de recomendação de filmes está ativa!"}
