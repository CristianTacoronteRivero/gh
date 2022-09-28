"""
Este modulo contiene helpers para el preprocesamiento de datos
"""
import numpy as np
# import pandas as pd

def get_numerical_feature(df):
    return df.select_dtypes(include=[np.number]).columns