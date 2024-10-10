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

def gerar_dataframe_hipotese3(dataframe: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    """
    Funcao que recebe o dataframe principal e retorna um novo dataframe apenas com os dados que serao utilizados na hipotese 3.

    Parameters
    ----------
    dataframe : pd.core.frame.DataFrame
        Dataframe principal.

    Returns
    -------
    dataframe_hipotese3 : pd.core.frame.DataFrame
        Dataframe apenas com os dados que serao utilizados na hipotese.

    """
    # Cria um dataframe vazio apenas com as colunas que serao utilizadas
    dataframe_hipotese3: pd.core.frame.DataFrame = pd.DataFrame(columns=["NiveisEducacionais", "AnosCodando", "Empregabilidade"])
    # Filtra o dataframe principal apenas com as colunas base
    dataframe_filtrado: pd.core.frame.DataFrame = mc.filtrar_colunas(dataframe, ["FormalEducation", "YearsCoding", "Employment"])
    # Remove os valores faltantes
    dataframe_filtrado = dataframe_filtrado.dropna()
    # Aplica os dicionarios as colunas que precisam deste tratamento
    dataframe_filtrado = pv.modificar_dados_usando_dicionario(dataframe_filtrado, "YearsCoding", ad.dicionario_YearsCoding)
    dataframe_filtrado = pv.modificar_dados_usando_dicionario(dataframe_filtrado, "FormalEducation", ad.dicionario_FormalEducation_hipotese3)
    # Cria listas com os possiveis niveis educacionais e com os anos codando
    lista_niveis_educacionais: list = ["Sem educacao formal", "Educacao basica", "Graduacao", "Mestrado", "Doutorado profissional", "Doutorado"]
    lista_anos_codando: list = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 30]
    # Para cada nivel educacional e ano codando cria uma copia do dataframe
    for nivel_educacional in lista_niveis_educacionais:
        for ano_codando in lista_anos_codando:
            dataframe_copia: pd.core.frame.DataFrame = dataframe_filtrado.copy()
            # Filtra apenas as linhas que possuem o nivel educacional e o ano codando da iteracao
            dataframe_copia = mc.filtrar_linhas(dataframe_copia, "FormalEducation", nivel_educacional)
            dataframe_copia = mc.filtrar_linhas(dataframe_copia, "YearsCoding", ano_codando)
            # Calcula a empregabilidade do dataframe filtrado
            empregabilidade: float = pv.calcular_empregabilidade(dataframe_copia)
            # Define uma nova linha com o nivel educacional e o ano codando da iteracao e a empregabilidade
            nova_linha: dict = {"NiveisEducacionais": nivel_educacional, "AnosCodando": ano_codando, "Empregabilidade": empregabilidade}
            # Coloca essa linha no dataframe da hipotese
            dataframe_hipotese3.loc[len(dataframe_hipotese3)] = nova_linha
    # Retorna o dataframe da hipotese
    return dataframe_hipotese3