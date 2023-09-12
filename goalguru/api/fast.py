# import pandas as pd
from goalguru.api.api_logic import *
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

## Model from soccermatch_package
# from goalguru.soccermatch_package.ml_logic.registry import load_model as load_model_sm

## Model from statsbombs_package
# from goalguru.statsbombs_package.registry import load_model as load_model_sb

app = FastAPI()

# app.state.model_sm = load_model_sm()
# app.state.model_sb = load_model_sb()


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
# http://127.0.0.1:8000/seasons?competition_id=55
@app.get("/seasons")
def get_seasons(competition_id : int):
    seasons = get_all_seasons(competition_id)
    return seasons


# http://127.0.0.1:8000/matches?competition_id=102&season_id=9291&matchweek=0&dataset=soccermatch
# http://127.0.0.1:8000/matches?competition_id=9&season_id=27&matchweek=1&dataset=statsbomb
# http://127.0.0.1:8000/matches?competition_id=55&season_id=43&matchweek=1&dataset=statsbomb

@app.get("/matches")
def get_matches(competition_id : int, season_id : int, matchweek : int, dataset: str):
    matches = get_all_matches(competition_id, season_id, matchweek, dataset)
    return matches


# http://127.0.0.1:8000/predict?match_id=1
@app.get('/predict')
def predict(match_id: int, dataset: str):
    X_preprocessed = get_X_preprocessed(match_id, dataset)

    # now we do the prediction, depending on the model
    # if dataset == 'soccermatch':
        # prediction = app.state.model_sm.predict(X_preprocessed)
    # if dataset == 'statsbomb':
        # prediction = app.state.model_sb.predict(X_preprocessed)

    # we do something with the prediction (ie, determining the outcome,
    # reversing the probabilities, obtaining the first element)
    refactored_prediction = None  # do something with the prediction!
    # example
    refactored_prediction = {
        'outcome': 1,
        'probabilities': [0.59, 0.25, 0.16]
    }
    return refactored_prediction


# http://127.0.0.1:8000/results?match_id=1
@app.get("/results")
def get_results(match_id : int):
    results = get_all_results(match_id)
    return results
