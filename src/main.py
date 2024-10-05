import manipulacao_csv as mc
import tratamento_dados as td
import preparacao_visualizacao as pv
import armazenamento_dicionarios as ad
import pandas as pd

# Caminho para o arquivo csv com os dados do stack overflow
caminho_arquivo: str = "../data/survey_results_public.csv"

# Dataframe gerado usando o csv com os dados do stack overflow
dados: pd.core.frame.DataFrame = mc.ler_csv(caminho_arquivo)

# Lista de colunas que irão ser utilizadas
lista_colunas: list[str] = ["Student", 
                 "Employment", 
                 "FormalEducation", 
                 "UndergradMajor",
                 "Respondent",
                 "YearsCoding", 
                 "JobSatisfaction",
                 "CareerSatisfaction",
                 "JobSearchStatus",
                 "LastNewJob",
                 "UpdateCV",
                 "ConvertedSalary",
                 "SelfTaughtTypes",
                 "LanguageWorkedWith",
                 "OperatingSystem",
                 "HoursComputer",
                 "HoursOutside",
                 "SkipMeals",
                 "Exercise",
                 "Age"]
# OBS: Salário dado anualmente

# Dataframe apenas com as colunas selecionadas
dados_filtrados: pd.core.frame.DataFrame = mc.filtrar_colunas(dados, lista_colunas)

# EXEMPLOS DAS NOVAS FUNÇÕES
print(dados_filtrados)

dados_tratados: pd.core.frame.DataFrame = td.tratamento_valores_faltantes(dados_filtrados, "YearsCoding", drop_faltantes=True)
dados_tratados: pd.core.frame.DataFrame = td.tratamento_valores_faltantes(dados_tratados, "LanguageWorkedWith", drop_faltantes=True)
dados_tratados: pd.core.frame.DataFrame = td.tratamento_lista_de_valores(dados_tratados, "LanguageWorkedWith")
dados_tratados: pd.core.frame.DataFrame = td.tratamento_valores_faltantes(dados_tratados, "ConvertedSalary", drop_faltantes=True)
dados_tratados: pd.core.frame.DataFrame = td.tratamento_valores_atipicos(dados_tratados, "ConvertedSalary", remover_zero=True, limite_superior_valores=2400000)

print(dados_tratados["YearsCoding"])
print(dados_tratados["LanguageWorkedWith"])
print(dados_tratados["ConvertedSalary"])

dados_tratados: pd.core.frame.DataFrame = td.tratamento_valores_faltantes(dados_tratados, "CareerSatisfaction", drop_faltantes=True)
dados_modificados: pd.core.frame.DataFrame = pv.modificar_dados_usando_dicionario(dados_tratados, "CareerSatisfaction", ad.dicionario_CareerSatisfaction)

print(dados_modificados["CareerSatisfaction"])

dataframe_filtrado = mc.filtrar_linhas(dados, "Employment", 'Employed part-time', 'Employed full-time', "Independent contractor, freelancer, or self-employed")
print(dataframe_filtrado["Employment"]) 

print(pv.analise_unidimensional(dados_tratados, "ConvertedSalary"))
coeficiente_de_correlacao = pv.analise_bidimensional(dados_modificados, "ConvertedSalary", "CareerSatisfaction")
print(coeficiente_de_correlacao)

dados_tratados: pd.core.frame.DataFrame = td.tratamento_valores_faltantes(dados_tratados, "HoursComputer", drop_faltantes=True)
dados_tratados: pd.core.frame.DataFrame = pv.modificar_dados_usando_dicionario(dados_tratados, "HoursComputer", ad.dicionario_HoursComputer)
dados_tratados: pd.core.frame.DataFrame = td.tratamento_valores_faltantes(dados_tratados, "HoursOutside", drop_faltantes=True)
dados_tratados: pd.core.frame.DataFrame = pv.modificar_dados_usando_dicionario(dados_tratados, "HoursOutside", ad.dicionario_HoursOutside)
dados_tratados: pd.core.frame.DataFrame = td.tratamento_valores_faltantes(dados_tratados, "SkipMeals", drop_faltantes=True)
dados_tratados: pd.core.frame.DataFrame = pv.modificar_dados_usando_dicionario(dados_tratados, "SkipMeals", ad.dicionario_SkipMeals)
dados_tratados: pd.core.frame.DataFrame = td.tratamento_valores_faltantes(dados_tratados, "Exercise", drop_faltantes=True)
dados_tratados: pd.core.frame.DataFrame = pv.modificar_dados_usando_dicionario(dados_tratados, "Exercise", ad.dicionario_Exercise)
dados_tratados = pv.criar_coluna_habitos_saudaveis(dados_tratados)
print(dados_tratados["HabitosSaudaveis"])
print(pv.calcular_empregabilidade(dados))