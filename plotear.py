import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
import numpy as np

def plot_linea(n, min_y, max_y, min_x, max_x):
    if n.hoja:
        return
    else:
        if n.label == "x":
            plt.plot([n.umbral, n.umbral], [min_y, max_y])

            #max_y = n.umbral
            plot_linea(n.lc, min_y, max_y, min_x, max_x)  # voy por la izquierda
            #min_y = n.umbral


            plot_linea(n.rc, min_y, max_y, min_x, max_x)  # voy por la derecha

        else:
            plt.plot([min_x, max_x], [n.umbral, n.umbral])

            #min_x=n.umbral
            plot_linea(n.lc, min_y, max_y, min_x, max_x)  # voy por la izquierda
            #max_x = n.umbral
            plot_linea(n.rc, min_y, max_y, min_x, max_x)  # voy por la derecha

def plotear(dataset, arbol, titulo):

    path = 'res/tree.svg'

    colors = np.where(dataset['clase'] == 1, 'b', 'k') #clase 1 = azul // clase0 = negro
    dataset.plot(kind="scatter", x="x", y="y", s=25, c=colors)

    max_x = dataset["x"].max()
    min_x  = 0
    max_y = dataset["y"].max()
    min_y  = 0

    n = arbol.raiz()

    plot_linea(n, min_y, max_y, min_x, max_x)

    plt.savefig(path)

    if arbol is not None:
        arbol.asignar_id() #asigna id a cada nodo u hoja
        arbol.export("mi arbol", "arbol.gv") #exporta la figura del arbol

    return path