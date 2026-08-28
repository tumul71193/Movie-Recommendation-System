from fastapi import FastAPI
from src.recommender import recommend_movies

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Movie Recommendation API is running"}

@app.get("/recommendations/{user_id}")
def get_recommendations(user_id: int):
    recommendations = recommend_movies(user_id)

    return {
        "user_id": user_id,
        "recommendations": recommendations
    }
