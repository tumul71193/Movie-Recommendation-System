# Movie Recommendation System

An end-to-end movie recommendation system that provides personalized Top-10 recommendations for existing users and popularity-based recommendations for new users.

## Overview

- Built popularity-based recommendation model.
- Used **Precision\@10, Recall\@10, and NDCG\@10** to evaluate recommendation quality.
- Developed a **FastAPI** backend and **Streamlit** frontend.
- Containerized both services using **Docker**.
- Deployed the application on a **Google Cloud Compute Engine VM**.

## Architecture

```text
User
  ↓
Streamlit Frontend
  ↓
FastAPI Backend
  ↓
Recommendation Engine
  ↓
Precomputed Recommendations
```

## Tech Stack

**Python · Pandas · NumPy · Scikit-learn · FastAPI · Streamlit · Docker · Docker Compose · GCP · GitHub**

## Evaluation

| Metric        | Score |
| ------------- | ----: |
| Precision\@10 |  8.2% |
| Recall\@10    |  6.7% |
| NDCG\@10      | 11.0% |

## Run Locally

```bash
docker-compose build
docker-compose up -d
```

Open:

```text
http://localhost:8501
```

## Cloud Deployment

The application was deployed to a **GCP Compute Engine VM** using Docker Compose, with the Streamlit frontend exposed through the VM's external IP.

## Key Learning

Built and deployed a complete recommendation-system application, covering **ML modeling → evaluation → API development → containerization → cloud deployment**.
