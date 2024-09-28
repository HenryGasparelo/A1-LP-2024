import pandas as pd
import numpy as np
import manipulacao_csv as mc

# Caminho para o arquivo csv com os dados do stack overflow
caminho_arquivo = "../data/survey_results_public.csv"

# Dataframe gerado usando o csv com os dados do stack overflow
dados = mc.ler_csv(caminho_arquivo)

# Lista de colunas que irão ser utilizadas
lista_colunas = ["Student", 
                 "Employment", 
                 "FormalEducation", 
                 "UndergradMajor",
                 "DevType",
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
dados_filtrados = mc.filtar_colunas(dados, lista_colunas)