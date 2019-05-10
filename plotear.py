import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plotear(dataset, arbol, titulo):

    path = 'res/tree.svg'

    colors = np.where(dataset['clase'] == 1, 'r', 'k') #clase 1 = rojo // clase0 = negro
    dataset.plot(kind="scatter", x="x", y="y", s=20, c=colors)

    techo_x = dataset["x"].max()
    piso_x  = 0
    techo_y = dataset["y"].max()
    piso_y  = 0
    resg_label = "x"

    #for nodo in arbol.arbol:

        #if nodo.label == "x":
         #   plt.plot([nodo.umbral,nodo.umbral],[piso_y,techo_y])

        #else:
            #if nodo.label != resg_label:
                # actualizar techo
             #   techo_x = nodo.parent.umbral

         #   plt.plot([piso_x,techo_x], [nodo.umbral,nodo.umbral])

    plt.title(titulo)
    plt.savefig(path)

    if arbol is not None:
        arbol.asignar_id()
        arbol.export("mi arbol", "arbol.gv")


    return path