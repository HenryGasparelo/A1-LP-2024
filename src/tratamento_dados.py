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
    # Tenta aplicar o metodo split no objeto e retorna-lo, caso o objeto não possua o metodo split, retorna apenas o objeto.
    try:
        return objeto.split(separador)
    except AttributeError:
        return objeto

def tratamento_valores_faltantes(dataframe: pd.core.frame.DataFrame, coluna: str, drop_faltantes: bool=False, fill_faltantes: bool=False, valor_fill=0) -> pd.core.frame.DataFrame:
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

    Returns
    -------
    dataframe_tratado : pd.core.frame.DataFrame
        Dataframe modificado apos cada tratamento.

    """
    # Define o novo dataframe como uma copia do original
    dataframe_tratado: pd.core.frame.DataFrame = dataframe.copy()
    
    # Caso seja necessario remover os dados faltantes da coluna escolhida (drop_faltantes=True), entao as linhas que nao possuem esses dados serao removidas
    if drop_faltantes:
        dataframe_tratado = dataframe_tratado.dropna(subset=[coluna])
    # Caso seja necessario preencher os dados faltantes da coluna escolhida (fill_faltantes=True), entao cada valor faltante na coluna escolhida vai ser preenchido pelo valor passado para preenchimento
    elif fill_faltantes:
        dataframe_tratado = dataframe_tratado.fillna(subset=[coluna], value=valor_fill)
    
    # Retorna o dataframe tratado
    return dataframe_tratado

def tratamento_valores_atipicos(dataframe: pd.core.frame.DataFrame, coluna: str, limite_inferior_valores: int|float=(-1)*np.inf, remover_zero: bool=False, limite_superior_valores: int|float=np.inf) -> pd.core.frame.DataFrame:
    """
    Funcao que recebe um dataframe e uma coluna especifica e retorna um novo dataframe que possui apenas as linhas que respeitam os limites e condicoes passadas na coluna escolhida.

    Parameters
    ----------
    dataframe : pd.core.frame.DataFrame
        Dataframe a ser tratado.
    coluna : str
        Coluna escolhida para o tratamento.
    limite_inferior_valores : int|float, optional
        Limite inferior, todos os dados retornados serao maiores ou iguais a ele. O padrao e (-1)*np.inf (infinito negativo).
    remover_zero : bool, optional
        Boleano que determina se os valores iguais a 0 serao ou nao removidos. O padrao e False (Falso).
    limite_superior_valores : int|float, optional
        Limite superior, todos os dados retornados serao menores ou iguais a ele. O padrao e np.inf (infinito positivo).

    Returns
    -------
    dataframe_tratado : TYPE
        Dataframe tratado, onde em cada linha, os valores na coluna espicifica respeitam as condicoes e limites passados.

    """
    # Define o novo dataframe como uma copia do original
    dataframe_tratado: pd.core.frame.DataFrame = dataframe.copy()
    
    # Se for necessario remover os valores zerados, filtra apenas os valores nao nulos.
    if remover_zero:
        dataframe_tratado = dataframe_tratado[dataframe_tratado[coluna] != 0]
    
    # Independente da remocao ou nao dos valores nulos, filtra apenas os valores que sao maiores ou iguais ao limite inferior e menores ou iguais as limite superior.
    dataframe_tratado = dataframe_tratado[(dataframe_tratado[coluna] >= limite_inferior_valores) & (dataframe_tratado[coluna] <= limite_superior_valores)]

    # Redefine os indices do dataframe tratado (alteracao por isaias)
    dataframe_tratado = dataframe_tratado.reset_index(drop=True)
    
    # Retorna o dataframe tratado
    return dataframe_tratado

def tratamento_lista_de_valores(dataframe: pd.core.frame.DataFrame, coluna: str) -> pd.core.frame.DataFrame:
    """
    Funcao que recebe um dataframe e coluna, e separa os elementos de cada linha dessa coluna em uma lista, onde o separador e ponto e virgula.

    Parameters
    ----------
    dataframe : pd.core.frame.DataFrame
        Dataframe a ser tratado.
    coluna : str
        Coluna na qual estao os dados a serem tratados.

    Returns
    -------
    dataframe_tratado : pd.core.frame.DataFrame
        Dataframe modificado apos a separacao em lista de cada elemento da coluna escolhida.

    """
    # Define o novo dataframe como uma copia do original
    dataframe_tratado: pd.core.frame.DataFrame = dataframe.copy()
    
    # Caso os dados precisem ser separados por ponto e virgula em uma lista, entao os dados vao ser separados usando a funcao_split e substituidos no novo dataframe
    dataframe_tratado[coluna] = dataframe_tratado[coluna].apply(funcao_split, args=";")
    
    # Retorna o dataframe tratado
    return dataframe_tratado
