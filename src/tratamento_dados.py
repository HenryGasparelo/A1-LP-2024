"""MODULO DE TRATAMENTO DE DADOS"""

import pandas as pd
import numpy as np

def funcao_split(objeto: str, separador: str) -> list[str]:
    """
    Funcao que recebe uma string e um separador e retorna uma lista onde os elementos sao as parcelas da string separadas pelo separador, ou seja, aplica o metodo split ao objeto.

    Parameters
    ----------
    objeto : str
        Objeto a ser separado.
    separador : str
        Valor que ira separar as parcelas da string.

    Returns
    -------
    list[str]
        Lista onde os elementos sao as parcelas do objeto separadas pelo separador.

    """
    # Tenta aplicar o método split no objeto e retorná-lo, caso o objeto não possua o método split, retorna apenas o objeto.
    try:
        return objeto.split(separador)
    except AttributeError:
        return objeto

def tratar_coluna(dataframe: pd.core.frame.DataFrame, coluna: str, drop_faltantes: bool=False, fill_faltantes: bool=False, valor_fill=0, split_por_ponto_e_virgula: bool=False) -> pd.core.frame.DataFrame:
    """
    Funcao que recebe um dataframe, uma coluna especifica, e alguns parametros, e retorna um dataframe com os dados tratados na coluna escolhida, a partir dos parametros passados.

    Parameters
    ----------
    dataframe : pd.core.frame.DataFrame
        Dataframe a ser tratado.
    coluna : str
        Coluna escolhida para o tratamento.
    drop_faltantes : bool, optional
        Boleano que determina se os valores faltantes vao ou nao ser removidos. O padrao e False (Falso).
    fill_faltantes : bool, optional
        Boleano que determina se os valores faltantes vao ou nao ser preenchidos. O padrao e False (Falso).
    valor_fill : TYPE, optional
        Valor para preenchimento dos valores faltantes. O padrao e 0.
    split_por_ponto_e_virgula : bool, optional
        Boleano que determina se os dados vao ou nao ser separados por ponto e virgula em uma lista. O padrao e False (Falso).

    Returns
    -------
    dataframe_tratado : pd.core.frame.DataFrame
        Dataframe modificado apos cada tratamento.

    """
    # Define o novo dataframe como uma cópia do original
    dataframe_tratado: pd.core.frame.DataFrame = dataframe.copy()
    
    # Caso seja necessário remover os dados faltantes da coluna escolhida (drop_faltantes=True), então as linhas que não possuem esses dados serão removidas
    if drop_faltantes:
        dataframe_tratado = dataframe_tratado.dropna(subset=[coluna])
    # Caso seja necessário preencher os dados faltantes da coluna escolhida (fill_faltantes=True), então as cada valor faltante na coluna escolhida vai ser preenchido pelo valor passado para preenchimento
    elif fill_faltantes:
        dataframe_tratado = dataframe_tratado.fillna(subset=[coluna], value=valor_fill)
    
    # Caso os dados preisem ser separados por ponto e vírgula em uma lista, então os dados vão ser separados usando a funcao_split e substituidos no novo dataframe
    if split_por_ponto_e_virgula:
        dataframe_tratado[coluna] = dataframe_tratado[coluna].apply(funcao_split, args=";")
    
    # Retorna o dataframe tratado
    return dataframe_tratado