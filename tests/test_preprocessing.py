from ast import Index
import pandas as pd
from modeltools.preprocessing import get_numerical_feature

def test_get_numerical_feature():
    """En estet test vamos a progar que logra distinguir
    entre cadenas de texto y numeros enteros
    """

    df = pd.DataFrame({
        "numerica": [5],
        "categorical": ["rojo"]
        })

    # assert es "como un if" pero que falla si la condicion es falsa. Esto es ideal para los tests
    assert get_numerical_feature(df) == ["numerica"]

def test_get_numerical_feature_empty():
    """Este test comprueba que se devuelve una lista vacía si no hay
    ninguna variable numerica
    """

    df = pd.DataFrame({
        "categorical": ["rojo"]
        })

    assert get_numerical_feature(df) == []

# def test_get_numerical_features_zero_columns():
#     """Este test comprueba que se devuelve una lista vacía
#     si el dataframe no tiene ninguna columna."""

#     df = pd.DataFrame([])

#     assert test_get_numerical_feature(df) == []


def test_get_numerical_features_zero_rows():
    """Este test comprueba que se devuelve una una variable si el DF
    tiene una variable numérica pero NINGUNA FILA."""

    df = pd.DataFrame({
        "numerica": pd.Series(dtype=int)
    })

    assert get_numerical_feature(df) == ["numerica"]

def test_get_numerical_features_int_and_float():
    """Este test comprueba que funciona correctamente
    cuando hay una columna integer y una flotante"""

    df = pd.DataFrame({
        "numerica": [5],
        "numerica_2": [3.4]
        })

    assert get_numerical_feature(df) == ["numerica", "numerica_2"]

# def test_get_numerical_features_complex():
#     """Este test comprueba que funciona correctamente con número complejos."""

#     df = pd.DataFrame({
#         "compleja": [complex(3,5)]
#     })

#     assert get_numerical_feature(df) == ["comleja"]


def test_get_numerical_features_columns_withoutname():
    """Este test comprueba que funciona correctamente
    cuando hay columnas numéricas sin nombre (columnas
    con numeros/posiciones)"""

    df = pd.DataFrame([
        [1, "a"]
    ])