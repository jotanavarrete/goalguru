import os
import numpy as np


##################  CONSTANTS  #####################
LOCAL_DATA_PATH = os.path.join(os.path.expanduser('~'), "code", "jotanavarrete","goalguru", "data")
PROCESSED_DATA_PATH = os.path.join(os.path.expanduser('~'), "code", "jotanavarrete","goalguru", "data", "processed_data")
API_DATA_PATH = os.path.join(os.path.expanduser('~'), "code", "jotanavarrete","goalguru", "data", "api_cache")
RAW_DATA_PATH = os.path.join(os.path.expanduser('~'), "code", "jotanavarrete","goalguru", "data", "raw_data")
LOCAL_REGISTRY_PATH =  os.path.join(os.path.expanduser('~'), "code", "jotanavarrete","goalguru", "training_outputs")

##################  CONSTANTS_SOCCMATCH  #####################
SOCCER_PROJECT = "soccer_match"
COLUMN_NAMES_RAW = ['teamsData', 'dateutc', 'competitionId', 'seasonId', 'gameweek', 'wyId','winner']
FEATURES = ['avgHomePassAccuLast10Games','avgHomeShotAccuLast10Games',
                     'avgAwayPassAccuLast10Games','avgAwayShotAccuLast10Games',
                     'homeWRlast10Games', 'awayWRlast10Games',
                    'homeLast10AvgRank', 'awayLast10AvgRank'
                    ]
TARGET = ['homeWins']
DTYPES_RAW = {}
