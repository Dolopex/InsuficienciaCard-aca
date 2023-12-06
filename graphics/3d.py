import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
import plotly.express as px

# Cargar el DataFrame desde el archivo CSV exportado por el script de ETL
df = pd.read_csv('datos_procesados.csv')

# Eliminar columnas no necesarias
X = df.drop(columns=['DEATH_EVENT', 'Categoria_Edad'])

# Extraer el vector objetivo (coluna DEATH_EVENT)
y = df['DEATH_EVENT'].values

# Aplicar t-SNE para reducción de dimensionalidad
X_embedded = TSNE(n_components=3, learning_rate='auto', init='random', perplexity=3).fit_transform(X)

# Crear DataFrame para el gráfico
df_plot = pd.DataFrame(X_embedded, columns=['X', 'Y', 'Z'])
df_plot['DEATH_EVENT'] = y

# Graficar dispersión 3D con Plotly
fig = px.scatter_3d(df_plot, x='X', y='Y', z='Z', color='DEATH_EVENT', labels={'color': 'Muerto'})

# Cambiar el título en la barra lateral derecha
fig.update_layout(coloraxis_colorbar=dict(title='Muertos'))

fig.update_layout(title='Visualización 3D con t-SNE', scene=dict(zaxis=dict(title='Z')))
fig.show()
