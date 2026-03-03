import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from design import Ui_MainWindow
import pandas as pd

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Подключение кнопок
        self.ui.radioButtonAll.clicked.connect(self.showAll)
        self.ui.radioButtonHigh.clicked.connect(self.showHighDensity)
        self.ui.radioButtonLow.clicked.connect(self.showLowDensity)
        
        # Определение пути к файлу данных (для работы и в IDE, и в .exe)
        if getattr(sys, 'frozen', False):
            # Если запущен как .exe
            base_path = os.path.dirname(sys.executable)
        else:
            # Если запущен как скрипт
            base_path = os.path.dirname(os.path.abspath(__file__))
        
        self.data_path = os.path.join(base_path, "1.xls")
        
        try:
            self.data = pd.read_excel(self.data_path, skiprows=5)
            self.setTable()
            self.showAll()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка", 
                f"Не удалось загрузить 1.xls!\nПуть: {self.data_path}\nОшибка: {e}")

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
            for c in range(6):
                self.ui.tableWidget.setItem(r, c, QTableWidgetItem(str(self.data.iloc[r, c])))

    def showHighDensity(self):
        self.ui.radioButtonHigh.setChecked(True)
        filtered_data = self.data[self.data.iloc[:, 3] > 10]
        self.ui.tableWidget.setRowCount(len(filtered_data))
        for i in range(len(filtered_data)):
            r = filtered_data.index[i]
            for c in range(6):
                self.ui.tableWidget.setItem(i, c, QTableWidgetItem(str(self.data.iloc[r, c])))

    def showLowDensity(self):
        self.ui.radioButtonLow.setChecked(True)
        filtered_data = self.data[self.data.iloc[:, 3] < 10]
        self.ui.tableWidget.setRowCount(len(filtered_data))
        for i in range(len(filtered_data)):
            r = filtered_data.index[i]
            for c in range(6):
                self.ui.tableWidget.setItem(i, c, QTableWidgetItem(str(self.data.iloc[r, c])))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = MyWindow()
    application.show()
    sys.exit(app.exec_())