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
    dataframe_hipotese1: pd.core.frame.DataFrame = pd.DataFrame(columns=["AnosCodando", "HabitosSaudaveis", "LinguagemProgramacao"])
    # Cria uma lista de todas as linguagens usadas na hipotese
    linguagens: list = ["Python", "JavaScript", "C", "Java"]
    # Cria uma lista com todos os possiveis anos codando
    lista_anos_codando: list = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 30]
    # Para cada linguagem cria um novo dataframe, com as colunas base
    for linguagem in linguagens:
            for ano_codando in lista_anos_codando:
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
                # Filtra apenas as linhas que possuem a linguagem da iteracao e o periodo codando
                dataframe_temporario = mc.filtrar_linhas_por_um_elemento_em_lista(dataframe_temporario, "LanguageWorkedWith", linguagem)
                dataframe_temporario = mc.filtrar_linhas(dataframe_temporario, "YearsCoding", ano_codando)
                # Aplica a analise unidimensional para a coluna habitos saudaveis
                analise = pv.analise_unidimensional(dataframe_temporario, "HabitosSaudaveis")
                # Define habitos saudaveis como a media dos habitos saudaveis
                habitos_saudaveis = analise["media"]
                # Define uma nova linha com o periodo codando, os habitos saudaveis e a linguagem de programacao
                nova_linha = {"AnosCodando": ano_codando, "HabitosSaudaveis": habitos_saudaveis, "LinguagemProgramacao": linguagem}
                # Coloca essa linha no dataframe
                dataframe_hipotese1.loc[len(dataframe_hipotese1)] = nova_linha
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
        # Trata os valores atipicos de salario, removendo aqueles que sao nulos, inferiores a 2400 e superiores a 600000
        dataframe_temporario = td.tratamento_valores_atipicos(dataframe_temporario, "ConvertedSalary", limite_inferior_valores=2400 ,remover_zero=True, limite_superior_valores=600000)
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

