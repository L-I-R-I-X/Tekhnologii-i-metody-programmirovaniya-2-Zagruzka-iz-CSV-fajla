"""Tekhnologii-i-metody-programmirovaniya-2-Zagruzka-iz-CSV-fajla"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from design import Ui_MainWindow
import pandas as pd

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.radioButtonAll.clicked.connect(self.showAll)
        self.ui.radioButtonHigh.clicked.connect(self.showHighDensity)
        self.ui.radioButtonLow.clicked.connect(self.showLowDensity)
        
        self.data = pd.read_excel("1.xls", skiprows=5)
        self.setTable()
        self.showAll()
    
    def setTable(self):
        headers = ["Регион", "Площадь (тыс. км²)", "Население (тыс.)", 
                   "Плотность (чел/км²)", "Города", "ПГТ"]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        
        for i in range(6):
            self.ui.tableWidget.horizontalHeader().setSectionResizeMode(
                i, QHeaderView.ResizeToContents)
    
    def showAll(self):
        self.ui.radioButtonAll.setChecked(True)
        self.ui.tableWidget.setRowCount(len(self.data))
        
        for r in range(len(self.data)):
            self.ui.tableWidget.setItem(r, 0, QTableWidgetItem(str(self.data.iloc[r, 0])))
            self.ui.tableWidget.setItem(r, 1, QTableWidgetItem(str(self.data.iloc[r, 1])))
            self.ui.tableWidget.setItem(r, 2, QTableWidgetItem(str(self.data.iloc[r, 2])))
            self.ui.tableWidget.setItem(r, 3, QTableWidgetItem(str(self.data.iloc[r, 3])))
            self.ui.tableWidget.setItem(r, 4, QTableWidgetItem(str(self.data.iloc[r, 4])))
            self.ui.tableWidget.setItem(r, 5, QTableWidgetItem(str(self.data.iloc[r, 5])))
    
    def showHighDensity(self):
        self.ui.radioButtonHigh.setChecked(True)
        filtered_data = self.data[self.data.iloc[:, 3] > 10]
        
        self.ui.tableWidget.setRowCount(len(filtered_data))
        
        for i in range(len(filtered_data)):
            r = filtered_data.index[i]
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.data.iloc[r, 0])))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.data.iloc[r, 1])))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(self.data.iloc[r, 2])))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(str(self.data.iloc[r, 3])))
            self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(str(self.data.iloc[r, 4])))
            self.ui.tableWidget.setItem(i, 5, QTableWidgetItem(str(self.data.iloc[r, 5])))
    
    def showLowDensity(self):
        self.ui.radioButtonLow.setChecked(True)
        filtered_data = self.data[self.data.iloc[:, 3] < 10]
        
        self.ui.tableWidget.setRowCount(len(filtered_data))
        
        for i in range(len(filtered_data)):
            r = filtered_data.index[i]
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.data.iloc[r, 0])))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.data.iloc[r, 1])))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(self.data.iloc[r, 2])))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(str(self.data.iloc[r, 3])))
            self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(str(self.data.iloc[r, 4])))
            self.ui.tableWidget.setItem(i, 5, QTableWidgetItem(str(self.data.iloc[r, 5])))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = MyWindow()
    application.show()
    sys.exit(app.exec_())