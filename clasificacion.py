import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
import pandas as pd

def graficar_distribucion_clases(y):
    plt.figure(figsize=(8, 6))
    plt.hist(y, bins=len(set(y)), edgecolor='black')
    plt.title('Distribución de Clases')
    plt.xlabel('Muertos')
    plt.ylabel('Cantidad')
    plt.show()

def clasificacion_decision_tree(X, y):
    # Realizar partición estratificada en conjunto de entrenamiento y test
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Ajustar un árbol de decisión
    modelo_arbol = DecisionTreeClassifier(random_state=42)
    modelo_arbol.fit(X_train, y_train)

    # Calcular el accuracy sobre el conjunto de test
    preds_test = modelo_arbol.predict(X_test)
    accuracy = accuracy_score(y_test, preds_test)
    print(f"Accuracy del Árbol de Decisión: {accuracy}")

def clasificacion_random_forest(X, y):
    # Realizar partición estratificada en conjunto de entrenamiento y test
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Ajustar un Random Forest
    modelo_rf = RandomForestClassifier(random_state=42)
    modelo_rf.fit(X_train, y_train)

    # Calcular el accuracy sobre el conjunto de test
    preds_test_rf = modelo_rf.predict(X_test)
    accuracy_rf = accuracy_score(y_test, preds_test_rf)
    print(f"Accuracy del Random Forest: {accuracy_rf}")

    # Calcular la matriz de confusión
    matriz_confusion_rf = confusion_matrix(y_test, preds_test_rf)
    print(f"Matriz de Confusión del Random Forest:\n{matriz_confusion_rf}")

    # Calcular el F1-Score
    f1_score_rf = f1_score(y_test, preds_test_rf)
    print(f"F1-Score del Random Forest: {f1_score_rf}")

if __name__ == "__main__":
    # Cargar el DataFrame desde el archivo CSV procesado
    df = pd.read_csv("datos_procesados.csv")

    # Eliminar la columna 'Categoria_Edad'
    if 'Categoria_Edad' in df.columns:
        df = df.drop(columns=['Categoria_Edad'])
        print("La columna 'Categoria_Edad' eliminada.")

        # Graficar la distribución de clases usando la columna 'DEATH_EVENT'
        if 'DEATH_EVENT' in df.columns:
            graficar_distribucion_clases(df['DEATH_EVENT'])
            
            # Añadir llamada a la función para clasificación con Random Forest
            clasificacion_random_forest(df.drop(columns=['DEATH_EVENT']), df['DEATH_EVENT'])
        else:
            print("No se encontró la columna 'DEATH_EVENT' para la gráfica de distribución de clases.")
    else:
        print("La columna 'Categoria_Edad' no está presente en el DataFrame.")
