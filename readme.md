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