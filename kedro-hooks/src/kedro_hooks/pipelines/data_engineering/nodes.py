"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.2
"""
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def add_data() -> pd.DataFrame:
    """Adding iris data from sklearn package"""
    iris = load_iris()
    df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])
    return df