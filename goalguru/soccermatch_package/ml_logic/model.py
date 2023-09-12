import numpy as np
import time

from colorama import Fore, Style
from typing import Tuple

from tensorflow import keras

from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import GridSearchCV

# Timing the TensorFlow import
print(Fore.BLUE + "\nLoading TensorFlow..." + Style.RESET_ALL)
start = time.perf_counter()

from tensorflow import keras
from keras import Model, Sequential, layers, regularizers, optimizers
from keras.callbacks import EarlyStopping

end = time.perf_counter()
print(f"\n✅ TensorFlow loaded ({round(end - start, 2)}s)")


## Functions for the model

def initialize_model() -> Model:
    """
    Initialize the Neural Network with random weights
    """

    params = {
    "loss" : ["hinge", "modified_huber"],
    "alpha" : [0.001,0.01, 0.1],
    "penalty" : ["l2", "l1", "elasticnet"],
}
    clf = SGDClassifier(max_iter=10000)
    model = GridSearchCV(clf, param_grid=params, cv=5, n_jobs = -1)


    print("✅ Model initialized")

    return model



def train_model(
        model: Model,
        X: np.ndarray,
        y: np.ndarray,
        validation_split=0.3
    ) -> Tuple[Model, dict]:
    """
    Fit the model and return a tuple (fitted_model, history)
    """
    print(Fore.BLUE + "\nTraining model..." + Style.RESET_ALL)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=validation_split)

    scaler = RobustScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    val_accuracy = accuracy_score(y_test, y_pred)


    print(f"✅ Model trained on {len(X)} rows with accuracy: {round(val_accuracy, 2)}")

    return model, val_accuracy



def evaluate_model(
        model: Model,
        X: np.ndarray,
        y: np.ndarray,
        batch_size=64
    ) -> Tuple[Model, dict]:
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
