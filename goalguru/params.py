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
       'last_10_home_as_home_avg_total_passes',
       'last_10_home_as_home_avg_total_accu_passes',
       'last_10_home_as_home_avg_total_shots',
       'last_10_home_as_home_avg_total_accu_shots',
       'last_10_home_as_home_avg_total_goals',
       'last_10_home_as_home_avg_total_goals_in',
       'last_10_home_as_home_avg_matchranks',
       'last_10_home_as_home_total_wins', 'last_10_home_as_home_total_draws',
       'last_10_home_as_home_total_loses', 'last_10_home_as_home_win_ratio',
       'last_10_home_as_away_avg_pass_accu',
       'last_10_home_as_away_avg_shot_accu',
       'last_10_home_as_away_avg_total_passes',
       'last_10_home_as_away_avg_total_accu_passes',
       'last_10_home_as_away_avg_total_shots',
       'last_10_home_as_away_avg_total_accu_shots',
       'last_10_home_as_away_avg_total_goals',
       'last_10_home_as_away_avg_total_goals_in',
       'last_10_home_as_away_avg_matchranks',
       'last_10_home_as_away_total_wins', 'last_10_home_as_away_total_draws',
       'last_10_home_as_away_total_loses', 'last_10_home_as_away_win_ratio',
       'last_10_away_as_home_avg_pass_accu',
       'last_10_away_as_home_avg_shot_accu',
       'last_10_away_as_home_avg_total_passes',
       'last_10_away_as_home_avg_total_accu_passes',
       'last_10_away_as_home_avg_total_shots',
       'last_10_away_as_home_avg_total_accu_shots',
       'last_10_away_as_home_avg_total_goals',
       'last_10_away_as_home_avg_total_goals_in',
       'last_10_away_as_home_avg_matchranks',
       'last_10_away_as_home_total_wins', 'last_10_away_as_home_total_draws',
       'last_10_away_as_home_total_loses', 'last_10_away_as_home_win_ratio',
       'last_10_away_as_away_avg_pass_accu',
       'last_10_away_as_away_avg_shot_accu',
       'last_10_away_as_away_avg_total_passes',
       'last_10_away_as_away_avg_total_accu_passes',
       'last_10_away_as_away_avg_total_shots',
       'last_10_away_as_away_avg_total_accu_shots',
       'last_10_away_as_away_avg_total_goals',
       'last_10_away_as_away_avg_total_goals_in',
       'last_10_away_as_away_avg_matchranks',
       'last_10_away_as_away_total_wins', 'last_10_away_as_away_total_draws',
       'last_10_away_as_away_total_loses', 'last_10_away_as_away_win_ratio',
       'avgHomePassAccuLast10Games','avgHomeShotAccuLast10Games',
       'avgAwayPassAccuLast10Games','avgAwayShotAccuLast10Games',
       'homeWRlast10Games', 'awayWRlast10Games',
       'homeLast10AvgRank', 'awayLast10AvgRank'
       ]

TARGET = ['homeWins']
DTYPES_RAW = {}

##################  CONSTANTS_STATSBOMS  #####################

##################  API_LOGIC  #####################
# dictionary with all the competitions (independent from dataset origin)
ALL_COMPETITIONS = {
    0: 'Premier League',
    1: 'Serie A',
    2: 'La Liga',
    3: 'Ligue 1',
    4: '1. Bundesliga',
    5: 'FIFA World Cup',
    6: 'UEFA Euro Cup',
    7: "FA Women's Super League",
    8: "Women's World Cup",
    9: "UEFA Women's Euro",
    10: 'Indian Super league'
}
# from ALL_COMPETITIONS to soccermatch dataset
TO_SOCCERMATCH_COMPETITIONS = {
    1: 524,  # 'Serie A'
    0: 364,  # Premier League
    2: 795,  # 'LaLiga'
    3: 412,  # 'Ligue 1'
    4: 426,  # 'Bundesliga'
    6: 102,  # 'Euro Cup'
    5: 28  # 'World Cup'
}
# from ALL_COMPETITIONS to statsbomb dataset
TO_STATSBOMB_COMPETITIONS = {
    4: 9,  # '1. Bundesliga'
    7: 37,  # "FA Women's Super League"
    5: 43,  # 'FIFA World Cup'
    10: 1238,  # 'Indian Super league'
    2: 11,  # 'La Liga'
    3: 7,  # 'Ligue 1'
    0: 2,  # 'Premier League'
    1: 12,  # 'Serie A'
    6: 55,  # 'UEFA Euro'
    8: 72,  # "Women's World Cup"
    9: 53  # "UEFA Women's Euro"
}
