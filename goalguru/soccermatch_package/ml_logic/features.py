import pandas as pd

def get_features(matches):
    """
    Gets the features corresponding to aggregate functions for each team in every match,
    for the last 10 games(less games if not enough)

    Creates features
    ['last_10_home_avg_pass_accu',
       'last_10_home_avg_shot_accu',
       'last_10_home_avg_total_passes',
       'last_10_home_avg_total_accu_passes',
       'last_10_home_avg_total_shots',
       'last_10_home_avg_total_accu_shots',
       'last_10_home_avg_total_goals',
       'last_10_home_avg_total_goals_in',
       'last_10_home_avg_matchranks',
       'last_10_home_total_wins', 'last_10_home_total_draws',
       'last_10_home_total_loses', 'last_10_home_win_ratio',
       'last_10_away_avg_pass_accu',
       'last_10_away_avg_shot_accu',
       'last_10_away_avg_total_passes',
       'last_10_away_avg_total_accu_passes',
       'last_10_away_avg_total_shots',
       'last_10_away_avg_total_accu_shots',
       'last_10_away_avg_total_goals',
       'last_10_away_avg_total_goals_in',
       'last_10_away_avg_matchranks',
       'last_10_away_total_wins', 'last_10_away_total_draws',
       'last_10_away_total_loses', 'last_10_away_win_ratio',
       ]

    Returns original df with this features
    """
    def get_features_for_team(team: int,
                                   home: bool,
                                   index):


        if home:
            team_str = 'home_'
        else:
            team_str = 'away_'

        #logic
        condition_team = (matches['homeId'] == team) | (matches['awayId'] == team)
        last_10_games_df = matches[condition_team & condition_date][0:10].copy()
        condition_home = last_10_games_df['homeId'] == team
        condition_away = last_10_games_df['awayId'] == team

        condition_home_win = last_10_games_df['homeWins'] == 1
        condition_away_win = last_10_games_df['homeWins'] == -1
        condition_draw = last_10_games_df['homeWins'] == 0

        if last_10_games_df.shape[0] == 0:
            inputer = None
            #pass accuracy
        else:
            inputer = 0
        try:
            matches.loc[index, f'last_10_{team_str}avg_pass_accu'] = (last_10_games_df[condition_home][['homeId','homePassAccuracy']].groupby('homeId').mean().loc[team, 'homePassAccuracy'] +
                                                                last_10_games_df[condition_away][['awayId','awayPassAccuracy']].groupby('awayId').mean().loc[team, 'awayPassAccuracy'])/2
        except:
            matches.loc[index, f'last_10_{team_str}avg_pass_accu'] = inputer
        #shot accuracy
        try:
            matches.loc[index, f'last_10_{team_str}avg_shot_accu'] = (last_10_games_df[condition_home][['homeId','homeShotAccuracy']].groupby('homeId').mean().loc[team, 'homeShotAccuracy'] +
                                                                        last_10_games_df[condition_away][['awayId','awayShotAccuracy']].groupby('awayId').mean().loc[team, 'awayShotAccuracy'])/2
        except:
            matches.loc[index, f'last_10_{team_str}avg_shot_accu'] = inputer
        #total passes
        try:
            matches.loc[index, f'last_10_{team_str}avg_total_passes'] = (last_10_games_df[condition_home][['homeId','totalHomePasses']].groupby('homeId').mean().loc[team, 'totalHomePasses'] +
                                                                            last_10_games_df[condition_away][['awayId','totalAwayPasses']].groupby('awayId').mean().loc[team, 'totalAwayPasses'])/2
        except:
            matches.loc[index, f'last_10_{team_str}avg_total_passes'] = inputer
        #total accu passes
        try:
            matches.loc[index, f'last_10_{team_str}avg_total_accu_passes'] = (last_10_games_df[condition_home][['homeId','accurateHomePasses']].groupby('homeId').mean().loc[team, 'accurateHomePasses'] +
                                                                                last_10_games_df[condition_away][['awayId','accurateAwayPasses']].groupby('awayId').mean().loc[team, 'accurateAwayPasses'])/2
        except:
            matches.loc[index, f'last_10_{team_str}avg_total_accu_passes'] = inputer
        #total shots
        try:
            matches.loc[index, f'last_10_{team_str}avg_total_shots'] = (last_10_games_df[condition_home][['homeId','totalHomeShots']].groupby('homeId').mean().loc[team, 'totalHomeShots'] +
                                                                        last_10_games_df[condition_away][['awayId','totalAwayShots']].groupby('awayId').mean().loc[team, 'totalAwayShots'])/2
        except:
            matches.loc[index, f'last_10_{team_str}avg_total_shots'] = inputer
        #total accu shots
        try:
            matches.loc[index, f'last_10_{team_str}avg_total_accu_shots'] = (last_10_games_df[condition_home][['homeId','accurateHomeShots']].groupby('homeId').mean().loc[team, 'accurateHomeShots'] +
                                                                                last_10_games_df[condition_away][['awayId','accurateAwayShots']].groupby('awayId').mean().loc[team, 'accurateAwayShots'])/2
        except:
            matches.loc[index, f'last_10_{team_str}avg_total_accu_shots'] = inputer
        #avg total goals
        try:
            matches.loc[index, f'last_10_{team_str}avg_total_goals'] = (last_10_games_df[condition_home][['homeId','homeScore']].groupby('homeId').mean().loc[team, 'homeScore'] +
                                                                        last_10_games_df[condition_away][['awayId','awayScore']].groupby('awayId').mean().loc[team, 'awayScore'])/2
        except:
            matches.loc[index, f'last_10_{team_str}avg_total_goals'] = inputer
        #avg total goals in
        try:
            matches.loc[index, f'last_10_{team_str}avg_total_goals_in'] = (last_10_games_df[condition_home][['homeId','awayScore']].groupby('homeId').mean().loc[team, 'awayScore'] +
                                                                            last_10_games_df[condition_away][['awayId','homeScore']].groupby('awayId').mean().loc[team, 'homeScore'])/2
        except:
            matches.loc[index, f'last_10_{team_str}avg_total_goals_in'] = inputer
        #avg matchranks
        try:
            matches.loc[index, f'last_10_{team_str}avg_matchranks'] = (last_10_games_df[condition_home][['homeId','homeTeam_matchRank']].groupby('homeId').mean().loc[team, 'homeTeam_matchRank'] +
                                                                        last_10_games_df[condition_away][['awayId','awayTeam_matchRank']].groupby('awayId').mean().loc[team, 'awayTeam_matchRank'])/2
        except:
            matches.loc[index, f'last_10_{team_str}avg_matchranks'] = inputer
        #total wins
        try:
            matches.loc[index, f'last_10_{team_str}total_wins'] = last_10_games_df.groupby('winner').count().loc[team, 'homeWins']
        except:
            matches.loc[index, f'last_10_{team_str}total_wins'] = inputer
        #total draws
        try:
            matches.loc[index, f'last_10_{team_str}total_loses'] = (last_10_games_df.groupby('winner').count().loc[0, 'homeWins'])
        except:
            matches.loc[index, f'last_10_{team_str}total_loses'] = inputer
        #total loses
        try:
            matches.loc[index, f'last_10_{team_str}total_draws'] = last_10_games_df.shape[0] - matches.loc[index, f'last_10_{team_str}total_loses'] - matches.loc[index, f'last_10_{team_str}total_wins']
        except:
            matches.loc[index, f'last_10_{team_str}total_draws'] = inputer
        #win ratio
        try:
            total = last_10_games_df.shape[0]
            if total != 0:
                matches.loc[index, f'last_10_{team_str}win_ratio'] = matches.loc[index, f'last_10_{team_str}total_wins'] / total
            else:
                matches.loc[index, f'last_10_{team_str}win_ratio'] = None
        except:
            matches.loc[index, f'last_10_{team_str}win_ratio'] = inputer
        else:
            pass
        return matches

    for index,row in matches.iterrows():
        home_id = matches['homeId'].iloc[index]
        away_id = matches['awayId'].iloc[index]
        date = matches['dateutc'].iloc[index]

        condition_date = matches['dateutc']<date

        get_features_for_team(home_id, True, index)
        get_features_for_team(away_id, False, index)
    return matches
