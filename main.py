from datasets import load_dataset
import numpy as np
import pandas as pd

# Se cargan los datos
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

# Convierte la estructura en dataframe de Pandas
df = pd.DataFrame(data)

# Separa el dataframe en perecidos y sobrevivientes
df_perecidos = df[df['is_dead'] == 1]
df_sobrevivientes = df[df['is_dead'] == 0]

# Calcula el promedio de las edades de los pacientes de cada dataset
promedio_edad_perecidos = np.mean(df_perecidos['age'])
promedio_edad_sobrevivientes = np.mean(df_sobrevivientes['age'])

# Imprime el resultado
print(f"El promedio de edad de las personas que perecieron es: {promedio_edad_perecidos:.2f}")
print(f"El promedio de edad de las personas que sobrevivieron es: {promedio_edad_sobrevivientes:.2f}")

"""Verificar si los datos son correctos"""
tipos_de_datos = df.dtypes
print("Tipos de datos en cada columna:")
print(tipos_de_datos)

# Calcular la cantidad de hombres fumadores vs mujeres fumadoras
# usando la función groupby agregamos género y hábito de fumar
conteo_fumadores = df.groupby(['is_male', 'is_smoker']).size().unstack().fillna(0)

# Mejorar la presentación del resultado
conteo_fumadores.columns = ['No Fumador', 'Fumador']
conteo_fumadores.index = ['Mujer', 'Hombre']

# Imprimir el resultado
print("\nCantidad de hombres y mujeres fumadoras:")
print(conteo_fumadores)