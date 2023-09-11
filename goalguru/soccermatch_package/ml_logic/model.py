import numpy as np
import time

from colorama import Fore, Style
from typing import Tuple

from tensorflow import keras

# Timing the TensorFlow import
print(Fore.BLUE + "\nLoading TensorFlow..." + Style.RESET_ALL)
start = time.perf_counter()

from tensorflow import keras
from keras import Model, Sequential, layers, regularizers, optimizers
from keras.callbacks import EarlyStopping

end = time.perf_counter()
print(f"\n✅ TensorFlow loaded ({round(end - start, 2)}s)")


## Functions for the model

def initialize_model(input_shape: tuple) -> Model:
    """
    Initialize the Neural Network with random weights
    """

    model = Sequential()
    model.add(layers.BatchNormalization())
    model.add(layers.Dense(120, input_dim = input_shape, activation = 'relu'))
    model.add(layers.Dense(80, activation = 'relu'))
    model.add(layers.Dense(40, activation = 'relu'))
    model.add(layers.Dense(20, activation = 'relu'))
    model.add(layers.Dense(12, activation = 'relu'))
    model.add(layers.Dense(6, activation = 'relu'))
    model.add(layers.Dropout(0.2))
    model.add(layers.Dense(4, activation = 'relu'))
    #model.add(layers.Dropout(0.1))
    model.add(layers.Dense(3, activation = 'softmax'))

    print("✅ Model initialized")

    return model



def compile_model(model: Model, learning_rate=0.001) -> Model:
    """
    Compile the Neural Network
    """
    optimizer = keras.optimizers.SGD(learning_rate=learning_rate)
    model.compile(
    loss = 'categorical_crossentropy',
    optimizer = optimizer,
    metrics = 'accuracy'
    )

    print("✅ Model compiled")

    return model



def train_model(
        model: Model,
        X: np.ndarray,
        y: np.ndarray,
        batch_size=64,
        patience=50,
        validation_data=None, # overrides validation_split
        validation_split=0.3
    ) -> Tuple[Model, dict]:
    """
    Fit the model and return a tuple (fitted_model, history)
    """
    print(Fore.BLUE + "\nTraining model..." + Style.RESET_ALL)

    es = EarlyStopping(
        monitor="val_loss",
        patience=patience,
        restore_best_weights=True
    )


    history = model.fit(
        X,
        y,
        validation_split = validation_split,
        validation_data=validation_data,
        shuffle = True,
        epochs = 200,
        batch_size =  batch_size,
        verbose = 0,
        callbacks = [es]
    )
    print(f"✅ Model trained on {len(X)} rows with accuracy: {round(np.max(history.history['val_accuracy']), 2)}")

    return model, history



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

    metrics = model.evaluate(
        x=X,
        y=y,
        batch_size=batch_size,
        verbose=0,
        callbacks=None,
        return_dict=True
    )

    loss = metrics["loss"]
    accuracy = metrics["accuracy"]

    print(f"✅ Model evaluated, accuracy: {round(accuracy, 2)}")

    return metrics
