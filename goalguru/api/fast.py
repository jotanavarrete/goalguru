# import pandas as pd
from goalguru.api.api_logic import *
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

## Model from soccermatch_package
#% from goalguru.soccermatch_package.preprocessor  import preprocess_features
# from goalguru.soccermatch_package.ml_logic.registry import load_model as load_model_sm

## Model from statsbombs_package
#% from goalguru.statsbombs_package.preprocessor  import preprocess_features
#% from goalguru.statsbombs_package.registry import load_model

app = FastAPI()

# app.state.model_sm = load_model_sm()


# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def root():
    return {'greeting': 'Hello'}

# http://127.0.0.1:8000/competitions
@app.get("/competitions")
def get_competitions():
    competitions = get_all_competitions()
    return competitions


# http://127.0.0.1:8000/seasons?competition_id=102
@app.get("/seasons")
def get_seasons(competition_id : int):
    seasons = get_all_seasons(competition_id)
    return seasons


# http://127.0.0.1:8000/matches?competition_id=102&season_id=9291&matchweek=0&dataset=soccermatch
@app.get("/matches")
def get_matches(competition_id : int, season_id : int, matchweek : int, dataset: str):
    matches = get_all_matches(competition_id, season_id, matchweek, dataset)
    return matches


# http://127.0.0.1:8000/results?match_id=1
@app.get("/results")
def get_results(match_id : int):
    results = get_all_results(match_id)
    return results
