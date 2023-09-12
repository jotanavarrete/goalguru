from sklearn.preprocessing import RobustScaler
from goalguru.soccermatch_package.ml_logic.data import load_processed_data
from goalguru.soccermatch_package.params import *

def scale_x(X):
    '''
    Argument: X without scalling

    Return X scaled
    '''
    data_processed = load_processed_data()

    x_processed = data_processed[FEATURES]

    scaler = RobustScaler()
    scaler.fit_transform(x_processed)

    X = scaler.transform(X)

    return X
