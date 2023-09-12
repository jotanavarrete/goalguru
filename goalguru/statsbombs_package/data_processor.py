import os
import pandas as pd
from goalguru.statsbombs_package.params import ACTUAL_MATCHES_PATH, TRAINING_MATCHES_PATH
from goalguru.statsbombs_package.preprocessor import get_full_season_df, get_past_info
from goalguru.statsbombs_package.data import valid_competitions

def save_full_season_actual_info(competition_id, season_id, merge=True):
    '''
    This function saves a full season with the actual info (passes and shots for
    the actual match) locally.
    `merge` is an optional parameter that indicates if one wants to save the
    dataframe merged with the full info (date, matchweek, etc).
    '''
    filename = f'{competition_id}_{season_id}'
    filename += '_merged.csv' if merge else '.csv'
    file_path = os.path.join(ACTUAL_MATCHES_PATH, filename)
    full_season_df = get_full_season_df(competition_id, season_id, merge)
    full_season_df.to_csv(file_path, header=True, index=False, mode='w+')
    print(f'{filename} saved locally')

def load_full_season_actual_info(competition_id, season_id, merge=True):
    '''
    This function loads a full season with the actual info (passes and shots for
    the actual match) locally.
    `merge` is an optional parameter that indicates if one wants to load the
    dataframe merged with the full info (date, matchweek, etc).
    '''
    filename = f'{competition_id}_{season_id}'
    filename += '_merged.csv' if merge else '.csv'
    file_path = os.path.join(ACTUAL_MATCHES_PATH, filename)
    full_season_df = pd.read_csv(file_path)
    print(f'{filename} loaded locally')
    return full_season_df

def save_all_seasons_actual_info(merge=True):
    '''
    This function saves the full seasons with the actual info (passes and shots for
    the actual match) locally, for all the available competitions and seasons.
    `merge` is an optional parameter that indicates if one wants to save the
    dataframe merged with the full info (date, matchweek, etc).
    '''
    competitions = valid_competitions()
    for _, row in competitions.iterrows():
        save_full_season_actual_info(row['competition_id'], row['season_id'], merge)

def load_all_seasons_actual_info(merge=True, save_concat=False):
    '''
    This function loads the full seasons with the actual info (passes and shots for
    the actual match) locally, for all the available competitions and seasons.
    `merge` is an optional parameter that indicates if one wants to load the
    dataframe merged with the full info (date, matchweek, etc).
    `save_concat` is an optional parameters that indicates if one wants to save
    the concatenation of all the dataframes.
    '''
    seasons_full_dfs = []
    competitions = valid_competitions()
    for _, row in competitions.iterrows():
        full_season = load_full_season_actual_info(row['competition_id'], row['season_id'], merge)
        seasons_full_dfs.append(full_season)

    all_seasons_concat = pd.concat(seasons_full_dfs, axis=0, ignore_index=True)

    if save_concat:
        filename = f'all_seasons'
        filename += '_merged.csv' if merge else '.csv'
        file_path = os.path.join(ACTUAL_MATCHES_PATH, filename)
        all_seasons_concat.to_csv(file_path, header=True, index=False, mode='w+')
        print(f'{filename} saved locally')

    return all_seasons_concat

def get_season_past_info(full_season_actual_info_df):
    '''
    This function receives a dataframe that contains all the actual info of the
    matches of a season, ie, what the function `get_full_season_df` returns,
    and returns a dataframe that contains the past info for all the matches
    and the target.
    '''
    matches = []
    for _, row in full_season_actual_info_df.iterrows():
        res = pd.DataFrame(get_past_info(full_season_actual_info_df, row)).T
        matches.append(res)

    matches_df = pd.concat(matches, ignore_index=True)
    return matches_df

def save_full_season_past_info(competition_id, season_id, merge=True):
    '''
    This function saves a full season with the past info (passes and shots for
    the past matches) locally.
    '''
    filename = f'{competition_id}_{season_id}.csv'
    file_path = os.path.join(TRAINING_MATCHES_PATH, filename)
    full_season_df = load_full_season_actual_info(competition_id, season_id, merge)
    full_season_past = get_season_past_info(full_season_df)
    full_season_past.to_csv(file_path, header=True, index=False, mode='w+')
    print(f'{filename} saved locally')

def save_all_seasons_past_info(merge=True):
    '''
    This function saves the full seasons with the past info (passes and shots for
    the past matches) locally, for all the available competitions and seasons.
    '''
    competitions = valid_competitions()
    for _, row in competitions.iterrows():
        save_full_season_past_info(row['competition_id'], row['season_id'], merge)

def load_full_season_past_info(competition_id, season_id):
    '''
    This function loads a full season with the past info (passes and shots for
    the past matches) locally.
    `merge` is an optional parameter that indicates if one wants to load the
    dataframe merged with the full info (date, matchweek, etc).
    '''
    filename = f'{competition_id}_{season_id}.csv'
    file_path = os.path.join(TRAINING_MATCHES_PATH, filename)
    full_season_df = pd.read_csv(file_path)
    print(f'{filename} loaded locally')
    return full_season_df

def load_all_seasons_past_info(save_concat=False, load_saved=True):
    '''
    This function loads the full seasons with the past info (passes and shots for
    the past matches) locally, for all the available competitions and seasons.
    `merge` is an optional parameter that indicates if one wants to load the
    dataframe merged with the full info (date, matchweek, etc).
    `save_concat` is an optional parameters that indicates if one wants to save
    the concatenation of all the dataframes.
    '''
    if load_saved:
        filename = f'all_seasons.csv'
        file_path = os.path.join(TRAINING_MATCHES_PATH, filename)
        all_seasons = pd.read_csv(file_path)
        print(f'{filename} loaded locally')
        return all_seasons

    seasons_full_dfs = []
    competitions = valid_competitions()
    for _, row in competitions.iterrows():
        full_season = load_full_season_past_info(row['competition_id'], row['season_id'])
        seasons_full_dfs.append(full_season)

    all_seasons_concat = pd.concat(seasons_full_dfs, axis=0, ignore_index=True)

    if save_concat:
        filename = f'all_seasons.csv'
        file_path = os.path.join(TRAINING_MATCHES_PATH, filename)
        all_seasons_concat.to_csv(file_path, header=True, index=False, mode='w+')
        print(f'{filename} saved locally')

    return all_seasons_concat

if __name__ == '__main__':
    # save_full_season_actual_info(2,27, merge=True)
    # print(load_full_season_actual_info(2,27, merge=True).head())
    # save_all_seasons_actual_info()
    # all_seasons_df = load_all_seasons_actual_info(merge=True, save_concat=False)
    # print(all_seasons_df.shape, all_seasons_df['match_id'].nunique())
    # save_full_season_past_info(2, 27)
    # save_all_seasons_past_info()
    all_seasons_past = load_all_seasons_past_info(save_concat=True)
    print(all_seasons_past.shape, all_seasons_past['match_id'].nunique())
