"""
Esta Seccion es para crear una API y subir el modelo a internet.

"""
## IMPORTANTE: Hayq eue descomentar cierta lineas que tenga ##%


import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

## Model from soccermatch_package
#% from goalguru.soccermatch_package.preprocessor  import preprocess_features
#% from goalguru.soccermatch_package.registry import load_model

## Model from statsbombs_package
#% from goalguru.statsbombs_package.preprocessor  import preprocess_features
#% from goalguru.statsbombs_package.registry import load_model



app = FastAPI()

#app.state.model =load_model()


# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)




# http://127.0.0.1:8000/predict?pickup_datetime=2012-10-06 12:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2

##%
"""

@app.get("/predict")

def predict(
        pickup_datetime: str,  # 2013-07-06 17:18:00
        pickup_longitude: float,    # -73.950655
        pickup_latitude: float,     # 40.783282
        dropoff_longitude: float,   # -73.984365
        dropoff_latitude: float,    # 40.769802
        passenger_count: int
    ):      # 1

    Make a single course prediction.
    Assumes `pickup_datetime` is provided as a string by the user in "%Y-%m-%d %H:%M:%S" format
    Assumes `pickup_datetime` implicitly refers to the "US/Eastern" timezone (as any user in New York City would naturally write)





    X_pred = pd.DataFrame(dict(
        pickup_datetime=[pd.Timestamp(str(pickup_datetime), tz='UTC')],
        pickup_longitude=[pickup_longitude],
        pickup_latitude=[pickup_latitude],
        dropoff_longitude=[dropoff_longitude],
        dropoff_latitude=[dropoff_latitude],
        passenger_count=[passenger_count],
    ))


    #model = load_model()
    #assert model is not None

    X_processed = preprocess_features(X_pred)
    y_pred = app.state.model.predict(X_processed)

    return {'fare_amount': float(y_pred)} # YOUR CODE HERE

"""

@app.get("/")
def root():
    return {'greeting': 'Hello'}


from goalguru.api.api_logic import *

@app.get("/competitions")
def get_competitions():
    competitions = get_all_competitions()
    return competitions


# http://127.0.0.1:8000/seasons?comptition_id_id=102

@app.get("/seasons")
def get_seasons(comptition_id : int):
    seasons = get_all_seasons(comptition_id)
    return seasons


# http://127.0.0.1:8000/matches?competition_id=102&season_id=9291&matchweek=0
@app.get("/matches")
def get_matches(competition_id : int, season_id : int, matchweek : int):
    matches = get_all_matches(competition_id, season_id, matchweek)
    return matches


# http://127.0.0.1:8000/results?match_id=1
@app.get("/results")
def get_results(match_id : int):
    seasons = get_all_results(match_id)
    return seasons