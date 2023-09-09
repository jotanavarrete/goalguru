import pandas as pd

from pathlib import Path

from goalguru.soccermatch_package.params import *
from goalguru.soccermatch_package.ml_logic import encoders, merges, features

def load_data():
    """
    Retrieve matches data, events data, playerank data, and teams data from
    local data path
    """
    data_directory = Path(RAW_DATA_PATH).joinpath(SOCCER_PROJECT)
    events_directory = os.path.join(data_directory, 'events')
    matches_directory = os.path.join(data_directory, 'matches')
    other_directory = os.path.join(data_directory, 'other')

    events_file_names = os.listdir(events_directory)
    matches_file_names = os.listdir(matches_directory)

    def read_jsons(directory:Path, file_names:list, replace = ''):
        df ={}
        for file_name in file_names:
            df[f"{file_name.replace(f'{replace}_','').replace('.json','')}"] = pd.read_json(os.path.join(directory,file_name))
        return df
    matches = read_jsons(matches_directory, matches_file_names, 'matches')
    events = read_jsons(events_directory, events_file_names, 'events')
    playerank = pd.read_json(os.path.join(other_directory,'playerank.json'))
    teams = pd.read_json(os.path.join(other_directory,'teams.json'))

    print("✅ matches, events, playerrank and teams loaded")
    return matches, events, playerank, teams

def merge_data(matches:pd.DataFrame,
               events: pd.DataFrame,
               playerank: pd.DataFrame,
               teams: pd.DataFrame
               ) -> pd.DataFrame:
    """
    matches: dataframe of dataframes for each league
    events: dataframe of dataframes for events of each league
    playerank: dataframe of playeranks for each match
    teams: dataframe of teams


    Creates all leagues dataframe doing the corresponding merges

    - league_matches with league_events to retrieve passes and shots for match
    - league_matches with teams to retrieve teams names for match
    - league_matches witch playerank to retrieve matchrank for match

    Re

    """
    leagues = []
    #For each league we merge with events, teams, and playerank
    for league in matches.keys():

        league_events = events[league]
        league_encoded = encoders.accurate_not_accurate(league_events)
        liga = matches[league][COLUMN_NAMES_RAW]
        liga = liga.rename(columns = {'wyId':'matchId'}).copy()


        #We get homeId and awayId to retrieve names and events
        liga = encoders.create_home_away_cols(liga)
        #We get events for every team in a match
        liga = merges.matches_events(liga, league_encoded)
        #We retrieve names
        liga = merges.get_home_away_names(liga,teams)
        #We retrieve matchrank
        liga = merges.get_avg_playerank(liga, playerank)
        #We retrieve gaols
        liga = encoders.get_goals(liga)
        #We get accuracies
        liga = encoders.accuracy_features(liga)
        #We get target
        liga = encoders.matches_target(liga)

        #We append to list of ligas (leagues)
        leagues.append(liga)

        print(f"✅ {league} done!")

    #We stack each league vertically
    all_leagues = pd.DataFrame(columns = leagues[0].keys())
    for liga in leagues:
        all_leagues = pd.concat([all_leagues, liga], axis = 0)
    #return
    print("✅ Dataset complete: all_matches dataset built")
    return all_leagues


def clean_data(matches: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw data by
    dropping Nan values from relevant features
    """
    matches = matches.dropna(subset = FEATURES)
    print("✅ Data cleaned")
    return matches


def create_features(all_matches:pd.DataFrame) -> pd.DataFrame:
    """
    Create relevant 50 features for model

    Returns dataframe with features
    """
    matches = all_matches.copy()
    #Get accuracy features
    matches = features.get_features(matches)

    print("✅ Features created")
    return matches
def create_features1(all_matches:pd.DataFrame) -> pd.DataFrame:
    """
    Create relevant features for model
    [
    'avgHomePassAccuLast10Games','avgHomeShotAccuLast10Games',
    'avgAwayPassAccuLast10Games','avgAwayShotAccuLast10Games',
    'homeWRlast10Games', 'awayWRlast10Games',
    'homeLast10AvgRank', 'awayLast10AvgRank'
    ]
    Returns dataframe with features
    """
    matches = all_matches.copy()
    #Get accuracy features
    matches = features.get_performance(matches)
    #Get matchranks features
    matches = features.get_last_matchranks(matches)
    #Get WR features
    matches = features.get_wr(matches)

    print("✅ Features created")
    return matches

def save_data(
        data: pd.DataFrame,
        file_name:str,
        path: Path,
        message = str
    ) -> None:
    """
    - Save the DataFrame to selected path
    """
    data.to_csv(Path(path).joinpath(file_name), header = True, index = False)

    print(f"✅ {message}, with shape {data.shape}")

def load_processed_data() ->pd.DataFrame:
    """
    Retrieves processed data

    Returns matches_processed
    """
    data_path = Path(PROCESSED_DATA_PATH).joinpath(SOCCER_PROJECT, "soccer_match-matches_processed.csv")
    if not data_path.is_file():
        print("❌ File not found")
    else:
        matches_processed = pd.read_csv(data_path)

    return matches_processed
