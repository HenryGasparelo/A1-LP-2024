"""MODULO DE ORGANIZACAO DO CSV"""

# Importando os modulos necessarios para as funcoes
import pandas as pd
import numpy as np

def ler_csv(caminho: str) -> pd.core.frame.DataFrame: 
    """
    Funcao que recebe um caminho relativo ao programa ate um arquivo csv e retorna um dataframe gerado usando esse arquivo csv.

    Parameters
    ----------
    caminho : str
        Caminho para o arquivo csv.

    Returns
    -------
    dados : pd.core.frame.DataFrame
        Dataframe gerado usando o arquivo csv encontrado utilizando o caminho.

    """
    
    # Cria um dataframe chamado dados e o retorna
    dados: pd.core.frame.DataFrame = pd.read_csv(caminho)
    return dados

def filtrar_colunas(dataframe: pd.core.frame.DataFrame, lista_colunas: list[str]) -> pd.core.frame.DataFrame:
    """
    Funcao que recebe um dataframe e uma lista de colunas e retorna um novo dataframe somente com as colunas da lista.

    Parameters
    ----------
    dataframe : pd.core.frame.DataFrame
        Dataframe que precisa ser filtrado.
    lista_colunas : list
        Lista de colunas que deseja no novo dataframe.

    Returns
    -------
    novo_dataframe : pd.core.frame.DataFrame
        Dataframe filtrado, que somente possui as colunas escolhidas.

    """
    
    # Cria um novo dataframe apenas com as colunas da lista e o retorna
    novo_dataframe: pd.core.frame.DataFrame = dataframe[lista_colunas]
    return novo_dataframe

def filtrar_linhas(dataframe: pd.core.frame.DataFrame, coluna_filtro: str, *args) -> pd.core.frame.DataFrame:
    """
    Funcao que recebe um dataframe, uma coluna especifica e elementos, e retorna um novo dataframe apenas com as linhas que possuem os elementos na coluna especifica.

    Parameters
    ----------
    dataframe : pd.core.frame.DataFrame
        Dataframe a ser filtrado.
    coluna_filtro : str
        Coluna especifica.
    *args : TYPE
        Elementos que serao procurados.

    Returns
    -------
    novo_dataframe : TYPE
        Dataframe filtrado apenas com as linhas que possuem os elementos na coluna especifica.

    """
    # Cria um novo dataframe que tem apenas as linhas que possuem o primeiro do elemento na coluna especifica
    novo_dataframe:pd.core.frame.DataFrame = dataframe[dataframe[coluna_filtro] == args[0]]
    # Se tiver mais de um elemento
    if len(args) > 1:
        # Para cada elemento, pega o dataframe que tem apenas as linhas que possuem aquele elemento na coluna especifica
        for elemento_filtro in args[1:]:
            dataframe_filtrado: pd.core.frame.DataFrame = dataframe[dataframe[coluna_filtro] == elemento_filtro]
            # Funde esse dataframe com o dataframe a ser retornado
            novo_dataframe = pd.merge(novo_dataframe, dataframe_filtrado, how="outer")
        
    # Retorna o dataframe filtrado
    return novo_dataframe

def filtrar_linhas_por_um_elemento_em_lista(dataframe:pd.core.frame.DataFrame, coluna: str, elemento_filtro: str) -> pd.core.frame.DataFrame:
    """
    Funcao que recebe um dataframe e uma coluna, onde cada elemento e uma lista, e retorna um novo dataframe apenas com as linhas que possuem o elemento do filtro.

    Parameters
    ----------
    dataframe : pd.core.frame.DataFrame
        Dataframe a ser filtrado.
    coluna : str
        Coluna escolhida.
    elemento_filtro : str
        Elemento escolhido para o filtro.

    Returns
    -------
    pd.core.frame.DataFrame
        Novo dataframe que possui somente as linhas que possuem o elemento escolhido para o filtro.

    """
    def verificar_pertencimento(lista:list) -> bool:
        """
        Verifica se uma lista possui um elemento.

        Parameters
        ----------
        lista : list
            Lista a ser verificada.

        Returns
        -------
        bool
            Retorna True se o elemento estiver na lista e False se nao estiver.

        """
        # Retorna True se o elemento estiver na lista e False se nao estiver
        return elemento_filtro in lista
    # Cria uma copia do dataframe original
    novo_dataframe: pd.core.frame.DataFrame = dataframe.copy()
    # Cria um novo dataframe apenas com as linhas que possuem o elemento do filtro, verificando na coluna se as listas tem esse elemento
    novo_dataframe: pd.core.frame.DataFrame = novo_dataframe[novo_dataframe[coluna].apply(verificar_pertencimento)]
    # Retorna o dataframe filtrado
    return novo_dataframe