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