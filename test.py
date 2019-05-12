import pandas as pd
from training import train_for_test

def test(test_dataset_path, modelo):
	predicciones = { 'correctos': [], 'inciertos': [], 'incorrectos': [] }

	modelo = train_for_test('datasets/condavid.csv')
	df = pd.read_csv(test_dataset_path)

	if df.empty:
		return ""

	df.columns = ["x", "y", "clase"]

	#tenemos el modelo y el dataset de prueba, ahora vamos a retornar las predicciones i hope this will run, please!




	print(df)
	return predicciones

# toma como parametros el modelo y el dataset de prueba => retorna la prediccion
#def predecir(model, test_data):
#	prediccion = pd.DataFrame()
#	return prediccion


# toma un registro de un dataset sin clase y un modelo => retorna la clase deducida
def deducir(model, registro):
	return clase


# compara dos dataset por la columna clase
def comparar(real_data, test_data):
	return exactitud