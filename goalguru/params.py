import os
import numpy as np


##################  CONSTANTS  #####################
LOCAL_DATA_PATH = os.path.join(os.path.expanduser('~'), "code", "jotanavarrete","goalguru", "data")
PROCESSED_DATA_PATH = os.path.join(os.path.expanduser('~'), "code", "jotanavarrete","goalguru", "data", "processed_data")
RAW_DATA_PATH = os.path.join(os.path.expanduser('~'), "code", "jotanavarrete","goalguru", "data", "raw_data")
LOCAL_REGISTRY_PATH =  os.path.join(os.path.expanduser('~'), "code", "jotanavarrete","goalguru", "training_outputs")

##################  CONSTANTS_SOCCMATCH  #####################
SOCCER_PROJECT = "soccer_match"
COLUMN_NAMES_RAW = ['teamsData','seasonId', 'dateutc', 'winner', 'wyId', 'competitionId', 'gameweek']
FEATURES = ['last_10_home_as_home_avg_pass_accu',
       'last_10_home_as_home_avg_shot_accu',
       'last_10_home_as_home_total_passes',
       'last_10_home_as_home_total_accu_passes',
       'last_10_home_as_home_total_shots',
       'last_10_home_as_home_total_accu_shots',
       'last_10_home_as_home_total_goals',
       'last_10_home_as_home_total_goals_in',
       'last_10_home_as_home_avg_matchranks',
       'last_10_home_as_home_total_wins', 'last_10_home_as_home_total_draws',
       'last_10_home_as_home_total_loses', 'last_10_home_as_home_win_ratio',
       'last_10_home_as_away_avg_pass_accu',
       'last_10_home_as_away_avg_shot_accu',
       'last_10_home_as_away_total_passes',
       'last_10_home_as_away_total_accu_passes',
       'last_10_home_as_away_total_shots',
       'last_10_home_as_away_total_accu_shots',
       'last_10_home_as_away_total_goals',
       'last_10_home_as_away_total_goals_in',
       'last_10_home_as_away_avg_matchranks',
       'last_10_home_as_away_total_wins', 'last_10_home_as_away_total_draws',
       'last_10_home_as_away_total_loses', 'last_10_home_as_away_win_ratio',
       'last_10_away_as_home_avg_pass_accu',
       'last_10_away_as_home_avg_shot_accu',
       'last_10_away_as_home_total_passes',
       'last_10_away_as_home_total_accu_passes',
       'last_10_away_as_home_total_shots',
       'last_10_away_as_home_total_accu_shots',
       'last_10_away_as_home_total_goals',
       'last_10_away_as_home_total_goals_in',
       'last_10_away_as_home_avg_matchranks',
       'last_10_away_as_home_total_wins', 'last_10_away_as_home_total_draws',
       'last_10_away_as_home_total_loses', 'last_10_away_as_home_win_ratio',
       'last_10_away_as_away_avg_pass_accu',
       'last_10_away_as_away_avg_shot_accu',
       'last_10_away_as_away_total_passes',
       'last_10_away_as_away_total_accu_passes',
       'last_10_away_as_away_total_shots',
       'last_10_away_as_away_total_accu_shots',
       'last_10_away_as_away_total_goals',
       'last_10_away_as_away_total_goals_in',
       'last_10_away_as_away_avg_matchranks',
       'last_10_away_as_away_total_wins', 'last_10_away_as_away_total_draws',
       'last_10_away_as_away_total_loses', 'last_10_away_as_away_win_ratio']
TARGET = ['homeWins']
DTYPES_RAW = {}

##################  CONSTANTS_STATSBOMS  #####################
