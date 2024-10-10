import manipulacao_csv as mc
import tratamento_dados as td
import preparacao_visualizacao as pv
import armazenamento_dicionarios as ad
import dataframes_hipoteses as dh
import pandas as pd

# Caminho para o arquivo csv com os dados do stack overflow
caminho_arquivo: str = "../data/survey_results_public.csv"

# Dataframe gerado usando o csv com os dados do stack overflow
dados: pd.core.frame.DataFrame = mc.ler_csv(caminho_arquivo)

# Lista de colunas que irao ser utilizadas
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
# OBS: Salario dado anualmente

# Dataframe apenas com as colunas selecionadas
dados_filtrados: pd.core.frame.DataFrame = mc.filtrar_colunas(dados, lista_colunas)

# EXEMPLOS DAS NOVAS FUNCOES

print(dh.gerar_dataframe_hipotese1(dados))
print(dh.gerar_dataframe_hipotese2(dados))
print(dh.gerar_dataframe_hipotese3(dados))