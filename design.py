from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.radioButtonAll = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonAll.setGeometry(QtCore.QRect(20, 20, 150, 25))
        self.radioButtonAll.setObjectName("radioButtonAll")
        self.radioButtonAll.setText("Все регионы")
        
        self.radioButtonHigh = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonHigh.setGeometry(QtCore.QRect(20, 50, 250, 25))
        self.radioButtonHigh.setObjectName("radioButtonHigh")
        self.radioButtonHigh.setText("Плотность > 10 чел/км²")
        
        self.radioButtonLow = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonLow.setGeometry(QtCore.QRect(20, 80, 250, 25))
        self.radioButtonLow.setObjectName("radioButtonLow")
        self.radioButtonLow.setText("Плотность < 10 чел/км²")
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 120, 860, 450))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)