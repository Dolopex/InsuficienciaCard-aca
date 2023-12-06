import pandas as pd
import matplotlib.pyplot as plt

# Cargar el DataFrame desde el archivo CSV exportado por el script de ETL
df = pd.read_csv('datos_procesados.csv')

# Crear subplots para los gráficos de torta
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

# Categorías
categorias = ['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']

# Colores
colors = ['lightgreen', 'lightskyblue']

# Nombres para "Si" y "No"
labels = ['No', 'Sí']

#Nombres categorias
categorias_nombres = ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos']

for i, categoria in enumerate(categorias):
    # Calcular porcentajes
    counts = df[categoria].value_counts(normalize=True) * 100

    # Graficar torta
    axes[i//2, i%2].pie(counts, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    axes[i//2, i%2].set_title(f'Distribución de {categorias_nombres[i]}')

# Ajustar diseño de subplots
plt.tight_layout()
plt.show()
