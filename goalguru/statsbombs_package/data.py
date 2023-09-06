import os
import pandas as pd

def valid_competitions():
    '''
    Get a dataframe with the competitions ids and their seasons ids, in which
    we are interested.
    '''
    # TODO: maybe save the path in params file or env vars
    competitions_path = '../../processed_data/statsbomb/competitions_id.csv'
    file_path = os.path.dirname(os.path.abspath(__file__))
    competitions_abs_path = os.path.join(file_path, competitions_path)
    competitions_df = pd.read_csv(competitions_abs_path)
    return competitions_df

if __name__ == '__main__':
    print(valid_competitions())
