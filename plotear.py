import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
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

def plotear(dataset, arbol, titulo):

    max_x = dataset["x"].max()
    min_x = dataset["x"].min()
    max_y = dataset["y"].max()
    min_y = dataset["y"].min()

    n = arbol.raiz()
    plot_linea(arbol, min_y, max_y, min_x, max_x)

    if arbol is not None:
        arbol.asignar_id() #asigna id a cada nodo u hoja
        arbol.export("mi arbol", "arbol.gv") #exporta la figura del arbol

    return dataset