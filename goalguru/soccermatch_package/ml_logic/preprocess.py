from goalguru.soccermatch_package.params import *
from goalguru.soccermatch_package.ml_logic.registry import load_scaler

from colorama import Fore, Style

def scale_x(X):
    '''
    Argument: X without scalling

    Return X scaled
    '''

    scaler = load_scaler()
    print(Fore.BLUE + f"Scaling X..." + Style.RESET_ALL)
    X = scaler.transform(X)
    print("✅ X scaled correctly\n")
    return X
