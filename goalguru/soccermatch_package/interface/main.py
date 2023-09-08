from goalguru.soccermatch_package.ml_logic import data
from goalguru.soccermatch_package.params import *
from pathlib import Path
import pandas as pd

def preprocess():
    """
    - Load raw matches datasets from all leagues matches and events, and from
    teams and playeranks
    - Merge matches datasets on teams, events, and playeranks
    - Stack leagues into a a dataset containing all leagues information
    - Creates relevant dataset with features and targets
    """

    processed_data_path = Path(PROCESSED_DATA_PATH).joinpath(SOCCER_PROJECT)
    data_query_cache_path = Path(processed_data_path).joinpath(f"{SOCCER_PROJECT}-matches_processed.csv")
    if not data_query_cache_path.is_file():
        matches, events, playerank, teams = data.load_data()

        all_matches =data.merge_data(matches,
                                    events,
                                    playerank,
                                    teams)

        all_matches = data.create_features(all_matches)

        matches_cleaned = data.clean_data(all_matches)

        X = matches_cleaned[FEATURES]
        y = matches_cleaned[TARGET]

        data.save_data(matches_cleaned,
                       f'{SOCCER_PROJECT}-matches_processed.csv',
                       processed_data_path,
                       'Saved processed matches locally')
        data.save_data(X,
                       f'{SOCCER_PROJECT}-X_processed.csv',
                       processed_data_path,
                       'Saved X processed locally')
        data.save_data(y,
                       f'{SOCCER_PROJECT}-y_processed.csv',
                       processed_data_path,
                       'Saved y processed locally')
    else:
        print(f"✅ Data processed already")
