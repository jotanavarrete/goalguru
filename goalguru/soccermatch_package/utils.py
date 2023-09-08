import json
from goalguru.soccermatch_package.params import *
from pathlib import Path

def save_json(data:dict,
              file_path: Path):
    """
    Saves a dictionary or list into json file
    """

    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)
    return None

def read_json(file_path: Path) -> dict:
    """
    Reads a json file from a path
    """

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data
