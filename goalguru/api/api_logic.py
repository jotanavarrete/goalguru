
import pandas as pd

### Dtafrmes used for example
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

from goalguru.api.fuctions import get_competitions , get_seasons

def get_all_competitions():

    """
    This Fuctions Returns a list of all comptetions, according to each dataset.
    """

    list_competitions_statbombs =  get_competitions(data_soccer, df_name='data_soccer') #get_statbombs_data() ## funcion que trae todas las competencias del dataset en una lista
    list_competitions_soccermatch = get_competitions(data_stats, df_name='data_stats') #get_soccermatch_data()  ## funcion que trae todas las competencias del dataset en una lista

    # Merge the two lists and remove duplicates based on the 'name' key
    merged_list = list_competitions_statbombs + list_competitions_soccermatch

    # Create a set of unique competition names, so only show the names of the competitions without repetition

    return merged_list



def get_all_seasons():

    """
    This Fuctions Returns a list of all seasons, according to each dataset.
    """

    list_seasons_statbombs = get_seasons(data_soccer, df_name='data_soccer') #get_statbombs_data() ## funcion que trae todas las seasons del dataset en una lista
    list_seasons_soccermatch = get_seasons(data_soccer, df_name='data_soccer') #get_soccermatch_data()  ## funcion que trae todas las seasons del dataset en una lista

    merged_list = list_seasons_statbombs + list_seasons_soccermatch

    return merged_list
