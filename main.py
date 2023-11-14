from datasets import load_dataset
import numpy as np

# Se cargan los datos
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

# Obtiene la lista de edades
edades = data["age"]

# Convierte la lista de edades a un arreglo de numpy
edades_np = np.array(edades)

# Calcula el promedio de las edades de los pacientes
promedio_edad = np.mean(edades_np)

# Imprime el resultado
print(f"El promedio de edad de las personas participantes en el estudio es: {promedio_edad:.2f}")