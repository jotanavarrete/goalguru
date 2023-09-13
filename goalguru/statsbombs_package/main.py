from goalguru.statsbombs_package.data_processor import load_all_seasons_past_info
from goalguru.statsbombs_package.params import *
# from goalguru.soccermatch_package.ml_logic.api_connection import get_x_preprocessed
# from goalguru.soccermatch_package.ml_logic.preprocess import scale_x

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler

from goalguru.statsbombs_package.model import initialize_model, train_model, evaluate_model
from goalguru.statsbombs_package.registry import load_model, save_model, save_results, load_scaler

from pathlib import Path
from colorama import Fore, Style
import pandas as pd

def train(
    test_size = 0.3,
    random_state = 79
) -> float:

    """
    - Loads processed data from local folders
    - Train on preprocessed dataset
    - Store training results

    Return val_accuracy as float
    """
    print(Fore.MAGENTA + "\n⭐️ Use case: train" + Style.RESET_ALL)
    print(Fore.BLUE + "\nLoading preprocessed validation data..." + Style.RESET_ALL)

    all_data = load_all_seasons_past_info(save_concat=False)
    all_data_not_na = all_data.dropna(axis=0, how='any')
    X = all_data_not_na.drop(columns=['match_id', 'target'])
    y = all_data_not_na['target']


    print(f'X shape: {X.shape},y shape: {y.shape}')

    # X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=test_size)

    # print(f'X train shape: {X_train.shape}, y train shape: {y_train.shape}')

    model = load_model()

    if model is None:
        model = initialize_model()

    model, val_accu = train_model(model, X, y, validation_split=test_size, random_state=79)

    params = dict(
        context = 'train',
        training_set_size = all_data_not_na.shape[0],
        row_count = len(X),
    )
    # Save results on the hard drive using taxifare.ml_logic.registry
    save_results(params=params, metrics=dict(val_accuracy=val_accu))

    #Save model weight locally
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

    all_data = load_all_seasons_past_info(save_concat=False)
    all_data_not_na = all_data.dropna(axis=0, how='any')
    X = all_data_not_na.drop(columns=['match_id', 'target'])
    y = all_data_not_na['target']

    # load scaler
    scaler = load_scaler()
    X = scaler.transform(X)

    metrics_dict = {}
    accuracy = evaluate_model(model=model, X=X, y=y)
    metrics_dict['accuracy'] = accuracy

    params = dict(
        context = 'evauate',
        training_set_size = all_data_not_na.shape[0],
        row_count = len(X)
    )
    save_results(params=params, metrics=metrics_dict)

    print("✅ evaluate() done \n")

    return accuracy

def pred(X_pred: pd.DataFrame = None):
    """
    Make a prediction using the latest trained model
    """

    print("\n⭐️ Use case: predict")

    if X_pred is None:
        print('❌ X not valid: showing case example')
        all_data = load_all_seasons_past_info(save_concat=False).sample(1)
        all_data_not_na = all_data.fillna(0)
        X_pred = all_data_not_na.drop(columns=['match_id', 'target'])
    model = load_model()
    assert model is not None

    # load scaler
    scaler = load_scaler()
    X_pred = scaler.transform(X_pred)
    y_pred = model.predict_proba(X_pred)

    print("\n✅ prediction done: ", y_pred, model.classes_, "\n")
    return y_pred

if __name__ == '__main__':
    val_accu = train()
    # print(val_accu)
    # accu = evaluate()
    # print(accu)
    #y_pred = pred()
    #print(y_pred)
