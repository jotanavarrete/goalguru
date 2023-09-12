import pandas as pd

def get_last_matchranks(matches: pd.DataFrame) -> pd.DataFrame:

    """
    Gets the average match rank of the last 10 games for each team playing
    the current match
    If there are less than 10 games played in the, past the average is
    calculated over that amount of games
    If not games are played in the past it imputes Nan for that team
    in that match

    Creates features ['homeLast10AvgRank'], ['awayLast10AvgRank']

    Returns original df with this features
    """

    matches = matches.sort_values(by = 'dateutc', ascending = False).reset_index()

    home_avg_matchrank = []
    away_avg_matchrank = []

    #matches_last_10_games_of_teams
    for index,row in matches.iterrows():
        #Teams and date
        home_id = matches['homeId'].iloc[index]
        away_id = matches['awayId'].iloc[index]
        date = matches['dateutc'].iloc[index]

        #Conditions
        condition_home_home = matches['homeId']==home_id
        condition_home_away = matches['awayId']==home_id
        condition_away_home = matches['homeId']==away_id
        condition_away_away = matches['awayId']==away_id
        condition_date = matches['dateutc']<date

        #Logic
        #home
        if (matches[(condition_home_home | condition_home_away) & condition_date].head(10).shape[0] < 11) & (matches[(condition_home_home | condition_home_away) & condition_date].head(10).shape[0] > 1):
            try:
                home_as_home_rank = matches[(condition_home_home | condition_home_away)  & condition_date].head(10).groupby('homeId').agg({'homeTeam_matchRank':'sum'}).loc[home_id,'homeTeam_matchRank']
                home_as_away_rank = matches[(condition_home_home | condition_home_away)  & condition_date].head(10).groupby('awayId').agg({'awayTeam_matchRank':'sum'}).loc[home_id,'awayTeam_matchRank']
                home_rank = home_as_home_rank + home_as_away_rank
                avg_home_rank = (home_rank / matches[(condition_home_home | condition_home_away) & condition_date].head(10).shape[0])
                home_avg_matchrank.append(avg_home_rank)
            except:
                home_avg_matchrank.append(None)
        else:
            home_avg_matchrank.append(None)
        #away
        if (matches[(condition_away_home | condition_away_away)  & condition_date].head(10).shape[0] < 11) & (matches[(condition_away_home | condition_away_away)  & condition_date].head(10).shape[0] > 1):
            try:
                away_as_home_rank = matches[(condition_away_home | condition_away_away)  & condition_date].head(10).groupby('homeId').agg({'homeTeam_matchRank':'sum'}).loc[away_id,'homeTeam_matchRank']
                away_as_away_rank = matches[(condition_away_home | condition_away_away)  & condition_date].head(10).groupby('awayId').agg({'awayTeam_matchRank':'sum'}).loc[away_id,'awayTeam_matchRank']
                away_rank = away_as_home_rank + away_as_away_rank
                avg_away_rank = (away_rank / matches[(condition_away_home | condition_away_away) & condition_date].head(10).shape[0])
                away_avg_matchrank.append(avg_away_rank)
            except:
                away_avg_matchrank.append(None)
        else:
            away_avg_matchrank.append(None)

    matches['homeLast10AvgRank'], matches['awayLast10AvgRank'] = home_avg_matchrank, away_avg_matchrank
    matches = matches.drop(columns = 'index')
    return matches


def get_wr(matches: pd.DataFrame) -> pd.DataFrame:
    """
    Gets the win ratio for the last 10 games for each team playing the match
    If there were less than 10 games played in the past it calculates the win
    ratio for the total of games played
    If there were not any games played in the past it sets Nan

    Cretes features ['homeWRlast10Games'] and ['awayWRlast10Games']

    Returns original matches df with this new features
    """

    matches = matches.sort_values(by = 'dateutc', ascending = False).reset_index()
    home_wins = matches['homeWins'] == 1

    home_wr =[]
    away_wr =[]

    #matches_last_10_games_of_teams
    for index,row in matches.iterrows():
        home_id = matches['homeId'].iloc[index]
        away_id = matches['awayId'].iloc[index]
        date = matches['dateutc'].iloc[index]

        condition_home_home = matches['homeId']==home_id
        condition_home_away = matches['awayId']==home_id
        condition_away_home = matches['homeId']==away_id
        condition_away_away = matches['awayId']==away_id
        condition_date = matches['dateutc']<date
        #home_10_games_wr
        if (matches[(condition_home_home | condition_home_away) & condition_date].head(10).shape[0] < 11) & (matches[(condition_home_home | condition_home_away) & condition_date].head(10).shape[0] > 1):
            try:
                home_wins = matches[(condition_home_home | condition_home_away)  & condition_date].head(10).groupby('winner').count().loc[home_id,'homeWins']#home last 10 games wins
                home_wr.append(home_wins/10)
            except:
                home_wr.append(0)
        else:
            home_wr.append(None)

        #away_10_gams_wr
        if (matches[(condition_away_home | condition_away_away)  & condition_date].head(10).shape[0] < 11) & (matches[(condition_away_home | condition_away_away)  & condition_date].head(10).shape[0] > 1):
            try:
                away_wins = matches[(condition_away_home | condition_away_away) & condition_date].head(10).groupby('winner').count().loc[away_id,'homeWins'] #away last 10 games wins
                away_wr.append(away_wins/10)
            except:
                away_wr.append(0)
        else:
            away_wr.append(None)
    matches['homeWRlast10Games'] = home_wr
    matches['awayWRlast10Games'] = away_wr
    matches = matches.drop(columns = 'index')

    return matches

