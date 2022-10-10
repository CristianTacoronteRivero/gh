"""
Este modulo contiene helpers para el preprocesamiento de datos
"""
import numpy as np

# import pandas as pd
















def get_numerical_feature(data_frame):
    """Resumen simple
    :param df: DataFrame
    :type df: pandas.DataFrame
    :return: Lista de nombres de columnas
    :rtype: List[str]
    example
    -------
        >>> from modeltools.preprocessing import get_numerical_feature
        >>> import pandas as pd
        >>> df = pd.DataFrame({"a":[1]})
        >>> get_numerical_feature(df)
        ['a']
    """
    return list(data_frame.select_dtypes(include=[np.number]).columns)


# def get_numerical_feature(df):
#     """Devuelve una lista con el nombre de las columnas
#     de tipo numerico!
#     Esta es con la nueva forma

#     :param df: DataFrame
#     :type df: DataFrame

#     :return: Lista de nonbres de las columnas que contiene datos numericos
#     :rtype: List[str]

#     :examples:
#         >>> from modeltools.preprocessing import get_numerical_feature
#         >>> import pandas as pd
#         >>> df = pd.DataFrame({"a":[1]})
#         >>> get_numerical_feature(df)
#         ['a']
#     """
#     return list(df.select_dtypes(include=[np.number]).columns)
