from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize, QRect, QMargins
from PyQt5 import QtWidgets, uic
import sys

from PyQt5 import QtCore, QtGui

from Static import yandex3

from modelPath import model
class Yandex3(QtWidgets.QMainWindow, yandex3.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.categories = model.categories()


        for i in self.categories:
            self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.pushButton_2.setMinimumSize(QtCore.QSize(307, 40))
            self.pushButton_2.setObjectName(f"{i[0]}")
            self.pushButton_2.setStyleSheet('QPushButton {background-color: #ffdbd1}')
            self.pushButton_2.setText(f"{i[1]}")
            self.pushButton_2.clicked.connect(self.ProductCategory)
            self.verticalLayout.addWidget(self.pushButton_2)


    def ProductCategory(self):
        s = self.sender().objectName()
        self.ram = open("RamCash/currentCategoryId","w")
        self.ram.write(s)
        self.ram.close()
        from Products import windowPR
        windowPR.show()
        self.hide()





windowPR = Yandex3()
