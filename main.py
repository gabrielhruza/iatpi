# ------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from training import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

from matplotlib.figure import Figure

class MatplotlibWidget(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        loadUi("window.ui", self)

        self.setWindowTitle("C4.5 con atributos continuos")

        self.crear_modelo.clicked.connect(self.procesar_dataset)
        self.examinar.clicked.connect(self.buscar_archivo)

        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))

    def update_graph(self, figura):

        fig = plt.figure()

        fig = FigureCanvas(fig)

        self.MplWidget.canvas.show()
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot([1,2,3,4,5],[3,4,5,6,7])
        self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
        self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')

        self.MplWidget.canvas.draw()


    def buscar_archivo(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Seleccione CSV", "", "CSV Files (*.csv );;All Files (*)")

        if fileName:
            self.input_file.setText(fileName)


    def procesar_dataset(self):
        if self.input_file.text():
            dataset_path = self.input_file.text()
            figura = train(dataset_path)
            self.update_graph(figura)


app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()