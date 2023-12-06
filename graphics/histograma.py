import pandas as pd
import matplotlib.pyplot as plt

# Cargar el DataFrame desde el archivo CSV exportado por el script de ETL
df = pd.read_csv('datos_procesados.csv')

# Graficar la distribución de edades con un histograma
plt.figure(figsize=(10, 6))
plt.hist(df['age'], bins=range(0, 105, 5), color='r', edgecolor='black')  # Ajustar el rango y el paso del bin
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Cantidad')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Agrupar por género y contar la cantidad de anémicos, diabéticos, fumadores y muertos
grouped_df = df.groupby('sex').agg({
    'anaemia': 'sum',
    'diabetes': 'sum',
    'smoking': 'sum',
    'DEATH_EVENT': 'sum'
}).reset_index()

# Configuración para graficar barras lado a lado
bar_width = 0.2
index = range(len(grouped_df))
opacity = 0.8

# Graficar barras verticales lado a lado
plt.bar(index, grouped_df['anaemia'], bar_width, alpha=opacity, color='b', label='Anémicos')
plt.bar([i + bar_width for i in index], grouped_df['diabetes'], bar_width, alpha=opacity, color='g', label='Diabéticos')
plt.bar([i + 2 * bar_width for i in index], grouped_df['smoking'], bar_width, alpha=opacity, color='r', label='Fumadores')
plt.bar([i + 3 * bar_width for i in index], grouped_df['DEATH_EVENT'], bar_width, alpha=opacity, color='c', label='Muertos')

# Configuración adicional
plt.xlabel('Género')
plt.ylabel('Cantidad')
plt.title('Estadísticas por Género')
plt.xticks([i + 1.5 * bar_width for i in index], ['Mujeres', 'Hombres'])  # Etiquetas centradas
plt.legend()

# Mostrar la gráfica
plt.show()