import os
from goalguru.statsbombs_package.params import PREPROCESSED_PATH
from goalguru.statsbombs_package.preprocessor import get_full_season_df

def save_full_season_preprocessed(competition_id, season_id, merge=False):
    '''
    This function saves a full season preprocessed (X and y) locally.
    `merge` is an optional parameter that indicates if one wants to save the
    dataframe merged with the full info (date, matchweek, etc).
    '''
    filename = f'{competition_id}_{season_id}'
    filename += '_merged.csv' if merge else '.csv'
    file_path = os.path.join(PREPROCESSED_PATH, filename)
    full_season_df = get_full_season_df(competition_id, season_id, merge)
    full_season_df.to_csv(file_path, header=True, index=False, mode='w+')
    print(f'{filename} saved locally')


if __name__ == '__main__':
    save_full_season_preprocessed(2,27)
