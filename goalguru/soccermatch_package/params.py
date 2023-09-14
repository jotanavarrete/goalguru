import os
import numpy as np

SOCCER_PROJECT = "soccer_match"

##################  PATHS  #####################
file_path = os.path.dirname(os.path.abspath(__file__))
LOCAL_DATA_PATH = os.path.join(file_path,'..','..',"data")
PROCESSED_DATA_PATH = os.path.join(file_path,'..', '..', "data", "processed_data")
API_DATA_PATH = os.path.join(file_path,'..','..', "data", "api_cache")
RAW_DATA_PATH = os.path.join(file_path,'..','..', "data", "raw_data")
LOCAL_REGISTRY_PATH =  os.path.join(LOCAL_DATA_PATH, "training_outputs", SOCCER_PROJECT)


MODEL_TARGET = os.environ.get("MODEL_TARGET")
GCP_PROJECT = os.environ.get("GCP_PROJECT")
#GCP_PROJECT_WAGON = os.environ.get("GCP_PROJECT_WAGON")
GCP_REGION = os.environ.get("GCP_REGION")
#BQ_DATASET = os.environ.get("BQ_DATASET")
#BQ_REGION = os.environ.get("BQ_REGION")
BUCKET_NAME = os.environ.get("BUCKET_NAME")

GCR_IMAGE = os.environ.get("GCR_IMAGE")
GCR_REGION = os.environ.get("GCR_REGION")
GCR_MEMORY = os.environ.get("GCR_MEMORY")

##################  CONSTANTS_SOCCMATCH  #####################

COLUMN_NAMES_RAW = ['teamsData', 'dateutc', 'competitionId', 'seasonId', 'gameweek', 'wyId','winner']
FEATURES = ['last_10_home_avg_pass_accu',
       'last_10_home_avg_shot_accu',
       'last_10_home_avg_total_passes',
       'last_10_home_avg_total_accu_passes',
       'last_10_home_avg_total_shots',
       'last_10_home_avg_total_accu_shots',
       'last_10_home_avg_total_goals',
       'last_10_home_avg_total_goals_in',
       'last_10_home_avg_matchranks',
       'last_10_home_total_wins', 'last_10_home_total_draws',
       'last_10_home_total_loses', 'last_10_home_win_ratio',
       'last_10_away_avg_pass_accu',
       'last_10_away_avg_shot_accu',
       'last_10_away_avg_total_passes',
       'last_10_away_avg_total_accu_passes',
       'last_10_away_avg_total_shots',
       'last_10_away_avg_total_accu_shots',
       'last_10_away_avg_total_goals',
       'last_10_away_avg_total_goals_in',
       'last_10_away_avg_matchranks',
       'last_10_away_total_wins', 'last_10_away_total_draws',
       'last_10_away_total_loses', 'last_10_away_win_ratio',
       ]
TARGET = 'homeWins'
DTYPES_RAW = {}
