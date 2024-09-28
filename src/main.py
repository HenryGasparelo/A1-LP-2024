import pandas as pd
import numpy as np
import manipulacao_csv as mc

# Caminho para o arquivo csv com os dados do stack overflow
caminho_arquivo = "../data/survey_results_public.csv"

# Dataframe gerado usando o csv com os dados do stack overflow
dados = mc.ler_csv(caminho_arquivo)