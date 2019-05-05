# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\users\gabi\Desktop\cosas\tree\qtdesigner.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from training import *

class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # frame principal
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 20, 800, 800))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # barra de pestañas
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 821, 491)) #debe ser adaptable
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 771, 81))
        self.groupBox.setObjectName("groupBox")

        # input buscar archivo
        self.input_archivo = QtWidgets.QLineEdit(self.groupBox)
        self.input_archivo.setGeometry(QtCore.QRect(130, 20, 511, 31))
        self.input_archivo.setObjectName("input_archivo")

        self.archivo = QtWidgets.QLabel(self.groupBox)
        self.archivo.setGeometry(QtCore.QRect(70, 30, 47, 13))
        self.archivo.setObjectName("archivo")

        # boton examinar
        self.examinar = QtWidgets.QPushButton(self.groupBox)
        self.examinar.setGeometry(QtCore.QRect(660, 20, 101, 31))
        self.examinar.setObjectName("examinar")
        self.examinar.clicked.connect(self.buscar_archivo)

        # boton procesar
        self.procesar = QtWidgets.QPushButton(self.tab)
        self.procesar.setGeometry(QtCore.QRect(330, 110, 101, 31))
        self.procesar.setObjectName("procesar")
        self.procesar.clicked.connect(self.procesar_dataset)

        # pestaña "Ingresar parámetros"
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setGeometry(QtCore.QRect(0, 40, 791, 391))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.tree_clasifier = QtWidgets.QLabel(self.frame_2)
        self.tree_clasifier.setGeometry(QtCore.QRect(0, 0, 791, 391))
        self.tree_clasifier.setText("")
        self.tree_clasifier.setPixmap(QtGui.QPixmap("tree.png"))
        self.tree_clasifier.setAlignment(QtCore.Qt.AlignCenter)
        self.tree_clasifier.setWordWrap(True)
        self.tree_clasifier.setObjectName("tree_clasifier")

        self.grafico_resultado = QtWidgets.QLabel(self.tab_2)
        self.grafico_resultado.setGeometry(QtCore.QRect(340, 10, 101, 21))
        self.grafico_resultado.setObjectName("grafico_resultado")

        # pestaña "Resultados"
        self.tabWidget.addTab(self.tab_2, "")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # pestaña "Test resultado
        self.tab_test = QtWidgets.QWidget()
        self.tab_test.setObjectName("tab_test")
        self.tabWidget.addTab(self.tab_test, "Test")

        # barra de herramientas
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 818, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuInicio = QtWidgets.QMenu(self.menuBar)
        self.menuInicio.setObjectName("menuInicio")
        self.menuAyuda = QtWidgets.QMenu(self.menuBar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuInicio.addAction(self.actionSalir)
        self.menuBar.addAction(self.menuInicio.menuAction())
        self.menuBar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "C4.5 con Atributos Continuos"))
        self.groupBox.setTitle(_translate("MainWindow", "Parámetros"))
        self.input_archivo.setText(_translate("MainWindow", ""))
        self.archivo.setText(_translate("MainWindow", "Archivo:"))
        self.examinar.setText(_translate("MainWindow", "Examinar"))
        self.procesar.setText(_translate("MainWindow", "Procesar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Ingresar parámetros"))
        self.grafico_resultado.setText(_translate("MainWindow", "Gráfico Obtenido"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Resultados"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_test), _translate("MainWindow", "Test"))
        self.menuInicio.setTitle(_translate("MainWindow", "Inicio"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Ctrl+Q"))

    def procesar_dataset(self):
        dataset_path = self.input_archivo.text()
        resultado = train(dataset_path)
        pixmap = QtGui.QPixmap(resultado)
        self.tree_clasifier.setPixmap(pixmap)
        self.tree_clasifier.setAlignment(QtCore.Qt.AlignCenter)
        self.tabWidget.setCurrentIndex(1)

    def buscar_archivo(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Seleccione CSV", "", "CSV Files (*.csv );;All Files (*)")
        if fileName:
            self.input_archivo.setText(fileName)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.tabWidget.setCurrentIndex(0)
    MainWindow.show()
    sys.exit(app.exec_())

