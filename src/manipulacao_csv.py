"""MÓDULO DE ORGANIZAÇÃO DO CSV"""

# Importando os módulos necessários para as funções
import pandas as pd
import numpy as np

def ler_csv(caminho: str):
    """
    Função que recebe um caminho relativo ao programa até um arquivo csv e retorna um dataframe gerado usando esse arquivo csv.

    Parameters
    ----------
    caminho : str
        Caminho para o arquivo csv.

    Returns
    -------
    dados : pandas.core.frame.DataFrame
        Dataframe gerado usando o arquivo csv encontrado utilizando o caminho.

    """
    
    # Cria um dataframe chamado dados e o retorna
    dados = pd.read_csv(caminho)
    return dados

def filtar_colunas(dataframe, lista_colunas: list):
    """
    Função que recebe um dataframe e uma lista de colunas e retorna um novo dataframe somente com as colunas da lista.

    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
        Dataframe que precisa ser filtrado.
    lista_colunas : list
        Lista de colunas que deseja no novo dataframe.

    Returns
    -------
    novo_dataframe : pandas.core.frame.DataFrame
        Dataframe filtrado, que somente possui as colunas escolhidas.

    """
    
    # Cria um novo dataframe apenas com as colunas da lista e o retorna
    novo_dataframe = dataframe[lista_colunas]
    return novo_dataframe