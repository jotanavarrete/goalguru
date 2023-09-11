# import pandas as pd
import goalguru.soccermatch_package.ml_logic.api_connection as sm
import goalguru.statsbombs_package.request as sb


def get_all_competitions():

    """
    This Fuctions Returns a list of all comptetions, according to each dataset.
    """
    list_competitions_statbombs = sb.get_competitions()
    # list_competitions_soccermatch = sm.get_competitions()

    merged_list = list_competitions_statbombs

    # merged_list = list_competitions_soccermatch #+ list_competitions_statbombs

    return merged_list

def get_all_seasons(competition_id : int):

    """
    This Fuctions Returns a list of all seasons, according to each dataset.
    """

    list_seasons_statbombs = sb.get_seasons(competition_id)
    # list_seasons_soccermatch = sm.get_seasons(competition_id)

    merged_list = list_seasons_statbombs #+ list_seasons_statbombs

    return merged_list

def get_all_matches(competition_id : int, season_id : int, matchweek : int, dataset: str):

    """
    This Fuctions Returns a list of all seasons, according to each dataset.
    """
    list_matches = []

    if dataset == 'soccermatch':
        list_matches = sm.get_matches(competition_id, season_id, matchweek)

    elif dataset == 'statsbomb':
        list_matches = sb.get_matches(competition_id, season_id, matchweek)

    return list_matches



def get_all_results(match_id : int):

    """
    This Fuctions Returns a list of all seasons, according to each dataset.
    """

    #list_results_soccermatch =
    list_results_soccermatch = sm.get_results(match_id)

    #merged_list = list_results_soccermatch #+ list_results_soccermatch

    return list_results_soccermatch
