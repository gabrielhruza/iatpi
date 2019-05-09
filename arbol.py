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

	def export(self, titulo, filename, size='8.5'):
		f = Digraph(titulo, filename=filename)
		f.attr(size=size)
		raiz = self.raiz()
		raiz.graficar(f)
		f.view()


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
		pass

class Hoja(object):
	"""docstring for Hoja"""
	def __init__(self, parent = None, clase = None, cant = None):
		super(Hoja, self).__init__()
		
		self.parent 	= parent
		self.clase  	= clase
		self.cant 		= cant

	# retorna la sintaxis de pydot para una Hoja
	def graficar(self, grafico):
		pass

