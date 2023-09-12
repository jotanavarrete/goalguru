import glob
import os
import time
import pickle

from colorama import Fore, Style
from sklearn.model_selection import GridSearchCV

from goalguru.soccermatch_package.params import *

def save_results(params: dict,
                 metrics: dict) -> None:
    """
    Persist params & metrics locally on the hard drive at
    "{LOCAL_REGISTRY_PATH}/params/{current_timestamp}.pickle"
    "{LOCAL_REGISTRY_PATH}/metrics/{current_timestamp}.pickle"
    """

    timestamp = time.strftime("%Y%m%d-%H%M%S")

    #Save params locally
    if params is not None:
        params_path = os.path.join(LOCAL_REGISTRY_PATH, "params", timestamp + ".pickle")
        with open(params_path, "wb") as file:
            pickle.dump(params,file)
    # Save metrics locally
    if metrics is not None:
        metrics_path = os.path.join(LOCAL_REGISTRY_PATH, "metrics", timestamp + ".pickle")
        with open(metrics_path, "wb") as file:
            pickle.dump(metrics, file)

    print("✅ Results saved locally")
    return None

def save_model(model: GridSearchCV = None) -> None:
    """
    Persist trained model locally on the hard drive at f"{LOCAL_REGISTRY_PATH}/models/{timestamp}.h5"
    """

    timestamp = time.strftime("%Y%m%d-%H%M%S")

    # Save model locally
    model_path = os.path.join(LOCAL_REGISTRY_PATH, "models", f"{timestamp}.h5")
    with open(model_path, 'wb') as file:
        pickle.dump(model,file)

    print("✅ Model saved locally")
    return None

def load_model()-> GridSearchCV:
    """
    Return a saved model:
    locally (latest one in alphabetical order)
    """
    # Get the latest model version name by the timestamp on disk
    local_model_directory = os.path.join(LOCAL_REGISTRY_PATH, "models")
    local_model_paths = glob.glob(f"{local_model_directory}/*")

    if not local_model_paths:
        return None

    most_recent_model_path_on_disk = sorted(local_model_paths)[-1]

    print(Fore.BLUE + f"Load latest model from disk..." + Style.RESET_ALL)

    with open(most_recent_model_path_on_disk, 'rb') as file:
        latest_model = pickle.load(file)

    print("✅ Model loaded from local disk")

    return latest_model

def load_scaler() -> pickle:
    """
    Return a saved scaler:
    locally (latest one in alphabetical order)
    """
    local_scaler_directory = os.path.join(LOCAL_REGISTRY_PATH, "scalers")
    local_scaler_paths = glob.glob(f"{local_scaler_directory}/*")

    if not local_scaler_paths:
        return None

    print(Fore.BLUE + f"\nLoad latest scaler from disk..." + Style.RESET_ALL)

    most_recent_scaler_path_on_disk = sorted(local_scaler_paths)[-1]
    with open(most_recent_scaler_path_on_disk, 'rb') as file:
        scaler = pickle.load(file)

    print("✅ Scaler loaded from local disk\n")

    return scaler
