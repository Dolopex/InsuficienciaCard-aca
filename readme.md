**#** Proyecto Integrador - Análisis de Datos de Insuficiencia Cardíaca

Este proyecto utiliza Python para analizar un conjunto de datos sobre insuficiencia cardíaca. El conjunto de datos contiene registros médicos de 299 pacientes durante un período de seguimiento. Las características clínicas incluyen información sobre edad, anemia, presión arterial alta, entre otras.

## Instalación

Para ejecutar este proyecto, asegúrate de tener instalada la librería `datasets` de Hugging Face:

```bash
pip install datasets
```

## Notas Parte 1

1.0 Se importaron las librerias Numpy y datasets

1.1 Se crearon las variables "datasets" y "data" en donde se cargaron los datos

1.2 Se creó la variable "edades" de la cual tomamos solos los datos de las edades del dataset

1.3 Se convierte la lista de edades en un array de numpy

1.4 Se crea una variable que calcule el promedio de las edades

1.5 Se imprime el resultado

## Notas Parte 2
2.0 Se importa Pandas

2.1 Se Cambia el Dataset de numpy a Pandas con pd.DataFrame

2.2 Se Separa el DataFrame en 2 para calcular el promedio de cada uno, se le asigna el valor de 1 a los pacientes perecidos y 0 a los sobrevivientes

2.3 Se calcula el promedio de las edades de los 2 dataframes con numpy

## Notas Parte 3
3.0 Se verifican los tipos de datos de cada columna del DataSet y se imprimen los resultados

3.1 Se crea una variable que usando la funcion Groupby se agregan los datos del genero y sin son fumadores o no

3.2 Como agregado personal ajuste las columnas y los indices para que la informacion tenga una mejor presentacion

3.3 Se imprimen los resultados