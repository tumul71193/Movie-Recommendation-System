from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"

existing_user_recommendations = pd.read_parquet(
    ARTIFACTS_DIR / "existing_user_top_n_recommendations.parquet"
)

new_user_recommendations = pd.read_parquet(
    ARTIFACTS_DIR / "new_user_top_n_recommendations.parquet"
)

existing_user_ids = set(
    existing_user_recommendations["userid"]
)

def recommend_movies(user_id):
    if user_id in existing_user_ids:
        recommendations = existing_user_recommendations.loc[
            existing_user_recommendations["userid"] == user_id,
            "title"
        ].to_list()
    else:
        recommendations = new_user_recommendations["title"].to_list()

    return recommendations
