import pandas as pd
import numpy as np

def matches_events(matches :pd.DataFrame
                   ,events_encoded:pd.DataFrame) -> pd.DataFrame:
    """
    This function requires first to encode events df with
    accurate_not_accurate() in encoders package

    For every match id in matches dataframe it finds all the passes and shots
    events of the match in events dataframe
    Then it creates for each team (home and away) in every match in the matches
    dataframe, 4 columns corresponding to the count of shots, accurate shots,
    passes, and accurate passes of the current game

    Returns the original matches df with this 8 new columns:
    ['totalHomePasses'], ['accurateHomePasses'], ['totalHomeShots'],
    ['accurateHomeShots']
    ['totalAwayPasses'], ['accurateAwayPasses'], ['totalAwayShots'],
    ['accurateAwayShots']
    """
    home_passes = []
    home_accurate_passes = []
    home_shots = []
    home_accurate_shots = []

    away_passes = []
    away_accurate_passes = []
    away_shots = []
    away_accurate_shots = []

    events = events_encoded.dropna(subset = ['accurate']).copy()
    events.loc[:,'accurate'] = events['accurate'].astype(int)

    condition_shot = (events['eventId']==10)
    condition_pass = (events['eventId']==8)
    condition_accurate = (events['accurate']==1)

    for index,row in matches.iterrows():
        match_id = matches['matchId'].loc[index]
        home_id = matches['homeId'].loc[index]
        away_id = matches['awayId'].loc[index]

        condition_match = (events['matchId']==match_id)
        condition_home_team = (events['teamId'] == home_id)
        condition_away_team = (events['teamId'] == away_id)
        try:
            home_passes.append(events[condition_match & condition_pass & condition_home_team].groupby('eventId').count()['id'].iloc[0])
        except:
            home_passes.append(0)
        try:
            home_accurate_passes.append(events[condition_match & condition_pass & condition_accurate & condition_home_team].groupby('eventId').count()['accurate'].iloc[0])
        except:
            home_accurate_passes.append(0)
        try:
            home_shots.append(events[condition_match & condition_shot & condition_home_team].groupby('eventId').count()['id'].iloc[0])
        except:
            home_shots.append(0)
        try:
            home_accurate_shots.append(events[condition_match & condition_shot & condition_accurate & condition_home_team].groupby('eventId').count()['accurate'].iloc[0])
        except:
            home_accurate_shots.append(0)

        try:
            away_passes.append(events[condition_match & condition_pass & condition_away_team].groupby('eventId').count()['id'].iloc[0])
        except:
            away_passes.append(0)
        try:
            away_accurate_passes.append(events[condition_match & condition_pass & condition_accurate & condition_away_team].groupby('eventId').count()['accurate'].iloc[0])
        except:
            away_accurate_passes.append(0)
        try:
            away_shots.append(events[condition_match & condition_shot & condition_away_team].groupby('eventId').count()['id'].iloc[0])
        except:
            away_shots.append(0)
        try:
            away_accurate_shots.append(events[condition_match & condition_shot & condition_accurate & condition_away_team].groupby('eventId').count()['accurate'].iloc[0])
        except:
            away_accurate_shots.append(0)

    matches['totalHomePasses'], matches['accurateHomePasses'], matches['totalHomeShots'], matches['accurateHomeShots'] = home_passes, home_accurate_passes, home_shots, home_accurate_shots
    matches['totalAwayPasses'], matches['accurateAwayPasses'], matches['totalAwayShots'], matches['accurateAwayShots'] = away_passes, away_accurate_passes, away_shots, away_accurate_shots
    return matches

def get_home_away_names(matches:pd.DataFrame
                        , teams:pd.DataFrame) ->pd.DataFrame:
    """
    This function requieres matches to be encoded first with
    create_home_away_cols() in order to have matches['homeId'] and
    matches['awayId'] in matches df

    Merges matches['homeId'] and matches['awayId'] on teams['wyId'] retrieving
    the team name for each of the teams playing in the match

    Return matches with new columns ['homeTeam'] and ['awayTeam']
    """

    teams = teams[['name', 'wyId']].copy()
    matches = matches.merge(teams, left_on = 'homeId', right_on = 'wyId')
    matches = matches.rename(columns = {'name' : 'homeTeam'}).drop(columns = 'wyId')
    matches = matches.merge(teams, left_on = 'awayId', right_on = 'wyId')
    matches = matches.rename(columns = {'name' : 'awayTeam'}).drop(columns = 'wyId')
    return matches.sort_values(by = 'dateutc', ascending = False)

def get_avg_playerank(matches: pd.DataFrame
                      , playerank: pd.DataFrame) -> pd.DataFrame:
    """
    Merges every lineup playerId from each team in a match with their
    corresponding match rank for that match, and clculates the team
    average matchrank for that team
    Creates the column ['homeTeam_matchRank'] and ['awayTeam_matchRank']

    Returns original match df with those new columns
    """

    home_avg_ranks = []
    away_avg_ranks = []
    def calc_avg_scores(players, index):
        scores = []
        for player in players:
            condition_player = playerank['playerId'] == player
            condition_match = playerank['matchId'] == matches.matchId.iloc[index]
            try:
                player_score = playerank[condition_player & condition_match]['playerankScore'].values[0]
                scores.append(player_score)
            except:
                None
        return np.mean(scores)

    for index, row in matches.iterrows():
        for team in list(matches.teamsData.iloc[index].keys()):
            players = []
            for dic in matches.teamsData.iloc[index][team]['formation']['lineup']:
                    players.append(dic['playerId'])
            if matches.iloc[index].teamsData[team]['side'] == 'home':
                home_avg_ranks.append(calc_avg_scores(players, index))
            else:
                away_avg_ranks.append(calc_avg_scores(players, index))
    matches['homeTeam_matchRank'] = home_avg_ranks
    matches['awayTeam_matchRank'] = away_avg_ranks
    return matches
