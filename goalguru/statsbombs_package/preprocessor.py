import pandas as pd
from goalguru.statsbombs_package.params import *
from goalguru.statsbombs_package.data import read_events, read_matches

def clean_matches(df):
    '''
    This function receives a raw matches dataframe and returns it without uninteresting
    columns. It adds the home and away team ids as columns and the target, ie, 1
    if home wins, 0 if it's a draw and -1 if away wins.
    '''
    df = df.drop(columns=COLS_DROP_CLEAN)
    df.loc[:, 'home_id'] = df.loc[:, 'home_team'].map(lambda x: x.get('home_team_id'))
    df.loc[:, 'away_id'] = df.loc[:, 'away_team'].map(lambda x: x.get('away_team_id'))
    df.loc[:, 'target'] = df.apply(lambda x: 1 if x['home_score'] > x['away_score'] else 0 if x['home_score'] == x['away_score'] else -1, axis=1)
    return df

def get_events_info_per_match(match_id, home_id, away_id):
  '''
  This function receives a certain match_id, looks for the events dataframe
  and returns a dataframe with the match_id and grouped interesting info (shots
  and passes) for the home and away team
  '''
  evs = read_events(match_id)
  evs.loc[:, 'type_id'] = evs.loc[:, 'type'].map(lambda x: x['id'])
  evs.loc[:, 'team_id'] = evs.loc[:, 'team'].map(lambda x: x['id'])
  # passes analysis
  passes = evs.query(f'type_id == {PASS_ID}')
  # determines if a pass is completed if it doesn't have an output (which exists
  # only if the pass is not completed)
  passes.loc[:, 'pass_completed'] = passes.loc[:, 'pass'].map(lambda x: 0 if x.get('outcome') else 1)
  # shots analysis
  shots = evs.query(f'type_id == {SHOT_ID}')
  # determines if the shot was on target, a goal and adds its xG
  shots.loc[:, 'shot_on_target'] = shots.loc[:, 'shot'].map(lambda x: 1 if x.get('outcome').get('id') in SHOT_ON_TARGET_IDS else 0)
  shots.loc[:, 'shot_goal'] = shots.loc[:, 'shot'].map(lambda x: 1 if x.get('outcome').get('id') == GOAL_ID else 0)
  shots.loc[:, 'shot_xg'] = shots.loc[:, 'shot'].map(lambda x: x.get('statsbomb_xg'))
  # aggregating the stats
  passes_grouped = passes.groupby(by='team_id').agg({'pass_completed': 'sum', 'type_id': 'size'})
  passes_grouped.loc[:, 'pass_precision'] = passes_grouped.loc[:, 'pass_completed'] / passes_grouped.loc[:, 'type_id'].map(lambda x: max(1,x))
  passes_grouped.rename(columns={'type_id': 'pass_total'}, inplace=True)

  shots_grouped = shots.groupby(by='team_id').agg({'shot_on_target': 'sum', 'shot_goal': 'sum', 'shot_xg': 'sum', 'type_id': 'size'})
  shots_grouped.loc[:, 'shot_precision'] = shots_grouped.loc[:, 'shot_on_target'] / shots_grouped.loc[:, 'type_id'].map(lambda x: max(1,x))
  shots_grouped.loc[:, 'shot_conversion'] = shots_grouped.loc[:, 'shot_goal'] / shots_grouped.loc[:, 'type_id'].map(lambda x: max(1,x))
  shots_grouped.rename(columns={'type_id': 'shot_total'}, inplace=True)

  grouped_df = pd.concat([passes_grouped, shots_grouped], axis=1)

  dummy_df = pd.DataFrame({'match_id': [match_id],
                           'home_id': [home_id],
                           'away_id': [away_id]})

  home_df = dummy_df.merge(grouped_df, left_on='home_id', right_on='team_id', suffixes=('', '_home'))
  away_df = home_df.merge(grouped_df, left_on='away_id', right_on='team_id', suffixes=('_home', '_away'))

  return away_df.drop(columns=['home_id', 'away_id'])

