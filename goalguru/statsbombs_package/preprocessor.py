import pandas as pd
from params import *
from data import read_events, read_matches

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


if __name__ == '__main__':
    # ev_test = get_events_info_per_match(3890561, 175, 181)
    # print(ev_test)

    match_full_test = get_full_season_df(9, 27)
    print(match_full_test.head())
