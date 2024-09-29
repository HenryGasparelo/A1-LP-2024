import manipulacao_csv as mc
import tratamento_dados as td
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
dados_filtrados: pd.core.frame.DataFrame = mc.filtar_colunas(dados, lista_colunas)

# EXEMPLOS DAS NOVAS FUNÇÕES
print(dados_filtrados)

dados_tratados: pd.core.frame.DataFrame = td.tratar_coluna(dados_filtrados, "LanguageWorkedWith", drop_faltantes=True, split_por_ponto_e_virgula=True)

print(dados_tratados["LanguageWorkedWith"])

