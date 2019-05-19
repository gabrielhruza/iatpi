import pandas as pd
from training import train_for_test

from arbol import *

def test(test_dataset_path, model_path):
    predicciones = { 'correctos': [], 'inciertos': [], 'incorrectos': [] }

    modelo = Arbol()
    modelo = modelo.import_file(model_path)

    df = pd.read_csv(test_dataset_path)

    if df.empty:
        return ""

    df.columns = ["x", "y", "clase"]

    #tenemos el modelo y el dataset de prueba, ahora vamos a retornar las predicciones
    for index, row in df.iterrows():

        pred = deducir(modelo, row)
        if pred == row['clase']:
            predicciones['correctos'].append(row)
        elif pred == 99:
            predicciones['inciertos'].append(row)
        else:
            # ver para colocar esta funcionalidad en otra parte (que devuelva row completo nomas)
            row['pred'] = pred
            predicciones['incorrectos'].append(row)

    return predicciones

def test_punto(path_modelo, punto):

    modelo = Arbol()
    modelo = modelo.import_file(path_modelo)

    return deducir(modelo, punto)


# toma un registro (punto XY) de un dataset sin clase y un modelo => retorna la clase deducida
def deducir(modelo, registro):

    clase = 99
    clase = modelo.pred(registro)

    return clase


# compara dos dataset por la columna clase
def comparar(real_data, test_data):
    return exactitud