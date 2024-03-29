# ------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

from training import *
from test import *

import webbrowser
import os


class MatplotlibWidget(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        loadUi("window.ui", self)

        self.setWindowTitle("C4.5 con atributos continuos")

        self.crear_modelo.clicked.connect(self.procesar_dataset) #boton para disparar el training
        self.examinar.clicked.connect(self.buscar_archivo) #boton para buscar el dataset de training
        self.ver_arbol.clicked.connect(self.verArbol)  # boton para "ver arbol"
        self.examinar_test.clicked.connect(self.buscar_archivo_test) #boton para buscar el dataset de test
        self.examinar_modelo.clicked.connect(self.buscar_modelo) #boton para buscar el modelo ".data"
        self.examinar_pred_punto.clicked.connect(self.buscar_modelo_punto)  # boton para buscar el modelo ".data" en "Predecir punto"
        self.testear.clicked.connect(self.test)  # boton para disparar el testeo
        self.predecir.clicked.connect(self.predecir_punto)  # boton para disparar la prediccion de un punto

        #Menubar
        self.actionTutorial.triggered.connect(self.ver_tutorial) #para ver el tutorial
        self.actionFormato.triggered.connect(self.ver_formato)  # para ver el formato de entrada

        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))

    def update_graph(self, dataset):

        if dataset.empty:
            return

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.clear()

        ax = plt.gca()
        for line in ax.lines:
            self.MplWidget.canvas.axes.plot(line.get_xdata(), line.get_ydata(), color="orange")
            self.MplWidget.canvas.axes.set_xlabel('X')
            self.MplWidget.canvas.axes.set_ylabel('Y')

        colors = np.where(dataset['clase'] == 1, 'b', 'k')  # clase 1 = azul // clase0 = negro

        x = dataset['x'].to_numpy()
        y = dataset['y'].to_numpy()

        self.MplWidget.canvas.axes.scatter(x=x,y=y, c=colors, s=25)
        self.MplWidget.canvas.axes.set_title('C4.5 con atributos continuos - 1:AZUL - 0:NEGRO')

        self.MplWidget.canvas.draw()
        plt.close()


    # buscar archivo para training
    def buscar_archivo(self):
        dirpath = os.getcwd()
        path = dirpath + "/datasets"
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Seleccione CSV", path, "CSV Files (*.csv )")

        if fileName:
            self.input_file.setText(fileName)

    # disparar el proceso de entrenamiento
    def procesar_dataset(self):
        if self.input_file.text():
            try:
                d = QDialog()
                d.setFixedSize(200,50)
                d.setWindowTitle('Por favor esperar ...')
                d.show()
                dataset_path = self.input_file.text()
                dataset = train(dataset_path)
                self.update_graph(dataset)
                self.ver_arbol.setEnabled(True)
            except:
                print("Hubo un problema durante el procesamiento del dataset. Por favor revisar el formato de entrada como se indica en el Menu")




    # buscar archivo de modelo .DATA en "testear modelo"
    def buscar_modelo(self):
        dirpath = os.getcwd()
        path = dirpath + "/modelos"
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Seleccione DATA", path , "DATA Files (*.data )")

        if fileName:
            self.input_file_model.setText(fileName)


    # buscar archivo de modelo .DATA en "predecir punto"
    def buscar_modelo_punto(self):
        dirpath = os.getcwd()
        path = dirpath + "/modelos"
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Seleccione DATA", path, "DATA Files (*.data )")

        if fileName:
            self.input_file_model_punto.setText(fileName)


    # buscar archivo para testing
    def buscar_archivo_test(self):
        dirpath = os.getcwd()
        path = dirpath + "/datasets"
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Seleccione CSV", path, "CSV Files (*.csv )")

        if fileName:
            self.input_file_test.setText(fileName)


    # disparar el proceso de testing y devuelve una lista con datos de las 2 tablas (incorrectas, correctas)
    def test(self):
        if self.input_file_test.text() and self.input_file_model.text():
            test_dataset_path   = self.input_file_test.text()
            model_path          = self.input_file_model.text()
            predicciones = test(test_dataset_path, model_path)

            while (self.corr_tableWidget.rowCount() > 0):
                    self.corr_tableWidget.removeRow(0);

            #while (self.nopred_tableWidget.rowCount() > 0):
             #       self.nopred_tableWidget.removeRow(0);

            while (self.incorr_tableWidget.rowCount() > 0):
                    self.incorr_tableWidget.removeRow(0);

            rowPosition = self.corr_tableWidget.rowCount()  # añado cada item a la tabla correctos
            if len(predicciones['correctos']) > 0:
                for row in predicciones['correctos']:
                    self.corr_tableWidget.insertRow(rowPosition)
                    self.corr_tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(row['x'])))
                    self.corr_tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(row['y'])))
                    self.corr_tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(row['clase'])))
                    rowPosition += 1

            #rowPosition = self.nopred_tableWidget.rowCount()  # añado cada item a la tabla incosistentes
            #for row in predicciones['inciertos']:
             #   self.nopred_tableWidget.insertRow(rowPosition)
             #   self.nopred_tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(row['x'])))
             #   self.nopred_tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(row['y'])))
             #   self.nopred_tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(row['clase'])))
             #   rowPosition += 1

            rowPosition = self.incorr_tableWidget.rowCount() # añado cada item a la tabla incorrectos
            for row in predicciones['incorrectos']:
                self.incorr_tableWidget.insertRow(rowPosition)
                self.incorr_tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(row['x'])))
                self.incorr_tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(row['y'])))
                self.incorr_tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(row['clase'])))
                self.incorr_tableWidget.setItem(rowPosition, 3, QTableWidgetItem(str(row['pred'])))
                rowPosition += 1

        return


    def predecir_punto(self):
        if self.input_punto_x.text() and self.input_punto_y.text() and self.input_file_model_punto.text():

            x = self.input_punto_x.text()
            y = self.input_punto_y.text()
            punto = {'x':float(x.replace(',','.')), 'y':float(y.replace(',','.'))}

            path_modelo = self.input_file_model_punto.text()

            clase = test_punto(path_modelo, punto)

            if clase is not None:
                self.resultado_clase.display(clase)

        return

    def verArbol(self):
        try:
            webbrowser.open('arbol.pdf', new=2)
        except:
            pass

    def ver_tutorial(self): #para ver el tutorial
        dirpath = os.getcwd()
        path = 'file://'+ dirpath + '/tutorial/ayuda/index.html'
        try:
            webbrowser.open(path, new=2)
        except:
            pass


    def ver_formato(self): #para ver el formato de entrada de datasets
        dirpath = os.getcwd()
        path = 'file://'+ dirpath + '/tutorial/formato/index.html'
        try:
            webbrowser.open(path, new=2)
        except:
            pass


app = QApplication([])
window = MatplotlibWidget()
window.tabWidget.setCurrentIndex(0)
window.show()
app.exec_()