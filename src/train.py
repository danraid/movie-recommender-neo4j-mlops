import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Criar diretório models/ se não existir
if not os.path.exists("models"):
    os.makedirs("models")

# Simulação de dados fictícios de avaliações de filmes
data = {
    "user_id": np.random.randint(1, 101, 1000),  # 100 usuários
    "movie_id": np.random.randint(1, 51, 1000),  # 50 filmes
    "rating": np.random.randint(1, 6, 1000)  # Notas de 1 a 5
}

df = pd.DataFrame(data)

# Codificar IDs para numéricos
encoder_user = LabelEncoder()
encoder_movie = LabelEncoder()

df["user_id"] = encoder_user.fit_transform(df["user_id"])
df["movie_id"] = encoder_movie.fit_transform(df["movie_id"])

# Separar features e target
X = df[["user_id", "movie_id"]]
y = df["rating"]

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Verificar se os dados foram corretamente divididos
print(f"X_train shape: {X_train.shape}, y_train shape: {y_train.shape}")

# Treinar modelo RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Salvar modelo treinado
model_path = "models/recommender.pkl"
joblib.dump(model, model_path)

print(f"✅ Modelo salvo com sucesso em: {model_path}")
