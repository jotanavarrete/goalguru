# import pandas as pd
import goalguru.soccermatch_package.ml_logic.api_connection as sm
import goalguru.statsbombs_package.request as sb
from goalguru.params import ALL_COMPETITIONS, TO_SOCCERMATCH_COMPETITIONS, TO_STATSBOMB_COMPETITIONS


def get_all_competitions():

    """
    This Fuctions Returns a list of all competitions, according to each dataset.
    Since both datasets have repeated competitions, it returns a general list
    that is mapped to the corresponding dataset in sequential functions.
    """
    # list_competitions_statbombs = sb.get_competitions()
    # list_competitions_soccermatch = sm.get_competitions()

    competitions = []

    for k, v in ALL_COMPETITIONS.items():
        competitions.append({'competition_id': k, 'name': v})

    return competitions

def get_all_seasons(competition_id : int):

    """
    This Fuctions Returns a list of all seasons, according to each dataset.
    It uses the mappers from params.py to take the general competition_id
    to the competition_id particular for each dataset.
    """
    list_seasons_soccermatch, list_seasons_statbombs = [], []

    sm_competition_id = TO_SOCCERMATCH_COMPETITIONS.get(competition_id)
    sb_competition_id = TO_STATSBOMB_COMPETITIONS.get(competition_id)

    if sm_competition_id is not None:
        list_seasons_soccermatch = sm.get_seasons(sm_competition_id)

    if sb_competition_id is not None:
        list_seasons_statbombs = sb.get_seasons(sb_competition_id)

    merged_list = list_seasons_soccermatch + list_seasons_statbombs

    return merged_list

def get_all_matches(competition_id : int, season_id : int, matchweek : int, dataset: str):

    """
    This Fuctions Returns a list of all seasons, according to each dataset.
    """
    list_matches = []

    if dataset == 'soccermatch':
        competition_id = TO_SOCCERMATCH_COMPETITIONS.get(competition_id)
        list_matches = sm.get_matches(competition_id, season_id, matchweek)

    elif dataset == 'statsbomb':
        competition_id = TO_STATSBOMB_COMPETITIONS.get(competition_id)
        list_matches = sb.get_matches(competition_id, season_id, matchweek)

    return list_matches



def get_all_results(match_id : int):

    """
    To be deprecated probably.
    This Fuctions Returns a list of all seasons, according to each dataset.
    """

    #list_results_soccermatch =
    list_results_soccermatch = sm.get_results(match_id)

    #merged_list = list_results_soccermatch #+ list_results_soccermatch

    return list_results_soccermatch

def get_X_preprocessed(match_id: int, dataset: str):
    '''
    This function returns a dataframe or array with the needed features to predict
    the outcome of a match. It depends on the dataset it's calling.
    '''
    X_preprocessed = []

    if dataset == 'soccermatch':
        X_preprocessed = sm.get_x_preprocessed(match_id)

    elif dataset == 'statsbomb':
        X_preprocessed = sb.get_X_preprocessed(match_id)


    return X_preprocessed
