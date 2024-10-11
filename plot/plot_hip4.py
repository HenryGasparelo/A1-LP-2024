import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys

# Para poder importar o módulo a partir do diretório '../src'
sys.path.append('../src')

import dataframes_hipoteses as dh
import main as mn


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
dict(boxstyle='round', facecolor='lightgray', alpha=0.5)
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
plt.xticks(rotation=0, ha='right')  # Rotacionar os rótulos

# Adicionar uma caixa de explicação com fundo
props = dict(boxstyle='round', facecolor='lightgray', alpha=0.5)
plt.text(1.05, 0.5, 
         "a: The official documentation and/or standards for the technology\n"
         "b: A book or e-book from O’Reilly, Apress, or a similar publishern"
         "c: Online developer communities other than Stack Overflow (ex. forums, listservs, IRC channels, etc.)\n"
         "d: A college/university computer science or software engineering book\n"
         "e: Internal Wikis, chat rooms, or documentation set up by my company for employees",
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