def get_performance(matches:pd.DataFrame) -> pd.DataFrame:

    """
    Gets the average shot accuracy and pass accuracy for the last 10 games
    played by each team
    If less than 10 games were played it calculates the average over the total
    games played
    If not games where played it sets the value Nan for that team

    Creates the features ['avgHomePassAccuLast10Games'],
    ['avgHomeShotAccuLast10Games'],
    ['avgAwayPassAccuLast10Games'],
    ['avgAwayShotAccuLast10Games']

    Return the dataframe with new features

    """
    home_pass_accu = []
    home_shot_accu = []

    away_pass_accu = []
    away_shot_accu = []

    #matches_last_10_games_of_teams
    for index,row in matches.iterrows():
        home_id = matches['homeId'].iloc[index]
        away_id = matches['awayId'].iloc[index]
        date = matches['dateutc'].iloc[index]

        condition_home_home = matches['homeId']==home_id
        condition_home_away = matches['awayId']==home_id
        condition_away_home = matches['homeId']==away_id
        condition_away_away = matches['awayId']==away_id
        condition_date = matches['dateutc']<date

        if (matches[(condition_home_home | condition_home_away) & condition_date].head(10).shape[0] < 11) & (matches[(condition_home_home | condition_home_away) & condition_date].head(10).shape[0] > 1):
            try:
                pass_accu_home_as_home = matches[(condition_home_home | condition_home_away) & condition_date][['homeId','homePassAccuracy']].head(10).groupby('homeId').mean().loc[home_id,'homePassAccuracy']
                shot_accu_home_as_home = matches[(condition_home_home | condition_home_away) & condition_date][['homeId','homeShotAccuracy']].head(10).groupby('homeId').mean().loc[home_id,'homeShotAccuracy']
            except:
                pass_accu_home_as_home = None
                shot_accu_home_as_home = None
            try:
                pass_accu_home_as_away = matches[(condition_home_home | condition_home_away) & condition_date][['awayId','homePassAccuracy']].head(10).groupby('awayId').mean().loc[home_id,'homePassAccuracy']
                shot_accu_home_as_away = matches[(condition_home_home | condition_home_away) & condition_date][['awayId','homeShotAccuracy']].head(10).groupby('awayId').mean().loc[home_id,'homeShotAccuracy']

            except:
                pass_accu_home_as_away = None
                shot_accu_home_as_away = None
            try:
                avg_pass_accu_home = (pass_accu_home_as_home + pass_accu_home_as_away)/2
                avg_shot_accu_home = (shot_accu_home_as_home + shot_accu_home_as_away)/2

                home_pass_accu.append(avg_pass_accu_home)
                home_shot_accu.append(avg_shot_accu_home)
            except:
                home_pass_accu.append(None)
                home_shot_accu.append(None)
        else:
            home_pass_accu.append(None)
            home_shot_accu.append(None)

        if (matches[(condition_away_home | condition_away_away)  & condition_date].head(10).shape[0] < 11) & (matches[(condition_away_home | condition_away_away)  & condition_date].head(10).shape[0] > 1):
            try:
                pass_accu_away_as_home = matches[(condition_away_home | condition_away_away) & condition_date][['homeId','homePassAccuracy']].head(10).groupby('homeId').mean().loc[away_id,'homePassAccuracy']
                shot_accu_away_as_home = matches[(condition_away_home | condition_away_away) & condition_date][['homeId','homeShotAccuracy']].head(10).groupby('homeId').mean().loc[away_id,'homeShotAccuracy']
            except:
                pass_accu_away_as_home = None
                shot_accu_away_as_home = None
            try:
                pass_accu_away_as_away = matches[(condition_away_home | condition_away_away) & condition_date][['awayId','homePassAccuracy']].head(10).groupby('awayId').mean().loc[away_id,'homePassAccuracy']
                shot_accu_away_as_away = matches[(condition_away_home | condition_away_away) & condition_date][['awayId','homeShotAccuracy']].head(10).groupby('awayId').mean().loc[away_id,'homeShotAccuracy']
            except:
                pass_accu_away_as_away = None
                shot_accu_away_as_away = None

            try:
                avg_pass_accu_away = (pass_accu_away_as_home + pass_accu_away_as_away)/2
                avg_shot_accu_away = (shot_accu_away_as_home + shot_accu_away_as_away)/2

                away_pass_accu.append(avg_pass_accu_away)
                away_shot_accu.append(avg_shot_accu_away)
            except:
                away_pass_accu.append(None)
                away_shot_accu.append(None)
        else:
            away_pass_accu.append(None)
            away_shot_accu.append(None)
    matches['avgHomePassAccuLast10Games'],matches['avgHomeShotAccuLast10Games'] = home_pass_accu, home_shot_accu
    matches['avgAwayPassAccuLast10Games'],matches['avgAwayShotAccuLast10Games'] = away_pass_accu, away_shot_accu
    return matches

def get_features(matches):
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
