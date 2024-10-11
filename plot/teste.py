import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys

# Para poder importar o módulo a partir do diretório '../src'
sys.path.append('../src')

import dataframes_hipoteses as dh
import main as mn

"""
# Definir o tema e contexto corretamente
sns.set_theme(context="notebook", style="whitegrid")

# Criar um DataFrame a partir dos dados
df = pd.DataFrame(dh.gerar_dataframe_hipotese4(mn.dados))

# Mapeamento de rótulos originais para letras
label_mapping = {
    'The official documentation and/or standards for the technology': 'a',
    'A book or e-book from O’Reilly, Apress, or a similar publisher': 'b',
    'Online developer communities other than Stack Overflow (ex. forums, listservs, IRC channels, etc.)': 'c',
    'A college/university computer science or software engineering book': 'd',
    'Internal Wikis, chat rooms, or documentation set up by my company for employees': 'e'
    
}

# Substituir os rótulos originais pelo mapeamento
df['TipoAutoAprendizado'] = df['TipoAutoAprendizado'].map(label_mapping)

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="TipoAutoAprendizado", y="QuantidadeDeLinguagens", hue="EnsinoSuperior")

# Modificar os rótulos do eixo x
plt.xticks(rotation=0, ha='right')  # Rotacionar os rótulos

# Adicionar explicação sobre o significado das letras
plt.text(0.5, -0.15, 
         "a: The official documentation and/or standards for the technology\n"
         "b: A book or e-book from O’Reilly, Apress, or a similar publisher\n"
         "c: Online developer communities other than Stack Overflow (ex. forums, listservs, IRC channels, etc.)\n"
         "d: A college/university computer science or software engineering book\n"
         "e: Internal Wikis, chat rooms, or documentation set up by my company for employees",
         ha='center', va='top', fontsize=12, 
         transform=plt.gca().transAxes)

# Ajustar os limites do eixo y se necessário
plt.ylim(0, df['QuantidadeDeLinguagens'].max() * 1.1)  # Aumentar um pouco o limite superior

# Mostrar o gráfico
plt.xlabel("Tipo de Autoaprendizado")
plt.ylabel("Quantidade de Linguagens")
plt.legend(title="Ensino Superior")

plt.tight_layout()  # Ajustar o layout para evitar sobreposição
plt.show()
"""

