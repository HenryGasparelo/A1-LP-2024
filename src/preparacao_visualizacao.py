"""MODULO DE PREPARACAO DE DADOS PARA VISUALIZACAO"""

import pandas as pd
import numpy as np

def aplicar_dicionario(key: str, dicionario: dict):
    """
    Funcao que recebe uma chave e um dicionario, e retorna o valor correspondente.

    Parameters
    ----------
    key : str
        Chave do dicionario.
    dicionario : dict
        Dicionario.

    Returns
    -------
    TYPE
        Valor atribuido a chave naquele dicionario.

    """
    # Retorna o valor da chave no dicionário
    return dicionario[key]

def modificar_dados_usando_dicionario(dataframe: pd.core.frame.DataFrame, coluna: str, dicionario: dict) -> pd.core.frame.DataFrame:
    """
    Funcao que recebe um dataframe, uma coluna e um dicionario, e retorna um novo dataframe, onde cada elemento da coluna e o valor do dicionario do elemento original.

    Parameters
    ----------
    dataframe : pd.core.frame.DataFrame
        Dataframe original.
    coluna : str
        Coluna escolhida para modificacao.
    dicionario : dict
        Dicionario que modificara a coluna.

    Returns
    -------
    dataframe_modificado : pd.core.frame.DataFrame
        Dataframe modificado, onde cada elemento da coluna escolhida e o valor do dicionario do elemento original.

    """
    # Cria uma cópia do dataframe original
    dataframe_modificado: pd.core.frame.DataFrame = dataframe.copy()
    # Aplica em cada elemento da coluna escolhida a função aplicar_dicionario, dicionario dentro de uma tupla para que não seja desempacotado
    dataframe_modificado[coluna] = dataframe_modificado[coluna].apply(aplicar_dicionario, args=(dicionario,))
    # Retorna o dicionário modificado
    return dataframe_modificado