def get_full_season_df(competition_id, season_id, merge=True):
    '''
    This function receives a competition_id and a season_id and returns a
    dataframe that contains the full actual info for all the matches for the
    given season (and competition).
    `merge` is an optional parameter that tells if you want to merge the clean
    matches dataframe (date, time...) with the new computed features.
    '''
    matches_df = read_matches(competition_id, season_id)
    matches_df = clean_matches(matches_df)

    events = []
    for _, row in matches_df.iterrows():
        match_id = row['match_id']
        home_id = row['home_id']
        away_id = row['away_id']
        events.append(get_events_info_per_match(match_id, home_id, away_id))

    matches_full_df = pd.concat(events, axis=0).reset_index(drop=True)
    if merge:
        matches_full_df = matches_df.merge(matches_full_df, on='match_id', how='left')

    return matches_full_df

def get_past_info_per_team(match_full, team_id, actual_date, if_home, past_games=10):
    '''
    This function receives a match_full dataframe with actual info, the team_id
    for which we want to compute the past info, the actual date to look into the
    past, if_home a boolean that indicates if the actual team is home or away, and
    the number of past games we want to compute the past info.
    '''
    home_cols = [feat for feat in match_full.columns if '_home' in feat]
    away_cols = [feat for feat in match_full.columns if '_away' in feat]
    home_or_away = home_cols if if_home else away_cols
    all_past_cols = [feat + '_all_past' for feat in home_or_away]
    last_cols = [feat + f'_last_{past_games}' for feat in home_or_away]

    all_prev_matches_home = match_full[(match_full.match_date < actual_date) &
                (match_full.home_id == team_id)][home_cols + ['match_date']]
    all_prev_matches_home.columns = all_past_cols + ['match_date']

    all_prev_matches_away = match_full[(match_full.match_date < actual_date) &
                (match_full.away_id == team_id)][away_cols + ['match_date']]
    all_prev_matches_away.columns = all_past_cols + ['match_date']

    all_prev_matches = pd.concat([all_prev_matches_home, all_prev_matches_away]).sort_values('match_date')
    last_prev_matches = all_prev_matches.tail(past_games)
    last_prev_matches.columns = last_cols + ['match_date']

    mean_all_prev = all_prev_matches.drop(columns='match_date').apply('mean', axis=0)
    mean_last_prev = last_prev_matches.drop(columns='match_date').apply('mean', axis=0)
    final_df = pd.concat([mean_all_prev, mean_last_prev], axis=0)

    return final_df

def get_past_info(match_full, match, past_games=10):
    '''
    Receives a full matches dataset with the actual info,
    the match for which we want to compute the
    mean of the features in the past for each team (home and away)
    and 'past_games' a variable that indicates for how many past matches
    we want to compute the average. It returns a dataframe whose first column
    is the match id, followed by the average of the past metrics for the home
    and away teams.
    '''
    # TODO: see if we want to drop this columns now or before (while processing)
    to_drop = ['kick_off', 'competition', 'season', 'home_team', 'away_team', 'home_score', 'away_score', 'competition_stage']
    match_full_dropped = match_full.drop(columns=to_drop)
    match = match.drop(columns=to_drop)
    # useful variables
    actual_date = match['match_date']
    home_team = match['home_id']
    away_team = match['away_id']
    home_last_info = get_past_info_per_team(match_full_dropped, home_team, actual_date, True, past_games)
    away_last_info = get_past_info_per_team(match_full_dropped, away_team, actual_date, False, past_games)
    match_complete = pd.concat([match[['match_id', 'target']], home_last_info, away_last_info], axis=0)
    return match_complete




if __name__ == '__main__':
    # ev_test = get_events_info_per_match(3890561, 175, 181)
    # print(ev_test)
    pass
