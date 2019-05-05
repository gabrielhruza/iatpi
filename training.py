import pandas as pd
import math

from arbol import *
from plotear import *

# toma un dataset y devuelve el modelo (arbol)
def train(dataset_path):

    df = pd.read_csv(dataset_path)
    df.columns = ["x", "y", "clase"]

    modelo = Arbol()
    nodo_resguardo = Nodo(level=0)

    max_gan = 0.1

    decision_tree(df, modelo, nodo_resguardo, max_gan)

    path_resultado = plotear(df, modelo, "Mi plot")

    return path_resultado


# basado en el algoritmo c4.5
def decision_tree(dataset, arbol, nodo_resguardo, max_gan):

    # CASOS BASES
    # el dataset tiene muy pocos elementos => 3 para este caso
    #if len(dataset.index) < 3:
     #   print("sali por dataset pequeño")
     #   return ""

    # el dataset esta vacio
    if dataset.empty:
        #print("sali por dataset vacio")
        return ""

    # el dataset contiene solo valores de una sola clase
    # frecuencia cada clase en el dataset
    fc = dataset.groupby(["clase"]).count()

    # si la longitud de "fc" == 1 es pq el dataset tiene elementos de una sola clase
    if (len(fc.index) == 1):
        print("sali por todos la misma clase")
        return ""


    # CASO GENERAL

    # calculo la maxima ganancia de informacion de x (hago de cuenta que no hay repetidos por ahora)
    umbral_y_ganancia_x = max_ganancia(dataset, "x", max_gan)

    # calculo la maxima ganancia de informacion de y (hago de cuenta que no hay repetidos por ahora)
    umbral_y_ganancia_y = max_ganancia(dataset, "y", max_gan)

    # comparo entre ganancias de "x" y de "y"
    if (umbral_y_ganancia_x[1] > umbral_y_ganancia_y[1]):

        atributo    = "x"
        umbral      = umbral_y_ganancia_x[0]
        resg_gan    = umbral_y_ganancia_x[1]

    else:
        atributo = "y"
        umbral = umbral_y_ganancia_y[0]
        resg_gan = umbral_y_ganancia_y[1]

    particion = particionar(dataset, atributo, umbral)

    left_node   = Nodo()
    right_node  = Nodo()

    left_node.parent = nodo_resguardo
    right_node.parent = nodo_resguardo

    nodo_resguardo.umbral = umbral
    nodo_resguardo.label = atributo
    #nodo_resguardo.level = nodo_resguardo.level + 1
    nodo_resguardo.lc = left_node
    nodo_resguardo.rc = right_node

    #arbol.add(left_node)
    #arbol.add(right_node)
    arbol.add(nodo_resguardo)

    nodo_resguardo = left_node
    decision_tree(particion[0], arbol, nodo_resguardo, max_gan)

    nodo_resguardo = right_node
    decision_tree(particion[1], arbol, nodo_resguardo, max_gan)


# calculo de entropia (dataset es de tipo DataFrame)
def entropia(dataset):
    entropia = 0

    # verificar si el dataset se encuentra vacío
    if dataset.empty:
        return entropia

    # frecuencia cada clase en el dataset
    fc = dataset.groupby(["clase"]).count()

    # si la longitud de "fc" == 1 es pq el dataset tiene elementos de una sola clase
    if (len(fc.index) == 1):
        return entropia

    # longitud total del dataset
    size = len(dataset.index)

    n1 = fc["x"][0] / size
    n2 = fc["y"][1] / size

    entropia = n1 * math.log(n1, 2) + n2 * math.log(n2, 2)

    # ver para log 0
    return entropia * (-1)


def max_ganancia(dataset, atributo, max_gan):

    entropia_dataset = entropia(dataset)
    dataset = dataset.sort_values(by=[atributo])

    fe = dataset.head(1)[atributo]
    umbral_y_ganancia = [fe.values[0], 0]
    max_ganancia = 0

    # itero por cada elemento del dataset segun el atributo
    for index, row in dataset.iterrows():
        umbral_actual = row[atributo]

        particion = particionar(dataset, atributo, umbral_actual)

        # obtener la probabilidad de cada particion
        long_dataset = len(dataset.index)
        long_particion_1 = len(particion[0].index)
        long_particion_2 = len(particion[1].index)

        p1 = long_particion_1 / long_dataset
        p2 = long_particion_2 / long_dataset

        # entropia de cada particion
        entropia_particion_1 = entropia(particion[0])
        entropia_particion_2 = entropia(particion[1])

        # split info para tasa de ganancia
        sp_info = split_info(long_particion_1, long_particion_2, long_dataset)

        ganancia = entropia_dataset - (p1 * entropia_particion_1) - (p2 * entropia_particion_2)

        print(sp_info)

        if sp_info == 0:
            gain_ratio = 0
        else:
            gain_ratio = ganancia / sp_info

        if gain_ratio > max_ganancia:
            umbral_y_ganancia = [umbral_actual, gain_ratio]
            max_ganancia = gain_ratio

    return umbral_y_ganancia


def split_info(long_parte_1, long_parte_2, long_dataset):

    n1 = long_parte_1 / long_dataset
    n2 = long_parte_2 / long_dataset

    print(long_dataset)

    try:
        t1 = (n1 * math.log(n1, 2))*(-1)
    except:
        t1 = 0

    try:
        t2 = (n2 * math.log(n2, 2))*(-1)
    except:
        t2 = 0

    sp_info =  t1 + t2

    return sp_info


# tomo un dataset y lo particiono en 2 segun el umbral => retorno particiones[[p1], [p2]]
def particionar(dataset, atributo, umbral):
    particion = [[], []]

    particion[0] = dataset[dataset[atributo] <= umbral]
    particion[1] = dataset[dataset[atributo] > umbral]

    return particion