"""
#Hipotese 4

# Definir o tema e contexto corretamente
sns.set_theme(context="notebook", style="whitegrid")

# Criar um DataFrame a partir dos dados
df = pd.DataFrame(dh.gerar_dataframe_hipotese4(mn.dados))

# Mapeamento de rótulos originais para letras
label_mapping = {
    'The official documentation and/or standards for the technology': 'a',
    'A book or e-book from O’Reilly, Apress, or a similar publisher': 'b',
    'Online developer communities other than Stack Overflow (ex. forums, listservs, IRC channels, etc.)': 'c',
    'A college/university computer science or software engineering book': 'd',
    'Internal Wikis, chat rooms, or documentation set up by my company for employees': 'e'
}

# Substituir os rótulos originais pelo mapeamento
df['TipoAutoAprendizado'] = df['TipoAutoAprendizado'].map(label_mapping)

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="TipoAutoAprendizado", y="QuantidadeDeLinguagens", hue="EnsinoSuperior")

# Modificar os rótulos do eixo x
plt.xticks(rotation=45, ha='right')  # Rotacionar os rótulos

# Adicionar uma caixa de explicação com fundo
props = dict(boxstyle='round', facecolor='lightgray', alpha=0.5)
plt.text(1.05, 0.5, 
         "A: Autoaprendizado 1\n"
         "B: Autoaprendizado 2\n"
         "C: Autoaprendizado 3\n"
         "D: Autoaprendizado 4", 
         ha='left', va='center', fontsize=10, bbox=props, transform=plt.gca().transAxes)

# Ajustar os limites do eixo y se necessário
plt.ylim(0, df['QuantidadeDeLinguagens'].max() * 1.1)

# Título e rótulos dos eixos
plt.title("Quantidade de Linguagens por Tipo de Autoaprendizado")
plt.xlabel("Tipo de Autoaprendizado")
plt.ylabel("Quantidade de Linguagens")

# Mover a legenda (hue) para fora do gráfico
plt.legend(title="Ensino Superior", bbox_to_anchor=(1.05, 1), loc='upper left')

# Ajustar o layout para evitar sobreposição
plt.tight_layout()

# Mostrar o gráfico
plt.show()
"""
"""
#Hipotese 3

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys

# Para poder importar o módulo a partir do diretório '../src'
sys.path.append('../src')

import dataframes_hipoteses as dh 
import main as mn 
 
# Definir o tema e estilo do gráfico
sns.set_theme(style="whitegrid")

# Criar um DataFrame a partir dos dados
df = pd.DataFrame(dh.gerar_dataframe_hipotese3(mn.dados))

# Definir uma paleta personalizada
paleta_linda_hex = ['#DCD301', '#DC0701', '#001EDB', '#C800DB', '#00DBA3', '#BD7200']

# Criar um dicionário de mapeamento para os valores de "NiveisEducacionais"
hue_mapping = {
    'Fundamental': 'A',
    'Médio': 'B',
    'Superior Incompleto': 'C',
    'Superior Completo': 'D',
    'Pós-Graduação': 'E'
}

# Aplicar o mapeamento à coluna "NiveisEducacionais"
df['NiveisEducacionais'] = df['NiveisEducacionais'].map(hue_mapping)

# Criar o gráfico de linhas
plt.figure(figsize=(10, 6))  # Definir o tamanho da figura
sns.lineplot(data=df, x="AnosCodando", y="Empregabilidade", hue="NiveisEducacionais", palette=paleta_linda_hex)

# Adicionar títulos e rótulos com espaçamento personalizado
plt.xlabel("Anos Codando", labelpad=15)  # Espaçamento do rótulo do eixo X
plt.ylabel("Empregabilidade", labelpad=15)  # Espaçamento do rótulo do eixo Y

# Ajustar o tamanho e a posição da legenda (hue)
plt.legend(title="Níveis Educacionais (Índice)", title_fontsize=14, fontsize=12, loc="lower center")

# Adicionar uma caixa de texto explicando o índice
plt.text(1.05, 0.5, "A: Fundamental\nB: Médio\nC: Superior Incompleto\nD: Superior Completo\nE: Pós-Graduação",
         transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.6))

# Mostrar o gráfico 
plt.show()
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys

# Para poder importar o módulo a partir do diretório '../src'
sys.path.append('../src')

import dataframes_hipoteses as dh 
import main as mn 
 
# Definir o tema
sns.set_theme()

# Criar um DataFrame a partir dos dados
df = pd.DataFrame(dh.gerar_dataframe_hipotese1(mn.dados))

# Usar pivot_table para agregar valores duplicados (por exemplo, usando a média)
df_p = df.pivot_table(index="YearsCoding", columns="LinguagemProgramacao", values="HabitosSaudaveis", aggfunc="mean")

# Inverter os anos
df_p = df_p.sort_index(ascending=False)


# Criar o heatmap
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(df_p, annot=True, fmt=".2f", cmap="magma_r", ax=ax)

# Adicionar títulos e rótulos com espaçamento personalizado
plt.xlabel("Linguagem Programação (Índice)", labelpad=15)  # Espaçamento do rótulo do eixo X
plt.ylabel("Anos Codando", labelpad=15)  # Espaçamento do rótulo do eixo Y

# Adicionar uma caixa de texto explicando o índice
plt.text(1.0, 1.05, "Índice de Hábitos Saudáveis",
         transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.6))

# Mostrar o gráfico
plt.show()

"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys

# Para poder importar o módulo a partir do diretório '../src'
sys.path.append('../src')

import dataframes_hipoteses as dh
import main as mn

# Carregar o dataframe gerado pela função
df = pd.DataFrame(dh.gerar_dataframe_hipotese2(mn.dados))

# Configuração das cores e formatos
palette = {"Python": "blue", "Java": "green", "C": "red", "JavaScript": "orange"}  # Cores para cada linguagem
markers = {"Python": "o", "Java": "s", "C": "D", "JavaScript": "X"}  # Formatos dos pontos

# Criando o gráfico de dispersão com cores e formatos diferentes
g = sns.lmplot(
    data=df,
    x="PeriodoCodando", y="Salario", hue="LinguagemProgramacao", markers=markers, palette=palette,
    height=5, fit_reg=False  # fit_reg=False para não desenhar a linha de regressão
)

# Ajustar os rótulos dos eixos
g.set_axis_labels("Anos Codando", "Salário Anual (convertido)")

# Exibir o gráfico
plt.show()
