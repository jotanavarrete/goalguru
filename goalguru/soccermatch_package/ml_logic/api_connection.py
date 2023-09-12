from goalguru.soccermatch_package.ml_logic.data import load_processed_data
from goalguru.soccermatch_package.params import *
from goalguru.soccermatch_package.utils import save_json, read_json
from pathlib import Path
import pandas as pd


def get_competitions() -> list:
    """
    Retrieves competitions ids and names from processed dataset
    If file containing the competitions already created it retrieves from
    the cache path, if not it creates it

    Returns list of dictionary with keys ['competition_id'] and ['name']

    """
    path = Path(API_DATA_PATH).joinpath(SOCCER_PROJECT, 'competitions_ids.json')
    if not path.is_file():
        matches = load_processed_data()
        l_comp = matches.competitionId.unique().tolist()
        comp = {524 : 'Serie A',
                    364 : 'Premier League',
                    795 : 'LaLiga',
                    412 : 'Ligue 1',
                    426 : 'Bundesliga',
                    102 : 'Euro Cup',
                    28 : 'World Cup'
                }
        competitions = []
        for id in l_comp:
            compet = {}
            compet['competition_id'] = id
            compet['name'] = comp[id]
            competitions.append(compet)
        save_json(competitions, path)
        return competitions
    else:
        competitions = read_json(path)

        return competitions

def get_seasons(competition_id:int) ->list:
    """
    Retrieves season lists from processed dataset given a competition id
    If file containing the season list for the competition already exists
    it retrieves it from the cache path, if not it creates it

    Returns list of dictionary with keys ['season_id'], ['name'],
    ['matchweeks'] and ['dataset']

    """
    path = Path(API_DATA_PATH).joinpath(SOCCER_PROJECT, f'seasons_{competition_id}.json')
    if not path.is_file():
        matches_cleaned = load_processed_data()
        seasons = matches_cleaned[matches_cleaned['competitionId'] == competition_id].seasonId.unique().tolist()
        s = []
        for season in seasons:
            seas_dic = {}
            min_year = matches_cleaned[matches_cleaned['seasonId']==season].dateutc.min()[0:4]
            max_year = matches_cleaned[matches_cleaned['seasonId']==season].dateutc.max()[0:4]
            matchweeks = sorted(matches_cleaned[matches_cleaned['seasonId']==season].gameweek.unique().tolist())
            dataset = 'soccermatch'
            seas_dic['season_id'] = season
            if min_year != max_year:
                seas_dic['name'] = f"{min_year}/{max_year}"
            else:
                seas_dic['name'] = f"{min_year}"
            seas_dic['matchweeks'] = matchweeks
            seas_dic['dataset'] = dataset
            s.append(seas_dic)
        save_json(s, path)
        return s
    else:
        s = read_json(path)
        return s


def get_matches(competition_id : int,
                season_id : int,
                matchweek : int) -> list:
    """
    Retrieves matches lists from processed dataset given a competition id,
    season_id and matchweek
    If file containing the matches list for the competition, season and
    matchweek already exists it retrieves it from the cache path,
    if not it creates it
    Returns list of dictionary with keys ['match_id'], ['name'],
    ['home_team'] and ['away_team']
    """
    path = Path(API_DATA_PATH).joinpath(SOCCER_PROJECT, f'matches_{competition_id}_{season_id}_{matchweek}.json')
    if not path.is_file():
        dataset = load_processed_data()
        condition_comp = dataset['competitionId'] == competition_id
        condition_season = dataset['seasonId'] == season_id
        condition_matchweek = dataset['gameweek'] == matchweek
        condition = condition_comp & condition_season & condition_matchweek
        matches_filt = dataset[condition]
        match_l = []
        for index, row in matches_filt.iterrows():
            m = {}
            m['match_id'] = int(matches_filt.loc[index, 'matchId'])
            m['name'] = f"{matches_filt.loc[index, 'homeTeam']} vs {matches_filt.loc[index, 'awayTeam']}"
            m['home_team'] = matches_filt.loc[index, 'homeTeam']
            m['away_team'] = matches_filt.loc[index, 'awayTeam']
            m['result'] = f"{matches_filt.loc[index, 'homeTeam']} {matches_filt.loc[index, 'homeScore']} - {matches_filt.loc[index, 'awayTeam']} {matches_filt.loc[index, 'awayScore']}"
            match_l.append(m)
        save_json(match_l,path)
        return match_l
    else:
        match_l = read_json(path)
        return match_l


def get_results(match_id : int) -> dict:
    """
    Retrieves result from a given match id from the processed dataset
    If file containing the result for the match id already exists it retrieves
    it from the cache path, if not it creates it

    Returns a dictionary with the key ['result']

    """

    path = Path(API_DATA_PATH).joinpath(SOCCER_PROJECT, f'result_{match_id}.json')
    if not path.is_file():
        dataset = load_processed_data()
        game = dataset[dataset['matchId'] == match_id]
        result = {}
        res = f"{game.homeTeam.values[0]} {game.homeScore.values[0]} - {game.awayTeam.values[0]} {game.awayScore.values[0]}"
        result['result'] = res
        save_json(result,path)
        return result
    else:
        result = read_json(path)
        return result

def get_x_preprocessed(match_id:int = 2058017) -> pd.DataFrame:
    """
    Retrieves features from match ID from processed dataset
    If file containing the features already created it retrieves from
    the cache path, if not it creates it

    Returns dataframe with all features for the match

    """
    path = Path(API_DATA_PATH).joinpath(SOCCER_PROJECT, f'features_{match_id}.json')
    if not path.is_file():
        dataset = load_processed_data()
        features = dataset[dataset['matchId'] == match_id][FEATURES].to_json()
        save_json(features, path)
        return features
    else:
        features = read_json(path)
        return features
