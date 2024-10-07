import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Dados de exemplo
data = {
    'Categoria': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Subcategoria': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Valor': [10, 15, 20, 25, 30, 35]
}

# Criando DataFrame
df = pd.DataFrame(data)

# Criando o gráfico de multibarras
sns.set_theme(style="whitegrid")
sns.barplot(x="Categoria", y="Valor", hue="Subcategoria", data=df)

# Exibir o gráfico
plt.show()
