#Exemplo de heatmap
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

# Load the example flights dataset and convert to long-form
flights_long = sns.load_dataset("flights")
flights = (
    flights_long
    .pivot(index="month", columns="year", values="passengers")
)

# Draw a heatmap with the numeric values in each cell

davi = sns.color_palette("blend:#7AB,#EDA", as_cmap=True)

f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(data=flights, annot=True, fmt="d", linewidths=.5, ax=ax)

plt.show()

#outro exemplo
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Dados de exemplo para o heatmap
data = np.random.rand(10, 12)

# Definir uma paleta personalizada de roxo e vermelho
paleta_purple_red_hex = ['#4B0082', '#6A0DAD', '#800080', '#9932CC', '#FF4500', '#DC143C', '#B22222', '#8B0000']

# Criar o heatmap com anotações menores
sns.heatmap(data, cmap=sns.color_palette(paleta_purple_red_hex, as_cmap=True), annot=True, fmt=".2f",
            annot_kws={"size": 8})  # Aumente ou diminua o valor de "size" conforme necessário

# Mostrar o gráfico
plt.show()
