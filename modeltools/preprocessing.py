"""
Este modulo contiene helpers para el preprocesamiento de datos
"""

import numpy as np


def get_numerical_feature(data_frame):
    """Resumen simple
    :param data_frame: DataFrame
    :type data_frame: pandas.DataFrame
    :return: Lista de nombres de columnas
    :rtype: List[str]


    >>> from modeltools.preprocessing import get_numerical_feature
    >>> import pandas as pd
    >>> data_frame = pd.DataFrame({"a":[1]})
    >>> get_numerical_feature(data_frame)
    ['a']
    """
    return list(data_frame.select_dtypes(include=[np.number]).columns)
