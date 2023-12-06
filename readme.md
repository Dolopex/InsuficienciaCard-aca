**##** Proyecto Integrador - Análisis de Datos de Insuficiencia Cardíaca

Este proyecto utiliza Python para analizar un conjunto de datos sobre insuficiencia cardíaca. El conjunto de datos contiene registros médicos de 299 pacientes durante un período de seguimiento. Las características clínicas incluyen información sobre edad, anemia, presión arterial alta, entre otras.

## Instalación

Para ejecutar este proyecto, asegúrate de instalar las librerias requeridas de "requirements.txt"

```bash
pip install -r requirements.txt
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

## Notas Parte 4
4.0 Se crea un nuevo archivo "download.py" en el que se cargan los datos mediante un GET requets

4.0.1 Se importan las librerias requeridas "request" y "csv"

4.0.2 Se crea una funcion que descargue y guarde los datos

4.1 Se hace el get request para traer los datos desde url

4.2 Se crea un codigo de status exitoso de la operacion (codigo 200)

4.3 Si la operacion es exitosa, los datos se escriben en formato csv

4.4 Se decodifica el contenido para que lo lea como un txt

4.5 Se hacen condicionales que se impriman en la consola de acuerdo a si la operacion fue exitosa o fallida

4.6 Se carga la url de donde se descargaran los datos

4.7 Se le asigna un nombre al archivo csv

4.8 Se llama a la funcion para descargar y guardar

## Notas Parte 5

5.0 Se importa  `StringIO` from `io` para crear un objeto StringIO para leer el contenido de texto de la respuesta HTTP.

5.1 Se usaron tecnicas de procesamiento de datos para lllenar valores faltantes, verificar que no existan filas repetidas y que Verifique si existen valores atípicos para eliminarlos

5.2 Se creó una columna con los que categoriza por edades

5.3 Se encapsula todo y se guarda en "datos.csv"

## Parte 6

Funcionalidades Implementadas
1. Descarga Automática de Datos
Se implementó una función que utiliza la biblioteca requests para descargar automáticamente los datos desde una URL proporcionada como argumento de línea de comandos.
2. Conversión a DataFrame y Operaciones de Limpieza
Los datos descargados se convierten en un DataFrame de Pandas, permitiendo un manejo eficiente y versátil.
Se aplicaron técnicas de limpieza de datos, eliminando filas con valores faltantes y duplicadas, y se eliminaron valores atípicos específicos.
3. Categorización por Edades
Se creó una nueva columna en el DataFrame que categoriza a los individuos según grupos de edad predefinidos.
4. Exportación Automática a CSV
El DataFrame resultante después del procesamiento se exporta automáticamente a un archivo CSV llamado "datos.csv".
Uso del Script
Para ejecutar el script procesar_datos.py, sigue estos pasos:

Abre la terminal en la ubicación del script.
Ejecuta el siguiente comando, reemplazando <URL_DATOS> con la URL específica de los datos que deseas procesar:
bash
Copy code
python procesar_datos.py <URL_DATOS>

## Notas Parte 6
6.0 Se importó StringIO desde io para crear un objeto StringIO y leer el contenido de texto de la respuesta HTTP.

6.1 Se utilizaron técnicas de procesamiento de datos para llenar valores faltantes, verificar la no existencia de filas repetidas y eliminar valores atípicos.

6.2 Se creó una columna que categoriza por edades.

6.3 Se encapsuló todo el proceso y se guardaron los resultados en el archivo "datos.csv".

## Parte 7 , 8, 9
Para esta seccion del proyecto, se realizaron análisis y visualizaciones de datos utilizando Matplotlib y plotly.express Se implementaron gráficos de barras,subplots,histogramas y 3d en Matplotlib para explorar distribuciones y relaciones dentro del conjunto de datos de insuficiencia cardíaca. 
Asegúrate de tener instalada la biblioteca Matplotlib.

```bash
pip install matplotlib
```
y

```bash
pip install plotly pandas
```

## Notas parte 7

7.0 Importación de Librerías
Se importaron las librerías Pandas y Matplotlib para el manejo y visualización de datos.

7.1 Carga del DataFrame
Se cargó el DataFrame desde el archivo CSV exportado por el script de ETL.

7.2 Histograma de Distribución de Edades
Se creó un histograma para visualizar la distribución de edades en el conjunto de datos.

7.3 Gráfico de Barras Agrupado por Género
Se utilizó la función groupby para agrupar los datos por género y contar la cantidad de anémicos, diabéticos, fumadores y muertos.

Configuración para graficar barras lado a lado.

Se creó un gráfico de barras verticales agrupadas por género y categorías de interés como anémicos, diabéticos, fumadores y muertos.

Configuración adicional y visualización del gráfico.

## Notas parte 8

8.0 Carga del DataFrame
Se cargó el DataFrame desde el archivo CSV exportado por el script de ETL.

8.1 Creación de Subplots
Se crearon subplots con 2 filas y 2 columnas para alojar los gráficos de torta.

8.2 Configuración de Categorías y Colores
Se definieron las categorías de interés como 'anaemia', 'diabetes', 'smoking' y 'DEATH_EVENT'. También se establecieron colores y nombres para las categorías "Sí" y "No".

8.3 Iteración y Creación de Gráficos de Torta
Se utilizó un bucle para iterar sobre las categorías y calcular los porcentajes de distribución.

Se crearon gráficos de torta en cada subplot, mostrando la proporción de "Sí" y "No" para cada categoría.

8.4  Ajustes de Diseño
Se realizaron ajustes de diseño para organizar y mostrar los gráficos de torta de manera clara y ordenada.

8.5 Visualización
Se ajustó el diseño de los subplots y se mostraron los gráficos de torta para las categorías de interés.

## Notas parte 9

9.0 Carga del DataFrame
Se cargó el DataFrame desde el archivo CSV exportado por el script de ETL.

9.1 Eliminación de Columnas no Necesarias
Se eliminaron las columnas 'DEATH_EVENT' y 'Categoria_Edad', ya que no son necesarias para la reducción de dimensionalidad.

9.2 Extracción de Vector Objetivo
Se extrajo el vector objetivo ('DEATH_EVENT') y se almacenó en la variable 'y'.

9.3 Aplicación de t-SNE para Reducción de Dimensionalidad
Se utilizó la técnica t-SNE para reducir la dimensionalidad del conjunto de datos a tres dimensiones.

9.4 Creación de DataFrame para la Visualización
Se creó un DataFrame específico para la visualización, con las dimensiones reducidas ('X', 'Y', 'Z') y el vector objetivo ('DEATH_EVENT').

9.5 Graficar Dispersión 3D con Plotly
Se utilizó Plotly Express para crear un gráfico de dispersión tridimensional. La variable objetivo ('DEATH_EVENT') se utilizó para asignar colores a los puntos.

9.6 Cambio del Título en la Barra Lateral Derecha
Se actualizó el diseño del gráfico para cambiar el título en la barra lateral derecha, especificando "Muertos" como título.

9.7 Configuración Adicional de Diseño
Se realizaron ajustes adicionales en el diseño, incluyendo el título general y las etiquetas de los ejes.

9.8 Visualización
Se mostró el gráfico interactivo de dispersión 3D con t-SNE.