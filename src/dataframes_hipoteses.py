import pandas as pd
import numpy as np
import preparacao_visualizacao as pv
import manipulacao_csv as mc
import tratamento_dados as td
import armazenamento_dicionarios as ad

def gerar_dataframe_hipotese1(dataframe: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    """
    Funcao que recebe o dataframe principal e retorna um novo dataframe apenas com os dados que serao utilizados na hipotese 1.

    Parameters
    ----------
    dataframe : pd.core.frame.DataFrame
        Dataframe principal.

    Returns
    -------
    dataframe_hipotese1 : pd.core.frame.DataFrame
        Dataframe apenas com os dados que serao utilizados.

    """
    # Cria um dataframe vazio apenas com os nomes das colunas que serao utilizadas na hipotese
    dataframe_hipotese1: pd.core.frame.DataFrame = pd.DataFrame(columns=["YearsCoding", "HabitosSaudaveis", "LinguagemProgramacao"])
    # Cria uma lista de todas as linguagens usadas na hipotese
    linguagens: list = ["Python", "JavaScript", "C", "Java"]
    # Para cada linguagem cria um novo dataframe, com as colunas base
    for linguagem in linguagens:
        dataframe_temporario: pd.core.frame.DataFrame = mc.filtrar_colunas(dataframe, ["LanguageWorkedWith", "HoursComputer","HoursOutside","SkipMeals","Exercise", "YearsCoding"])
        # Remove os valores faltantes
        dataframe_temporario = dataframe_temporario.dropna()
        # Transforma as listas de linguagens de programacao em listas de python
        dataframe_temporario = td.tratamento_lista_de_valores(dataframe_temporario, "LanguageWorkedWith")
        # Aplica os valores dos dicionario para cada coluna que precisa de tratamento
        dataframe_temporario = pv.modificar_dados_usando_dicionario(dataframe_temporario, "HoursComputer", ad.dicionario_HoursComputer)
        dataframe_temporario = pv.modificar_dados_usando_dicionario(dataframe_temporario, "HoursOutside", ad.dicionario_HoursOutside)
        dataframe_temporario = pv.modificar_dados_usando_dicionario(dataframe_temporario, "SkipMeals", ad.dicionario_SkipMeals)
        dataframe_temporario = pv.modificar_dados_usando_dicionario(dataframe_temporario, "Exercise", ad.dicionario_Exercise)
        dataframe_temporario = pv.modificar_dados_usando_dicionario(dataframe_temporario, "YearsCoding", ad.dicionario_YearsCoding)
        # Cria a coluna de Habitos Saudaveis
        dataframe_temporario = pv.criar_coluna_habitos_saudaveis(dataframe_temporario)
        # Filtra apenas as linhas que possuem a linguagem da iteracao
        dataframe_temporario = mc.filtrar_linhas_por_um_elemento_em_lista(dataframe_temporario, "LanguageWorkedWith", linguagem)
        # Define uma nova coluna com a linguagem
        dataframe_temporario["LinguagemProgramacao"] = linguagem
        # Filtra apenas as linhas que serao utilizadas na hipotese
        dataframe_temporario = mc.filtrar_colunas(dataframe_temporario, ["YearsCoding", "HabitosSaudaveis", "LinguagemProgramacao"])
        # Fundi o dataframe da linguagem com o principal
        dataframe_hipotese1 = pd.merge(dataframe_hipotese1, dataframe_temporario, how="outer")
    # Retorna o dataframe da hipotese
    return dataframe_hipotese1

def gerar_dataframe_hipotese2(dataframe: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    """
    Funcao que recebe o dataframe principal e retorna um novo dataframe apenas com os dados que serao utilizados na hipotese 2.

    Parameters
    ----------
    dataframe : pd.core.frame.DataFrame
        Dataframe principal.

    Returns
    -------
    dataframe_hipotese2 : pd.core.frame.DataFrame
        Dataframe apenas com os dados que serao utilizados na hipotese.

    """
    # Cria um novo dataframe, sem dados, apenas com as colunas que serao usadas na hipotese
    dataframe_hipotese2: pd.core.frame.DataFrame = pd.DataFrame(columns=["YearsCoding", "ConvertedSalary", "LinguagemProgramacao"])
    # Cria uma lista com as linguagens de programacao a serem analisadas
    linguagens: list = ["Python", "JavaScript", "C", "Java"]
    # Para cada linguagem cria um dataframe apenas com as coluna base
    for linguagem in linguagens:
        dataframe_temporario: pd.core.frame.DataFrame = mc.filtrar_colunas(dataframe, ["LanguageWorkedWith", "YearsCoding", "ConvertedSalary"])
        # Remove os valores faltantes
        dataframe_temporario = dataframe_temporario.dropna()
        # Trata as listas de linguagens para listas em python
        dataframe_temporario = td.tratamento_lista_de_valores(dataframe_temporario, "LanguageWorkedWith")
        # Aplica o respectivo dicionario a coluna que precisa ser tratada
        dataframe_temporario = pv.modificar_dados_usando_dicionario(dataframe_temporario, "YearsCoding", ad.dicionario_YearsCoding)
        # Trata os valores atipicos de salario, removendo aqueles que sao nulos ou superiores a 2400000
        dataframe_temporario = td.tratamento_valores_atipicos(dataframe_temporario, "ConvertedSalary",remover_zero=True, limite_superior_valores=2400000)
        # Filtra apenas as linhas que possuem a linguagem da iteracao
        dataframe_temporario = mc.filtrar_linhas_por_um_elemento_em_lista(dataframe_temporario, "LanguageWorkedWith", linguagem)
        # Define uma nova coluna com a linguagem
        dataframe_temporario["LinguagemProgramacao"] = linguagem
        # Filtra apenas as linhas que serao utilizadas na hipotese
        dataframe_temporario = mc.filtrar_colunas(dataframe_temporario, ["YearsCoding", "ConvertedSalary", "LinguagemProgramacao"])
        # Fundi o dataframe da linguagem com o principal
        dataframe_hipotese2 = pd.merge(dataframe_hipotese2, dataframe_temporario, how="outer")
    # Retorna o dataframe da hipotese
    return dataframe_hipotese2



