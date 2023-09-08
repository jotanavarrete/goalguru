
import pandas as pd

### Dtafrmes used for example
"""
data_soccer = pd.DataFrame([
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1,'match': 'match_1'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1,'match': 'match_1'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1,'match': 'match_2'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1,'match': 'match_3'},

    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_1'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_1'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_2'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_3'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_4'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_5'},

    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 1,'match': 'match_1'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 1, 'match': 'match_2'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 1,'match': 'match_3'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 1,'match': 'match_4'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 1,'match': 'match_5'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 1, 'match': 'match_6'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 1, 'match': 'match_7'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 1, 'match': 'match_8'},

    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 2,'match': 'match_1'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 2, 'match': 'match_2'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 2,'match': 'match_3'},

    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 3,'match': 'match_1'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 3, 'match': 'match_2'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 3,'match': 'match_3'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 3,'match': 'match_4'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 3,'match': 'match_5'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 3, 'match': 'match_6'},






    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1, 'match': 'match_1'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1, 'match': 'match_2'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1,'match': 'match_3'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1,'match': 'match_4'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1,'match': 'match_5'},

    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2, 'match': 'match_1'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2, 'match': 'match_2'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_3'},

    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 3, 'match': 'match_1'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 3, 'match': 'match_2'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 3,'match': 'match_3'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 3,'match': 'match_4'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 3,'match': 'match_5'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 3, 'match': 'match_6'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 3, 'match': 'match_7'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 3,'match': 'match_8'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 3,'match': 'match_9'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 3,'match': 'match_10'},

    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 1,'match': 'match_1'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 1,'match': 'match_2'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 1,'match': 'match_3'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 1,'match': 'match_4'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 1,'match': 'match_5'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 1,'match': 'match_6'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 1,'match': 'match_7'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 1,'match': 'match_8'},

    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 2,'match': 'match_1'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 2,'match': 'match_2'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 2,'match': 'match_3'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 2,'match': 'match_4'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 2,'match': 'match_5'},





    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 0, 'season': '2016/2017','match_week': 1, 'match': 'match_1'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1,'match': 'match_2'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1,'match': 'match_3'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1,'match': 'match_4'},

    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 0, 'season': '2016/2017','match_week': 2, 'match': 'match_1'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_2'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_3'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_4'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_5'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_6'},

    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 1, 'season': '2017/2018','match_week': 1, 'match': 'match_1'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 1, 'season': '2017/2018','match_week': 1, 'match': 'match_2'},

    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 1, 'season': '2017/2018','match_week': 2, 'match': 'match_1'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 1, 'season': '2017/2018','match_week': 2, 'match': 'match_2'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 1, 'season': '2017/2018','match_week': 2, 'match': 'match_3'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 1, 'season': '2017/2018','match_week': 2, 'match': 'match_4'},
    ])




data_stats = pd.DataFrame([
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1,'match': 'match_1'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1,'match': 'match_1'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1,'match': 'match_2'},

    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_1'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_1'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_2'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_3'},

    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 1,'match': 'match_1'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 1, 'match': 'match_2'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 1,'match': 'match_3'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 1,'match': 'match_4'},


    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 2,'match': 'match_1'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 2, 'match': 'match_2'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 2,'match': 'match_3'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 2, 'match': 'match_4'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 2,'match': 'match_4'},

    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 3,'match': 'match_1'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 3, 'match': 'match_2'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 3,'match': 'match_3'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 3,'match': 'match_4'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 3,'match': 'match_5'},
    {'competition_id': 0, 'name': 'Premier League' , 'season_id': 1, 'season': '2017/2018', 'match_week': 3, 'match': 'match_6'},






    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1, 'match': 'match_1'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1, 'match': 'match_2'},

    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2, 'match': 'match_1'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2, 'match': 'match_2'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_3'},

    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 3, 'match': 'match_1'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 3, 'match': 'match_2'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 3,'match': 'match_3'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 0, 'season': '2016/2017', 'match_week': 3,'match': 'match_4'},

    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 1,'match': 'match_1'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 1,'match': 'match_2'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 1,'match': 'match_3'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 1,'match': 'match_4'},

    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 2,'match': 'match_1'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 2,'match': 'match_2'},
    {'competition_id': 1, 'name': 'Serie A' , 'season_id': 1, 'season': '2017/2018','match_week': 2,'match': 'match_3'},


    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 0, 'season': '2016/2017','match_week': 1, 'match': 'match_1'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1,'match': 'match_2'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 0, 'season': '2016/2017', 'match_week': 1,'match': 'match_3'},


    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 0, 'season': '2016/2017','match_week': 2, 'match': 'match_1'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_2'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_3'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 0, 'season': '2016/2017', 'match_week': 2,'match': 'match_4'},

    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 1, 'season': '2017/2018','match_week': 1, 'match': 'match_1'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 1, 'season': '2017/2018','match_week': 1, 'match': 'match_2'},

    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 1, 'season': '2017/2018','match_week': 2, 'match': 'match_1'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 1, 'season': '2017/2018','match_week': 2, 'match': 'match_2'},
    {'competition_id': 2, 'name': 'Bundesliga' , 'season_id': 1, 'season': '2017/2018','match_week': 2, 'match': 'match_3'},
    ])

"""

import goalguru.soccermatch_package.ml_logic.api_connection as sm


def get_all_competitions():

    """
    This Fuctions Returns a list of all comptetions, according to each dataset.
    """
    #list_competitions_statbombs =
    list_competitions_soccermatch = sm.get_competitions()

    merged_list = list_competitions_soccermatch #+ list_competitions_statbombs

    return merged_list




def get_all_seasons(competition_id : int):

    """
    This Fuctions Returns a list of all seasons, according to each dataset.
    """

    #list_seasons_statbombs =
    list_seasons_soccermatch = sm.get_seasons(competition_id)

    merged_list = list_seasons_soccermatch #+ list_seasons_statbombs

    return merged_list



def get_all_matches(competition_id : int, season_id : int, matchweek : int):

    """
    This Fuctions Returns a list of all seasons, according to each dataset.
    """

    #list_matches_statbombs =
    list_matches_soccermatch = sm.get_matches(competition_id, season_id, matchweek)

    merged_list = list_matches_soccermatch #+ list_matches_statbombs

    return merged_list



def get_all_results(match_id : int):

    """
    This Fuctions Returns a list of all seasons, according to each dataset.
    """

    #list_results_soccermatch =
    list_results_soccermatch = sm.get_results(match_id)

    #merged_list = list_results_soccermatch #+ list_results_soccermatch

    return list_results_soccermatch
