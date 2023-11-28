import requests
import csv

def descargar_y_guardar_csv(url, nombre_archivo):
    # GET request
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Escribe la respuesta en un archivo CSV
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
            # Decodificar el contenido de la respuesta como texto y escribirlo en el archivo
            archivo_csv.write(response.text)
        print(f"Descarga exitosa. Datos guardados en: '{nombre_archivo}'")
    else:
        print(f"Error al descargar los datos. Código de estado: {response.status_code}")

# URL de los datos
url_datos = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"

# Nombre del archivo donde se guardarán los datos
nombre_archivo_csv = "datos.csv"

# Llamar a la función para descargar y guardar los datos
descargar_y_guardar_csv(url_datos, nombre_archivo_csv)
