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

def analise_unidimensional(dataframe: pd.core.frame.DataFrame, coluna: str) -> dict:
    """
    Funcao que recebe um dataframe e uma coluna e retorna um dicionario com uma analise completa daquela coluna.

    Parameters
    ----------
    dataframe : pd.core.frame.DataFrame
        Dataframe com os dados.
    coluna : str
        Coluna a ser analisada.

    Returns
    -------
    dict
        Dicionario com a quantidade de elementos, media, desvio padrao, minimo, primeiro quartil, mediana, terceiro quartil e maximo entre os dados.

    """
    # Define uma serie com a coluna a ser analisada
    serie = dataframe[coluna]
    
    # Cria o dicionario com a analise
    # Define a quantidade de elementos como o comprimento da serie
    analise: dict = {"quantidade_de_elementos": len(serie),
    # Define a media como a media aritmetica calculada usando o Numpy
    "media": np.mean(serie),
    # Define o desvio padrao calculado usando o Numpy
    "desvio_padrao": np.std(serie, ddof=0),
    # Define o minimo, calculado usando o Numpy
    "minimo": np.min(serie),
    # Define o primeiro quartil, que marca os primeiros 1/4 dos dados, calculado usando o Numpy
    "primeiro_quartil": np.quantile(serie, 0.25),
    # Define a mediana, que marca metade dos dados, calculada usando o Numpy
    "mediana": np.quantile(serie, 0.5),
    # Define o terceiro quartil, que marca os primeiros 3/4 dos dados, calculado usando o Numpy
    "terceiro_quartil": np.quantile(serie, 0.75),
    # Define o maximo, calculado usando o Numpy
    "maximo": np.max(serie)}
    
    # Retorna o dicionario
    return analise

def analise_bidimensional(dataframe: pd.core.frame.DataFrame, coluna1: str, coluna2: str) -> float:
    """
    Funcao que recebe o dataframe e duas colunas e retorna o coeficiente de correlacao entre elas.

    Parameters
    ----------
    dataframe : pd.core.frame.DataFrame
        Dataframe com os dados.
    coluna1 : str
        Primeira coluna para analise.
    coluna2 : str
        Segunda coluna para analise.

    Returns
    -------
    float
        Coeficiente de correlacao calculado como a media dos produtos dos desvios de cada coluna, dividido pelo produto entre os desvios padrao.

    """
    # Cria uma copia do dataframe
    copia_dataframe: pd.core.frame.DataFrame = dataframe.copy()
    # Cria dois dicionarios com as analises de cada coluna
    analise_coluna1: dict = analise_unidimensional(copia_dataframe, coluna1)
    analise_coluna2: dict = analise_unidimensional(copia_dataframe, coluna2)
    # Define novas 2 colunas no dataframe com os desvios em relacao a media
    copia_dataframe["desvio_coluna1"] = copia_dataframe[coluna1] - analise_coluna1["media"]
    copia_dataframe["desvio_coluna2"] = copia_dataframe[coluna2] - analise_coluna2["media"]
    # Define uma nova coluna com os produtos entre os desvios
    copia_dataframe["produto_desvios"] = copia_dataframe["desvio_coluna1"] * copia_dataframe["desvio_coluna2"]
    # Define o cov, como a media desses produtos
    cov: float = np.mean(copia_dataframe["produto_desvios"])
    # Encontra o coeficiente de correlacao, dividindo o cov pelo produto entre os desvios padrao
    correlacao: float = cov / (analise_coluna1["desvio_padrao"] * analise_coluna2["desvio_padrao"])
    
    # Retorna o coeficiente de correlacao
    return correlacao