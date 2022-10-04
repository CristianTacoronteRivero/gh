"""
Este modulo contiene helpers para el preprocesamiento de datos
"""
import numpy as np
# import pandas as pd

def get_numerical_feature(df):
    """Devuelve una lista con el nombre de las columnas
    de tipo numerico

    Args:
        df (DataFrame): Objeto DataFrame

    Returns:
        list: Lista de nonbres de las columnas que contiene datos numericos

    Examples:
        >>> from modeltools.preprocessing import get_numerical_feature
        >>> import pandas as pd
        >>> df = pd.DataFrame({"a":[1]})
        >>> get_numerical_feature(df)
        ['a']
    """
    return list(df.select_dtypes(include=[np.number]).columns)