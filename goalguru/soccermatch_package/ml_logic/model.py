import numpy as np
import time
import pickle

from colorama import Fore, Style
from typing import Tuple


from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import GridSearchCV

from goalguru.soccermatch_package.params import *



## Functions for the model

def initialize_model() -> GridSearchCV:
    """
    Initialize the Neural Network with random weights
    """

    params = {
    "loss" : ["modified_huber"],
    "alpha" : [0.001,0.01, 0.1],
    "penalty" : ["l2", "l1", "elasticnet"],
}
    clf = SGDClassifier(max_iter=10000)
    model = GridSearchCV(clf, param_grid=params, cv=5, n_jobs = -1)


    print("✅ Model initialized")

    return model



def train_model(
        model: GridSearchCV,
        X: np.ndarray,
        y: np.ndarray,
        test_size = 0.3
    ) -> Tuple[GridSearchCV, float]:
    """
    Fit the model and return a tuple (fitted_model, history)
    """
    timestamp = time.strftime("%Y%m%d-%H%M%S")

    print(Fore.BLUE + "\nTraining model..." + Style.RESET_ALL)

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=test_size)

    print(f'X train shape: {X_train.shape}, y train shape: {y_train.shape}\n')

    scaler = RobustScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    #Save scaler locally
    scaler_path = os.path.join(LOCAL_REGISTRY_PATH, "scalers", f"{timestamp}.h5")
    with open(scaler_path, 'wb') as file:
        pickle.dump(scaler, file)
    print(f"✅ Scaler saved locally \n")

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    val_accuracy = accuracy_score(y_test, y_pred)

    print(f"✅ Model trained on {len(X_train)} rows with accuracy: {round(val_accuracy, 2)}")

    return model, val_accuracy



def evaluate_model(
        model: GridSearchCV,
        X: np.ndarray,
        y: np.ndarray,
        batch_size=64
    ) -> Tuple[GridSearchCV, float]:
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
