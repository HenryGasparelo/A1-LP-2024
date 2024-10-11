import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys

# Para poder importar o módulo a partir do diretório '../src'
sys.path.append('../src')

import manipulacao_csv as mc
import tratamento_dados as td
import preparacao_visualizacao as pv
import armazenamento_dicionarios as ad
import dataframes_hipoteses as dh

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

def plotar_h1(dataframe):
    # Estilo do fundo 
    sns.set_theme(style="whitegrid")

    # Gerar DataFrame usando a função personalizada
    df = pd.DataFrame(dh.gerar_dataframe_hipotese1(dados))

    # Usar pivot_table para agregar valores duplicados (por exemplo, usando a média)
    df_p = df.pivot_table(index="AnosCodando", columns="LinguagemProgramacao", values="HabitosSaudaveis", aggfunc="mean")

    # Inverter os anos
    df_p = df_p.sort_index(ascending=False)

    # Criar o heatmap
    f, ax = plt.subplots(figsize=(9, 6))
    sns.heatmap(df_p, annot=True, fmt=".2f", cmap="magma", ax=ax)

    # Definir os rótulos dos eixos
    plt.xlabel("Linguagens Usadas", labelpad=17)
    plt.ylabel("Anos Codando", labelpad=17)

    # Adicionar uma caixa de texto explicando o índice
    plt.text(1.0, 1.05, "Índice de Hábitos Saudáveis",
            transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.6))



    # Mostrar o gráfico
    plt.tight_layout()
    plt.show()

#Teste 1
#plotar_h1(dados)


def plotar_h2(dataframe):
    #Estilo de Fundo
    sns.set_theme(style="whitegrid")

    # Carregar o dataset
    df = pd.DataFrame(dh.gerar_dataframe_hipotese2(dados))

    # Criar o gráfico
    g = sns.lmplot(
        data=df,
        x="PeriodoCodando", y="Salario", hue="LinguagemProgramacao",
        height=8, palette="tab10"
    )

    # Alterar o título da legenda (índice do hue)
    g._legend.set_title("Linguagens", prop={'size': 15})  # Tamanho do título

    #plt.legend(title="Linguagens", title_fontsize=15, fontsize=13)

    # Ajustar os rótulos dos eixos
    plt.xlabel("Período Codando (Anos)", labelpad=20)
    plt.ylabel("Salário (USD por Ano)", labelpad=20)

    # Exibir o gráfico
    plt.show()

#teste 2
#plotar_h2(dados)


def plotar_h3(dataframe):
    # Definir o tema e estilo do gráfico
    sns.set_theme(style="whitegrid")

    # Criar um DataFrame a partir dos dados
    df = pd.DataFrame(dh.gerar_dataframe_hipotese3(dados))

    # Definir uma paleta personalizada
    paleta_linda_hex = ['#DCD301', '#DC0701', '#001EDB', '#C800DB', '#00DBA3', '#BD7200']

    # Criar o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definir o tamanho da figura
    sns.lineplot(data=df, x="AnosCodando", y="Empregabilidade", hue="NiveisEducacionais", palette=paleta_linda_hex)


    # Adicionar títulos e rótulos com espaçamento personalizado
    plt.xlabel("Anos Codando", labelpad=15)  # Espaçamento do rótulo do eixo X
    plt.ylabel("Empregabilidade", labelpad=15)  # Espaçamento do rótulo do eixo Y

    # Ajustar o tamanho e a posição da legenda (hue)
    plt.legend(title="Níveis Educacionais", title_fontsize=14, fontsize=12, loc="lower center")

    # Mostrar o gráfico
    plt.show()

#Teste
#plotar_h3(dados)

def plotar_h4(dataframe):
    sns.set_theme(style="whitegrid")

    # Carregar o dataframe
    df = pd.DataFrame(dh.gerar_dataframe_hipotese1_original(dados))

    # Paleta personalizada
    paleta_linda_hex = ['#DCD301', '#DC0701', '#001EDB']

    # Criar o gráfico de linhas empilhadas com marcadores
    d = sns.lineplot(
        data=df,
        x="AnosCodando", y="SalarioMedio", hue="Satisfacao", style="Satisfacao",
        markers=True, dashes=False, palette=paleta_linda_hex
    )

    # Ajustar os rótulos dos eixos
    plt.xlabel("Anos Codando", labelpad=17)
    plt.ylabel("Salário Médio Anual", labelpad=17)

    # Personalizar o título da legenda
    d.legend(title="Nível de Satisfação", title_fontsize='13', loc='best')

    # Exibir o gráfico
    plt.show()


#teste
#plotar_h4(dados)
