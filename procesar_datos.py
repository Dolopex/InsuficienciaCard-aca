import sys
import requests
import pandas as pd
from io import StringIO

def descargar_y_crear_dataframe(url):
    # GET request
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Crear DataFrame desde el contenido de la respuesta
        df = pd.read_csv(StringIO(response.text))
        print("Descarga exitosa. DataFrame creado.")
        return df
    else:
        print(f"Error al descargar los datos. Código de estado: {response.status_code}")
        return None

def limpiar_dataframe(df):
    # Verificar valores faltantes
    if df.isnull().values.any():
        df = df.dropna()
        print("Se eliminaron filas con valores faltantes.")

    # Verificar filas repetidas
    if df.duplicated().any():
        df = df.drop_duplicates()
        print("Se eliminaron filas duplicadas.")

    # Verificar y eliminar valores atípicos 
    # Aquí, se eliminan valores atípicos en la columna 'age' que están por encima de 100
    df = df[df['age'] <= 100]
    print("Se eliminaron valores repetidos.")

    # Crear columna que categorice por edades
    bins = [0, 12, 19, 39, 59, 150]  # Rangos de edades
    labels = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    df['Categoria_Edad'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

    return df

def procesar_y_guardar_datos(url, nombre_archivo_csv):
    # Descargar y crear DataFrame
    df = descargar_y_crear_dataframe(url)

    if df is not None:
        # Limpiar DataFrame
        df_limpiado = limpiar_dataframe(df)

        # Guardar el resultado en el archivo CSV especificado
        df_limpiado.to_csv(nombre_archivo_csv, index=False)
        print(f"Datos procesados y guardados en: '{nombre_archivo_csv}'")

if __name__ == "__main__":
    # Obtener los argumentos de la línea de comandos
    if len(sys.argv) != 3:
        print("Uso: python script.py <URL_datos> <nombre_archivo_csv>")
        sys.exit(1)

    url_datos = sys.argv[1]
    nombre_archivo_csv = sys.argv[2]

    # Llamar a la función para procesar y guardar los datos
    procesar_y_guardar_datos(url_datos, nombre_archivo_csv)
