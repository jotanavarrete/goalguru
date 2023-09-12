import os

# PATHS
file_path = os.path.dirname(os.path.abspath(__file__))
raw_data_path = os.path.join('..', '..', 'raw_data', 'open-data', 'data')
proccesed_data_path = os.path.join('..', '..', 'data', 'processed_data', 'statsbomb')

VALID_COMPETITIONS_PATH = os.path.join(file_path, proccesed_data_path, 'competitions_id.csv')
MATCHES_PATH = os.path.join(file_path, raw_data_path, 'matches')
EVENTS_PATH = os.path.join(file_path, raw_data_path, 'events')
REQUEST_PATH = os.path.join(file_path, proccesed_data_path, 'request')
PREPROCESSED_PATH = os.path.join(file_path, proccesed_data_path, 'preprocessed')

# COLUMNS
COLS_DROP_CLEAN = ['match_status', 'match_status_360', 'last_updated', 'last_updated_360', 'metadata', 'stadium', 'referee']

# EVENTS IDS
PASS_ID = 30
SHOT_ON_TARGET_IDS = [96, 97, 100]
GOAL_ID = 97
SHOT_ID = 16
