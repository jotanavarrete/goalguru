import numpy as np
import pandas as pd

from colorama import Fore, Style

from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer # make_column_transformer
#from sklearn.preprocessing import OneHotEncoder, FunctionTransformer



def preprocess_df(X: pd.DataFrame) -> np.ndarray:

    def create_preprocessor() -> ColumnTransformer:
        """
        La idea de esta funcion, es crear el pipeline que preprocese todo
        el dataframe. Para que luego al aplicar el fit_transform(X)
        Entregue el dataframe.

        Create your OWN.
        """
        list_of_features=['A','B','C']

        pipeline_1= make_pipeline()
        pipeline_2= make_pipeline()
        pipeline_3= make_pipeline()

        # COMBINED PREPROCESSOR
        final_preprocessor = ColumnTransformer(
            [
                ("name1_preproc", pipeline_1, ["column_name_1"]),
                ("name2_preproc", pipeline_2, ["column_name_2"]),
                ("name2_preproc", pipeline_3, list_of_features),
            ],
            n_jobs=-1,
        )

        return final_preprocessor



    print(Fore.BLUE + "\nPreprocessing features..." + Style.RESET_ALL)

    preprocessor = create_preprocessor()
    X_processed = preprocessor.fit_transform(X)

    print("✅ X_processed, with shape", X_processed.shape)

    return X_processed
