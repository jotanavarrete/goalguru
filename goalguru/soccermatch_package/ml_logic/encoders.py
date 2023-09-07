import pandas as pd

def accurate_not_accurate(events:pd.DataFrame) -> pd.DataFrame:
    """
    From a raw dataset of all the events of soccer matches it retrieves all
    shots and passes and create a column indicating if the event was accurate
    (1) or not (0).
    Returns a dataframe with events filtered by shots and passes and with an
    accurate target.
    """
    events_df = events[events['eventId'].isin([8,10])].reset_index().copy()
    accurate = []
    for index, row in events_df.iterrows():
        list = [events_df['tags'].iloc[index][i]['id'] for i in range(len(events_df['tags'].iloc[index]))]
        if 1801 in list:
            accurate.append(1)
        elif 1802 in list:
            accurate.append(0)
        else:
            accurate.append(None)
    events_df['accurate'] = accurate
    events_df = events_df.drop(columns = ['tags','index'])
    return events_df

def create_home_away_cols(matches: pd.DataFrame) -> pd.DataFrame:
    """
    For each matchId in matches df it creates ['homeId'] and ['awayId']
    columns corresponding to the teamId of each of home and away teams
    Returns the original df with this new columns
    """
    home = []
    away = []
    for index, row in matches.iterrows():
        team0 = list(matches.iloc[index].teamsData.keys())[0]
        team1 = list(matches.iloc[index].teamsData.keys())[1]
        if matches.iloc[index].teamsData[team0]['side'] == 'home':
            home.append(team0)
            away.append(team1)
        else:
            home.append(team1)
            away.append(team0)
    matches['homeId'] = home
    matches['homeId'] = matches['homeId'].astype(int)
    matches['awayId'] = away
    matches['awayId'] = matches['awayId'].astype(int)
    return matches

def get_goals(matches:pd.DataFrame) -> pd.DataFrame:
    """
    Retrieves goals from each team for each match id in matches df
    Creates new columns ['homeScore'] and ['awayScore']

    Returns original matches df with these new columns ['homeScore'],
    ['awayScore']
    """
    home_goals = []
    away_goals = []
    for index, row in matches.iterrows():
        team0 = list(matches.loc[index].teamsData.keys())[0]
        team1 = list(matches.loc[index].teamsData.keys())[1]
        goals0 = matches.loc[index].teamsData[team0]['score']
        goals1 = matches.loc[index].teamsData[team1]['score']
        if matches.loc[index].teamsData[team0]['side'] == 'home':
            home_goals.append(goals0)
            away_goals.append(goals1)
        else:
            home_goals.append(goals1)
            away_goals.append(goals0)
    matches['homeScore'] = home_goals
    matches['awayScore'] = away_goals
    return matches

def accuracy_features(matches:pd.DataFrame) ->pd.DataFrame:
    """
    Creates accuracy columns based on shots, passes, accurate shots and
    accurate passes, as accurate/total

    New columns are ['homePassAccuracy'], ['homeShotAccuracy'],
    ['awayPassAccuracy'], ['awayShotAccuracy']

    Returns matches df with these new columns
    """
    matches['homePassAccuracy'] = matches['accurateHomePasses']/matches['totalHomePasses']
    matches['homeShotAccuracy'] = matches['accurateHomeShots']/matches['totalHomeShots']

    matches['awayPassAccuracy'] = matches['accurateAwayPasses']/matches['totalAwayPasses']
    matches['awayShotAccuracy'] = matches['accurateAwayShots']/matches['totalAwayShots']

    return matches

def matches_target(matches:pd.DataFrame) ->pd.DataFrame:

    """
    Creates target column ['homeWins'] that takes the values:
    1 -> home is the winner
    0 -> draw
    -1 -> away is the winner

    Returns dataframe with target column ['homeWins']
    """
    def condition(row):
        if row['winner'] == row['homeId']:
            return 1
        elif row['winner'] == row['awayId']:
            return -1
        elif row['winner'] == 0:
            return 0
        else:
            return None
    matches['homeWins'] = matches.apply(condition, axis = 1)
    matches = matches.drop(columns = 'teamsData')
    return matches
