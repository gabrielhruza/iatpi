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

		#return f

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

		#caso base
		#print("caso base")
		if self is None:
			return

		#caso general

		#print("caso general")

		# graficar el nodo
		grafico.attr('node', shape='box')

		# graficar las ramas con su etiqueta
		nodo_actual 	= self.label #+ "_" + str(self.level)
		nodo_izquierdo 	= self.lc.label #+ "_" + str(self.lc.level)
		nodo_derecho 	= self.rc.label #+ "_" + str(self.rc.level)

		if nodo_izquierdo is not None:
			grafico.edge(nodo_actual, nodo_izquierdo, "<=")
			self.lc.graficar(grafico)

		if nodo_derecho is not None:
			grafico.edge(nodo_actual, nodo_derecho, ">")
			self.rc.graficar(grafico)


class Hoja(object):
	"""docstring for Hoja"""
	def __init__(self, parent = None, clase = None, cant = None):
		super(Hoja, self).__init__()
		
		self.parent 	= parent
		self.clase  	= clase
		self.cant 		= cant

	# retorna la sintaxis de pydot para una Hoja
	def graficar(self, grafico):
		return grafico

