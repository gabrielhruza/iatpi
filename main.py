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

    def update_graph(self, dataset):

        self.MplWidget.canvas.axes.clear()

        ax = plt.gca()
        for line in ax.lines:
            self.MplWidget.canvas.axes.plot(line.get_xdata(), line.get_ydata())

        colors = np.where(dataset['clase'] == 1, 'b', 'k')  # clase 1 = azul // clase0 = negro

        x = dataset['x'].to_numpy()
        y = dataset['y'].to_numpy()
        self.MplWidget.canvas.axes.scatter(x=x,y=y, c=colors, s=25)

        self.MplWidget.canvas.axes.set_title('C4.5 con atributos continuos')

        self.MplWidget.canvas.draw()


    def buscar_archivo(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Seleccione CSV", "", "CSV Files (*.csv );;All Files (*)")

        if fileName:
            self.input_file.setText(fileName)

    def procesar_dataset(self):
        if self.input_file.text():
            dataset_path = self.input_file.text()
            dataset = train(dataset_path)
            self.update_graph(dataset)
            window.tabWidget.setCurrentIndex(1)


app = QApplication([])
window = MatplotlibWidget()
window.tabWidget.setCurrentIndex(0)
window.show()
app.exec_()