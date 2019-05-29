import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_linea(n, min_y, max_y, min_x, max_x):
    for nodo in n.arbol:

        if not nodo.hoja:

            if nodo.label == "x":
                plt.plot([nodo.umbral, nodo.umbral], [min_y, max_y])
                min_x = nodo.umbral

            else:
                plt.plot([min_x, max_x], [nodo.umbral, nodo.umbral])
                min_y = nodo.umbral


def plot_linea_rec(n, min_y, max_y, min_x, max_x):

    if not n.hoja:

        min_x_resg = min_x
        min_y_resg = min_y

        if n.label == "x":
            plt.plot([n.umbral, n.umbral], [min_y, max_y], color="blue")
            min_x = n.umbral
        else:
            plt.plot([min_x, max_x], [n.umbral, n.umbral], color="blue")
            min_y = n.umbral

        plot_linea_rec(n.rc, min_y, max_y, min_x, max_x) #voy por la izquierda

        min_x = min_x_resg
        min_y = min_y_resg

        if n.label == "x":
            max_x = n.umbral
        else:
            max_y = n.umbral
        plot_linea_rec(n.lc, min_y, max_y, min_x, max_x) #voy por la derecha

    else:
        return

def plotear(dataset, arbol, titulo):

    max_x = dataset["x"].max()
    min_x = dataset["x"].min()
    max_y = dataset["y"].max()
    min_y = dataset["y"].min()

    n = arbol.raiz()
    plot_linea_rec(n, min_y, max_y, min_x, max_x)

    if arbol is not None:
        arbol.asignar_id() #asigna id a cada nodo u hoja
        arbol.export("mi arbol", "arbol.gv") #exporta la figura del arbol

    return dataset