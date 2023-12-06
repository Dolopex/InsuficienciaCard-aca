import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Cargar el DataFrame desde el archivo CSV
df = pd.read_csv('datos.csv')

# Eliminar las columnas DEATH_EVENT, age y Categoria_Edad
X = df.drop(columns=['DEATH_EVENT', 'age', 'Categoria_Edad'])

# Vector objetivo
y = df['age']

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar el modelo de regresión lineal
modelo_regresion = LinearRegression()

# Ajustar el modelo a los datos de entrenamiento
modelo_regresion.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = modelo_regresion.predict(X_test)

# Calcular el error cuadrático medio
mse = mean_squared_error(y_test, y_pred)

# Imprimir el error cuadrático medio
print(f'Error Cuadrático Medio: {mse}')

# Mostrar las edades reales y predichas para comparación
comparacion_resultados = pd.DataFrame({'Real': y_test, 'Predicho': y_pred})
print(comparacion_resultados)
