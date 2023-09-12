from goalguru.soccermatch_package.ml_logic import data
from goalguru.soccermatch_package.params import *
from goalguru.soccermatch_package.ml_logic.api_connection import get_x_preprocessed

from sklearn.model_selection import train_test_split
from goalguru.soccermatch_package.ml_logic.model import initialize_model, train_model, evaluate_model, compile_model
from goalguru.soccermatch_package.ml_logic.registry import load_model, save_model, save_results

from pathlib import Path
from colorama import Fore, Style
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
    merged_data_path = Path(processed_data_path).joinpath(f'{SOCCER_PROJECT}-leagues_merged.csv')
    if not data_query_cache_path.is_file():
        if not merged_data_path.is_file():
            matches, events, playerank, teams = data.load_data()
            all_matches =data.merge_data(matches,
                                        events,
                                        playerank,
                                        teams)
        else:
            all_matches = pd.read_csv(merged_data_path)


        #all_matches = data.create_features(all_matches)
        all_matches = data.create_features(all_matches)

        matches_cleaned = data.clean_data(all_matches)

        X = matches_cleaned[FEATURES]
        y = matches_cleaned[TARGET]

        print("------ Saving data ------")
        print('-------------------------')
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

def train(
    learning_rate = 0.001,
    batch_size = 64,
    patience = 50,
    test_size = 0.3
) -> float:

    """
    - Loads processed data from local folders
    - Train on preprocessed dataset
    - Sotre training results

    Return val_accuracy as float
    """
    print(Fore.MAGENTA + "\n⭐️ Use case: train" + Style.RESET_ALL)
    print(Fore.BLUE + "\nLoading preprocessed validation data..." + Style.RESET_ALL)

    data_processed = data.load_processed_data()

    X = data_processed[FEATURES]
    y = data_processed[TARGET]

    print(f'X shape: {X.shape},y shape: {y.shape}')

    y = pd.get_dummies(y,prefix = 'Class', dtype = int)

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=test_size)

    print(f'X train shape: {X_train.shape}, y train shape: {y_train.shape}')

    model = load_model()

    if model is None:
        model = initialize_model(input_shape=X_train.shape[-1])

    model = compile_model(model, learning_rate=learning_rate)

    model, history = train_model(
        model, X_train, y_train,
        batch_size=batch_size,
        patience=patience
    )
    val_accu = np.max(history.history['val_accuracy'])

    params = dict(
        context = 'train',
        training_set_size = data_processed.shape[0],
        row_count = len(X_train),
    )
    # Save results on the hard drive using taxifare.ml_logic.registry
    save_results(params=params, metrics=dict(val_accuracy=val_accu))

    #Save model weight locaclly
    save_model(model = model)

    return val_accu

def evaluate() -> float:
    """
    Evaluate the performance of the latest production model on processed data
    Return Accuracy as a float
    """
    print(Fore.MAGENTA + "\n⭐️ Use case: evaluate" + Style.RESET_ALL)

    model = load_model()
    assert model is not None

    data_processed = data.load_processed_data()

    X = data_processed[FEATURES]
    y = data_processed[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    y_test = pd.get_dummies(y_test,prefix = 'Class', dtype = int)

    metrics_dict = evaluate_model(model=model, X=X_test, y=y_test)
    accuracy = metrics_dict["accuracy"]

    params = dict(
        context = 'evauate',
        training_set_size = data_processed.shape[0],
        row_count = len(X_test)
    )
    save_results(params=params, metrics=metrics_dict)

    print("✅ evaluate() done \n")

    return accuracy

def pred(X_pred: pd.DataFrame = None) -> np.ndarray:
    """
    Make a prediction using the latest trained model
    """

    print("\n⭐️ Use case: predict")

    if X_pred is None:
        print('❌ X not valid: showing case example')
        X_pred = pd.read_json(get_x_preprocessed(2058017))
    model = load_model()
    assert model is not None

    X_processed = X_pred
    y_pred = model.predict(X_processed)

    print("\n✅ prediction done: ", y_pred, "\n")
    return y_pred
