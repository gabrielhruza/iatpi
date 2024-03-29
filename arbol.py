from graphviz import Digraph
import time
import pickle

class Arbol(object):

    def __init__(self):
        self.arbol = list()

    def add(self, nodo):
        self.arbol.append(nodo)

    def raiz(self):
        return self.arbol[0]

    def long(self):
        return len(self.arbol)

    def imprimir(self):
        for item in self.arbol:
            print(item.label, item.umbral, item.id, item.clase)


    def asignar_id(self): # asignar id unico a cada nodo/hoja para poder dibujar despues
        id = self.raiz().id
        for item in self.arbol:
            if item is not None:
                item.id = id
                id += 1

    def export(self, titulo, filename, size='8.5'):

        self.asignar_id()

        f = Digraph(titulo, filename=filename, format="pdf")
        f.attr(size=size)
        f.attr('node', shape='record', style='rounded')
        i = 0
        while i<len(self.arbol):
            self.arbol[i].graficar(f)
            i+=1
        try:
            f.render()
        except:
            pass


    def pred(self, reg):

        raiz = self.raiz()

        clase = 99
        clase = self.buscar(raiz, reg, clase)

        return clase


    def buscar(self, nodo, reg, c):
        while not nodo.hoja:

            if reg[nodo.label] <= nodo.umbral:
                nodo = nodo.lc

            else:
                nodo = nodo.rc

        return nodo.clase


    def export_file(self):  # exporto el arbol hacia un archivo .data "ver excepciones"

        path = 'modelos/' + time.strftime("%d-%m-%Y%H%M%S") + '.data'

        with open(path, 'wb') as filehandle:
            # store the data as binary data stream
            return  pickle.dump(self, filehandle)


    def import_file(self, path): # importo el arbol desde un archivo "ver excepciones"

        # read the data as binary data stream
        with open(path, 'rb') as filehandle:
            return pickle.load(filehandle)


class Nodo(object):

    def __init__(self, label=None, parent=None, lc=None, rc=None, umbral=None, id=None, ganancia = None):
        super(Nodo, self).__init__()

        self.label 	= label # etiqueta
        self.parent = self # Nodo padre
        self.lc 	= lc # left child => Nodo u Hoja
        self.rc 	= rc # right child => Nodo u Hoja
        self.umbral = umbral # umbral <= o >
        self.ganancia = ganancia #gain ratio del nodo
        self.id 	= id # nivel para hacer unicas las etiqutas del graphviz
        self.clase  = None
        self.cant   = None
        self.hoja   = False

    def graficar(self, grafico): # retorna la sintaxis de pydot para un Nodo

        if self.hoja:
            grafico.node(str(self.id), label="{Clase: "+str(self.clase)+ "| Cant: " + str(self.cant) + "\\n Gain Ratio: " + str(self.ganancia)+"}", color="green")
        else:
            grafico.node(str(self.id) , label="{"+ self.label.upper() + "| Gain Ratio: " + str(round(self.ganancia, 2))+"}")
            self.graficar_edge(grafico)
        return

    def graficar_edge(self, grafico):
        if self.lc is not None:
            grafico.edge(str(self.id), str(self.lc.id), headlabel='<= ' + str(round(self.umbral,2)), labelangle='60', labeldistance='2.8')
        if self.rc is not None:
            grafico.edge(str(self.id), str(self.rc.id), label='>' + str(round(self.umbral,2)))
        return