def gerar_dataframe_hipotese4(dataframe: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    """
    Funcao que recebe o dataframe principal e retorna um novo dataframe apenas com os dados que serao utilizados na hipotese 4.

    Parameters
    ----------
    dataframe : pd.core.frame.DataFrame
        Dataframe principal.

    Returns
    -------
    dataframe_hipotese4 : pd.core.frame.DataFrame
        Dataframe apenas com os dados que serao utilizados na hipotese.

    """
    # Cria um dataframe vazio apenas com as colunas que serao utilizadas
    dataframe_hipotese4: pd.core.frame.DataFrame = pd.DataFrame(columns=["EnsinoSuperior", "TipoAutoAprendizado", "QuantidadeDeLinguagens"])
    # Filtra o dataframe principal apenas com as colunas base
    dataframe_filtrado: pd.core.frame.DataFrame = mc.filtrar_colunas(dataframe, ["FormalEducation", "SelfTaughtTypes", "LanguageWorkedWith"])
    # Remove os valores faltantes
    dataframe_filtrado = dataframe_filtrado.dropna()
    # Aplica os dicionarios as colunas que precisam deste tratamento
    dataframe_filtrado = pv.modificar_dados_usando_dicionario(dataframe_filtrado, "FormalEducation", ad.dicionario_FormalEducation_hipotese4)
    # Transforma os dados em formato de lista em lista de python
    dataframe_filtrado = td.tratamento_lista_de_valores(dataframe_filtrado, "SelfTaughtTypes")
    dataframe_filtrado = td.tratamento_lista_de_valores(dataframe_filtrado, "LanguageWorkedWith")
    # Define a coluna de linguagem de programacao como o comprimento de cada lista, para conseguir analisar a quantidade de linguagens aprendidas
    dataframe_filtrado["LanguageWorkedWith"] = dataframe_filtrado["LanguageWorkedWith"].apply(len)
    # Cria listas com as diferentes formas de auto aprendizado e se possui ou nao ensino superior
    lista_formacao_superior: list = ["Nao possui ensino superior", "Possui ensino superior"]
    lista_formas_aprendizado: list = ["The official documentation and/or standards for the technology",
                                "A book or e-book from O’Reilly, Apress, or a similar publisher",
                                "Online developer communities other than Stack Overflow (ex. forums, listservs, IRC channels, etc.)",
                                "A college/university computer science or software engineering book",
                                "Internal Wikis, chat rooms, or documentation set up by my company for employees"]
    # Para cada possibilidade de formacao e de forma de auto aprendizado cria uma copia do dataframe
    for formacao in lista_formacao_superior:
        for forma_aprendizado in lista_formas_aprendizado:
            dataframe_copia: pd.core.frame.DataFrame = dataframe_filtrado.copy()
            # Filtra apenas as linhas que possuem os elementos da iteracao
            dataframe_copia = mc.filtrar_linhas_por_um_elemento_em_lista(dataframe_copia, "SelfTaughtTypes", forma_aprendizado)
            dataframe_copia = mc.filtrar_linhas(dataframe_copia, "FormalEducation", formacao)
            # Faz uma analise unidimensional da coluna de linguagem de programacao
            analise_unidimensional: dict = pv.analise_unidimensional(dataframe_copia, "LanguageWorkedWith")
            # Define a quantidade de linguagens como a media
            quantidade_de_linguagens: float = analise_unidimensional["media"]
            # Cria uma nova linha com a formacao, tipo de auto aprendizado e media de quantidade de linguagens aprendidas
            nova_linha: dict = {"EnsinoSuperior": formacao, "TipoAutoAprendizado": forma_aprendizado, "QuantidadeDeLinguagens": quantidade_de_linguagens}
            # Insere a linha no dataframe da hipotese
            dataframe_hipotese4.loc[len(dataframe_hipotese4)] = nova_linha
    # Retorna o dataframe da hipotese
    return dataframe_hipotese4
    
def gerar_dataframe_hipotese1_original(dataframe):
    # Cria um dataframe vazio apenas com as colunas que serao utilizadas
    dataframe_hipotese1_original: pd.core.frame.DataFrame = pd.DataFrame(columns=["Satisfacao", "AnosCodando", "SalarioMedio"])
    # Filtra o dataframe principal apenas com as colunas base
    dataframe_filtrado: pd.core.frame.DataFrame = mc.filtrar_colunas(dataframe, ["YearsCoding", "CareerSatisfaction", "ConvertedSalary"])
    # Remove os valores faltantes
    dataframe_filtrado = dataframe_filtrado.dropna()
    # Aplica os dicionarios as colunas que precisam deste tratamento
    dataframe_filtrado = pv.modificar_dados_usando_dicionario(dataframe_filtrado, "CareerSatisfaction", ad.dicionario_CareerSatisfaction)
    dataframe_filtrado = pv.modificar_dados_usando_dicionario(dataframe_filtrado, "YearsCoding", ad.dicionario_YearsCoding)
    # Trata os valores atipicos de salario, removendo aqueles que sao nulos, inferiores a 2400 e superiores a 600000
    dataframe_filtrado = td.tratamento_valores_atipicos(dataframe_filtrado, "ConvertedSalary", limite_inferior_valores=2400 ,remover_zero=True, limite_superior_valores=600000)
    # Cria listas com os niveis de satisfacao
    lista_niveis_satisfacao = ["Alto", "Medio", "Baixo"]
    # Lista de possiveis anos codando
    lista_anos_codando: list = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 30]
    # Para cada nivel de satisfacao e periodo codando cria uma copia do dataframe
    for nivel_satisfacao in lista_niveis_satisfacao:
        for periodo_codando in lista_anos_codando:
            dataframe_copia: pd.core.frame.DataFrame = dataframe_filtrado.copy()
            # Filtra apenas as linhas que possuem o nivel de satisfacao e o ano codando da iteracao
            dataframe_copia = mc.filtrar_linhas(dataframe_copia, "CareerSatisfaction", nivel_satisfacao)
            dataframe_copia = mc.filtrar_linhas(dataframe_copia, "YearsCoding", periodo_codando)
            # Faz uma analise unidimensional da coluna salario convertido
            analise_unidimensional: dict = pv.analise_unidimensional(dataframe_copia, "ConvertedSalary")
            # Define o salario medio como a media
            salario_medio: float = analise_unidimensional["media"]
            # Cria uma nova linha com a satisfacao, anos codando e salario medio
            nova_linha: dict = {"Satisfacao": nivel_satisfacao, "AnosCodando": periodo_codando, "SalarioMedio": salario_medio}
            # Insere a linha no dataframe da hipotese
            dataframe_hipotese1_original.loc[len(dataframe_hipotese1_original)] = nova_linha
            
    return dataframe_hipotese1_original
            
            
    