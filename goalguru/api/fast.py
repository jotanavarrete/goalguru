import pandas as pd
from goalguru.api.api_logic import *
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

## Model from soccermatch_package
from goalguru.soccermatch_package.ml_logic.registry import load_model as load_model_sm

## Model from statsbombs_package
from goalguru.statsbombs_package.registry import load_model as load_model_sb

app = FastAPI()

app.state.model_sm = load_model_sm()
app.state.model_sb = load_model_sb()


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


# competition_id=[0,10]
# http://127.0.0.1:8000/seasons?competition_id=5
@app.get("/seasons")
def get_seasons(competition_id : int):
    seasons = get_all_seasons(competition_id)
    return seasons


# http://127.0.0.1:8000/matches?competition_id=2&season_id=181144&matchweek=2&dataset=soccermatch
# http://127.0.0.1:8000/matches?competition_id=9&season_id=27&matchweek=1&dataset=statsbomb
# http://127.0.0.1:8000/matches?competition_id=55&season_id=43&matchweek=1&dataset=statsbomb

@app.get("/matches")
def get_matches(competition_id : int, season_id : int, matchweek : int, dataset: str):
    matches = get_all_matches(competition_id, season_id, matchweek, dataset)
    return matches


# http://127.0.0.1:8000/predict?match_id=2576335&dataset=soccermatch
@app.get('/predict')
def predict(match_id: int, dataset: str):
    X_preprocessed = pd.read_json(get_X_preprocessed(match_id, dataset))

    # now we do the prediction, depending on the model
    if dataset == 'soccermatch':
        outcome = app.state.model_sm.predict(X_preprocessed)
        prediction = app.state.model_sm.predict_proba(X_preprocessed)
    if dataset == 'statsbomb':
        outcome = app.state.model_sb.predict(X_preprocessed)
        prediction = app.state.model_sb.predict_proba(X_preprocessed)

    refactored_prediction = {
        'outcome': outcome.tolist()[0],
        'probabilities': prediction.tolist()[0][::-1]
    }
    return refactored_prediction


# http://127.0.0.1:8000/results?match_id=1
@app.get("/results")
def get_results(match_id : int):
    results = get_all_results(match_id)
    return results
