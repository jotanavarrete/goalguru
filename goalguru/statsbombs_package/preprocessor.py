import pandas as pd
from params import *
from data import read_events

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




if __name__ == '__main__':
    # ev_test = get_events_info_per_match(3890561, 175, 181)
    # print(ev_test)
    pass
