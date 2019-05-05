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

	def imprimir(self):
		for nodo in self.arbol:
			print(nodo.label, nodo.umbral)


class Nodo(object):

	def __init__(self, label=None, parent=None, lc=None, rc=None, umbral=None, level=None):
		super(Nodo, self).__init__()
		
		self.label 	= label # etiqueta
		self.parent = self # Nodo padre
		self.lc 	= lc # left child => Nodo u Hoja
		self.rc 	= rc # right child => Nodo u Hoja
		self.umbral = umbral # umbral <= o >
		self.level 	= level # nivel para hacer unicas las etiqutes

	# retorna la sintaxis de pydot para un Nodo
	def graficar(self, grafico):
		
		# graficar el nodo
		grafico = grafico.attr('node', shape='circle')
		
		# graficar las ramas con su etiqueta
		nodo_actual 	= self.label + "_" + self.level
		nodo_izquierdo 	= self.lc.label + "_" + self.lc.level
		nodo_derecho 	= self.rc.label + "_" + self.rc.level

		grafico = grafico.edge( nodo_actual, nodo_izquierdo, label=self.ll)
		grafico = grafico.edge( nodo_actual, nodo_derecho, label=self.rl)


		# grafico los hijos
		self.lc.graficar(grafico)
		self.rc.graficar(grafico)

		return grafico


class Hoja(object):
	"""docstring for Hoja"""
	def __init__(self, arg):
		super(Hoja, self).__init__()
		
		self.parent = None	# Nodo padre
		self.clase  = None 	#
	
	# retorna la sintaxis de pydot para una Hoja
	def graficar(self, grafico):
		return grafico


def exportar_a_pydot(arbol, titulo, filename, size='8.5'):
	
	f = Digraph(titulo, filename=filename)
	f.attr(size=size)

	# si no tiene padre es Nodo raiz, graficamos con doble círculo
	#if self.parent == None 
	#		grafico.attr('node', shape='doublecircle')

	f = arbol.graficar(f)

	f.view()
