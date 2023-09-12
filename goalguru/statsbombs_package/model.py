import numpy as np
# import time

from colorama import Fore, Style
from typing import Tuple

# from tensorflow import keras

from goalguru.statsbombs_package.registry import save_scaler

from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import RobustScaler
# from sklearn.model_selection import GridSearchCV

# # Timing the TensorFlow import
# print(Fore.BLUE + "\nLoading TensorFlow..." + Style.RESET_ALL)
# start = time.perf_counter()

# from tensorflow import keras
# from keras import Model, Sequential, layers, regularizers, optimizers
# from keras.callbacks import EarlyStopping

# end = time.perf_counter()
# print(f"\n✅ TensorFlow loaded ({round(end - start, 2)}s)")


## Functions for the model

def initialize_model():
    """
    Initialize the SGD model.
    """
    # this was for the GridSearch
    # params = {
    # "loss" : ["hinge", "modified_huber"],
    # "alpha" : [0.001,0.01, 0.1],
    # "penalty" : ["l2", "l1", "elasticnet"]
    # }

    model = SGDClassifier(loss='modified_huber',
                        penalty='l1',
                        alpha=0.1,
                        max_iter=10000)

    # model = GridSearchCV(clf, param_grid=params, cv=5, n_jobs = -1)

    print("✅ Model initialized")

    return model



def train_model(
        model,
        X: np.ndarray,
        y: np.ndarray,
        validation_split=0.3,
        random_state=79
    ):
    """
    Fit the model and return a tuple (fitted_model, history)
    """
    print(Fore.BLUE + "\nTraining model..." + Style.RESET_ALL)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=validation_split, random_state=79)

    scaler = RobustScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # save the scaler locally
    save_scaler(scaler)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    val_accuracy = accuracy_score(y_test, y_pred)


    print(f"✅ Model trained on {len(X)} rows with accuracy: {round(val_accuracy, 2)}")

    return model, val_accuracy



def evaluate_model(
        model,
        X: np.ndarray,
        y: np.ndarray
    ):
    """
    Evaluate trained model performance on the dataset
    """

    print(Fore.BLUE + f"\nEvaluating model on {len(X)} rows..." + Style.RESET_ALL)

    if model is None:
        print(f"\n❌ No model to evaluate")
        return None

    y_pred = model.predict(X)
    accuracy = accuracy_score(y, y_pred)


    print(f"✅ Model evaluated, accuracy: {round(accuracy, 2)}")

    return accuracy
