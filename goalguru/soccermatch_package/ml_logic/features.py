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
                                   as_home: bool,
                                   index):

        condition_draw = matches['homeWins'] == 0
        if home:
            team_str = 'home_'
        else:
            team_str = 'away_'
        if as_home:
            as_str = 'as_home_'
            condition_team = matches['homeId'] == team
            like = 'homeId'
            condition_win = matches['homeWins'] == 1
            condition_loses = matches['homeWins'] == -1
            pass_accuracy = 'homePassAccuracy'
            shot_accuracy = 'homeShotAccuracy'
            passes = 'totalHomePasses'
            accu_passes = 'accurateHomePasses'
            shots = 'totalHomeShots'
            accu_shots = 'accurateHomeShots'
            goals = 'homeScore'
            goals_in = 'awayScore'
            matchrank = 'homeTeam_matchRank'
            wins = 'homeWins'

        else:
            as_str = 'as_away_'
            condition_team = matches['awayId'] == team
            like = 'awayId'
            condition_win = matches['homeWins'] == -1
            condition_loses = matches['homeWins'] == 1
            pass_accuracy = 'awayPassAccuracy'
            shot_accuracy = 'awayShotAccuracy'
            passes = 'totalAwayPasses'
            accu_passes = 'accurateAwayPasses'
            shots = 'totalAwayShots'
            accu_shots = 'accurateAwayShots'
            goals = 'awayScore'
            goals_in = 'homeScore'
            matchrank = 'awayTeam_matchRank'
            wins = 'homeWins'

        #logic
        try:
            condition = (matches[(condition_team) & condition_date].head(10).shape[0] < 11) & (matches[condition_team & condition_date].head(10).shape[0] > 0)
            inputer = 0
        except:
            condition = True
            inputer = None
        if condition:
            try:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_pass_accu'] = matches[(condition_team) & condition_date].head(10)[[like, pass_accuracy]].groupby(like).mean().loc[team,pass_accuracy]
            except:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_pass_accu'] = inputer
            try:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_shot_accu'] = matches[(condition_team) & condition_date].head(10)[[like, shot_accuracy]].groupby(like).mean().loc[team,shot_accuracy]
            except:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_shot_accu'] = inputer
            try:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_total_passes'] = matches[(condition_team) & condition_date].head(10)[[like, passes]].groupby(like).mean().loc[team,passes]
            except:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_total_passes'] = inputer
            try:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_total_accu_passes'] = matches[(condition_team) & condition_date].head(10)[[like, accu_passes]].groupby(like).mean().loc[team,accu_passes]
            except:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_total_accu_passes'] = inputer
            try:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_total_shots'] = matches[(condition_team) & condition_date].head(10)[[like, shots]].groupby(like).mean().loc[team,shots]
            except:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_total_shots'] = inputer
            try:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_total_accu_shots'] = matches[(condition_team) & condition_date].head(10)[[like, accu_shots]].groupby(like).mean().loc[team,accu_shots]
            except:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_total_accu_shots'] = inputer
            try:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_total_goals'] = matches[(condition_team) & condition_date].head(10)[[like, goals]].groupby(like).mean().loc[team,goals]
            except:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_total_goals'] = inputer
            try:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_total_goals_in'] = matches[(condition_team) & condition_date].head(10)[[like, goals_in]].groupby(like).mean().loc[team,goals_in]
            except:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_total_goals_in'] = inputer
            try:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_matchranks'] = matches[(condition_team) & condition_date].head(10)[[like, matchrank]].groupby(like).mean().loc[team,matchrank]
            except:
                matches.loc[index, f'last_10_{team_str}{as_str}avg_matchranks'] = inputer
            try:
                matches.loc[index, f'last_10_{team_str}{as_str}total_wins'] = matches[condition_team & condition_date & condition_win].head(10)[[like, wins]].groupby(like).count().loc[team,wins]
            except:
                matches.loc[index, f'last_10_{team_str}{as_str}total_wins'] = inputer
            try:
                matches.loc[index, f'last_10_{team_str}{as_str}total_draws'] = matches[condition_team & condition_date & condition_draw].head(10)[[like, wins]].groupby(like).count().loc[team, wins]
            except:
                matches.loc[index, f'last_10_{team_str}{as_str}total_draws'] = inputer
            try:
                matches.loc[index, f'last_10_{team_str}{as_str}total_loses'] = matches[condition_team & condition_date & condition_loses].head(10)[[like, wins]].groupby(like).count().loc[team,wins]
            except:
                matches.loc[index, f'last_10_{team_str}{as_str}total_loses'] = inputer
            try:
                matches.loc[index, f'last_10_{team_str}{as_str}win_ratio'] = matches.loc[index, f'last_10_{team_str}{as_str}total_wins'] / (matches.loc[index, f'last_10_{team_str}{as_str}total_wins'] +
                                                                                                                                        matches.loc[index, f'last_10_{team_str}{as_str}total_draws']+
                                                                                                                                           matches.loc[index, f'last_10_{team_str}{as_str}total_loses'])
            except:
                matches.loc[index, f'last_10_{team_str}{as_str}win_ratio'] = inputer
            else:
                pass
        return matches

    for index,row in matches.iterrows():
        home_id = matches['homeId'].iloc[index]
        away_id = matches['awayId'].iloc[index]
        date = matches['dateutc'].iloc[index]

        condition_date = matches['dateutc']<date

        get_features_for_team(home_id, True, True, index)
        get_features_for_team(home_id, True, False, index)
        get_features_for_team(away_id, False, True, index)
        get_features_for_team(away_id, False, False, index)
    return matches
