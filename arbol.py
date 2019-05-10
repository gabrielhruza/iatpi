from pydot import Digraph

class Arbol(object):

    def __init__(self):
        self.arbol = list()

    def add(self, nodo):
        self.arbol.append(nodo)

    def raiz(self):
        return self.arbol[0]

    def long(self):
        return len(self.arbol)

    def asignar_id(self): # asignar id unico a cada nodo/hoja para poder dibujar despues
        id = self.raiz().id
        for item in self.arbol:
            if item is not None:
                item.id = id
                id += 1

    def export(self, titulo, filename, size='8.5'):
        f = Digraph(titulo, filename=filename)
        f.attr(size=size)
        raiz = self.raiz()

        for item in self.arbol:
            item.graficar(f)

        f.view()

class Nodo(object):

    def __init__(self, label=None, parent=None, lc=None, rc=None, umbral=None, id=None):
        super(Nodo, self).__init__()

        self.label 	= label # etiqueta
        self.parent = self # Nodo padre
        self.lc 	= lc # left child => Nodo u Hoja
        self.rc 	= rc # right child => Nodo u Hoja
        self.umbral = umbral # umbral <= o >
        self.id 	= id # nivel para hacer unicas las etiqutes
        self.clase  = None
        self.cant   = None

    def graficar(self, grafico): # retorna la sintaxis de pydot para un Nodo

        if self.clase == 0:
            grafico.attr('node', shape='proteasesite')
        elif self.clase == 1:
            grafico.attr('node', shape='proteinstab')
        else:
            grafico.attr('node', shape='box')

        grafico.node(str(self.id))
        if self.lc is not None:
            grafico.edge(str(self.id), str(self.lc.id), label='<=')
        if self.rc is not None:
            grafico.edge(str(self.id), str(self.rc.id), label='>')

class Hoja(object):
    """docstring for Hoja"""
    def __init__(self, parent = None, clase = None, cant = None, id=None):
        super(Hoja, self).__init__()

        self.parent 	= parent
        self.clase  	= clase
        self.cant 		= cant
        self.id			= id

    # retorna la sintaxis de pydot para una Hoja
    def graficar(self, grafico):
        grafico.attr('node', shape='circle')
        grafico.node(str(self.id))
