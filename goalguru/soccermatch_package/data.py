"""
IMPORTANTE:
Esta Seccion es para crear funciones de limpieza de datos,
extraccion de datos, y subir datos (si es necesario)
Haya que construirlas, pero estas necesitan big Query.
"""

import pandas as pd

from colorama import Fore, Style
from pathlib import Path

from goalguru.params import *


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw data by
    - assigning correct dtypes to each column
    - removing buggy or irrelevant transactions
    """
    pass ## insert code here

    print("✅ data cleaned")

    return df


def get_data_with_cache(
        gcp_project:str,
        query:str,
        cache_path:Path,
        data_has_header=True
    ) -> pd.DataFrame:
    """
    Retrieve `query` data from BigQuery, or from `cache_path` if the file exists
    Store at `cache_path` if retrieved from BigQuery for future use
    """
    pass ## insert code here

    #print(f"✅ Data loaded, with shape {df.shape}")

    #return df


def load_data_to_bq(
        data: pd.DataFrame,
        gcp_project:str,
        bq_dataset:str,
        table: str,
        truncate: bool
    ) -> None:
    """
    - Save the DataFrame to BigQuery
    - Empty the table beforehand if `truncate` is True, append otherwise
    """

    # Load data onto full_table_name

    # 🎯 HINT for "*** TypeError: expected bytes, int found":
    # After preprocessing the data, your original column names are gone (print it to check),
    # so ensure that your column names are *strings* that start with either
    # a *letter* or an *underscore*, as BQ does not accept anything else

    pass  # YOUR CODE HERE

    print(f"✅ Data saved to bigquery, with shape {data.shape}")
