import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd


def load_df():
    file_path = "Country-data.csv"
    kaggle_path = "rohan0301/unsupervised-learning-on-country-data"

    df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        kaggle_path,
        file_path,
    )
    return df


