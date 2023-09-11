import os
import pandas as pd
from goalguru.statsbombs_package.params import *

def valid_competitions():
    '''
    Get a dataframe with the competitions ids, seasons ids, competition name
    and season name, in which we are interested.
    '''
    competitions_df = pd.read_csv(VALID_COMPETITIONS_PATH)
    return competitions_df

def read_matches(competition_id, season_id):
    '''
    Get a dataframe with the raw matches (unprocessed), given a competition_id and
    a season_id
    '''
    matches_path = os.path.join(MATCHES_PATH, str(competition_id), f'{str(season_id)}.json')
    matches_df = pd.read_json(matches_path)
    return matches_df

def read_events(match_id):
    '''
    Get a dataframe with the raw events (unprocessed), given a match_id
    '''
    events_path = os.path.join(EVENTS_PATH, f'{str(match_id)}.json')
    events_df = pd.read_json(events_path)
    return events_df


# if __name__ == '__main__':
#     # print(valid_competitions())
#     # print(read_match(2,27).head())
#     test_matches = read_matches(2,27)
#     # from preprocessor import clean_matches
#     # print(clean_matches(test_matches).head())
#     test_match_id = test_matches.iloc[0]['match_id']
#     print(test_match_id)
#     test_events = read_events(test_match_id)
#     print(test_events.head())
