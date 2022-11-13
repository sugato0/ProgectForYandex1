from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize, QRect, QMargins
from PyQt5 import QtWidgets, uic
import sys

from PyQt5 import QtCore, QtGui

from Static import yandex4

from modelPath import model
class Yandex4(QtWidgets.QMainWindow, yandex4.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_5.clicked.connect(self.CatAndBas)
        self.pushButton_6.clicked.connect(self.CatAndBas)
    def abstractBlockProduct(self):
        ram = open("RamCash/currentCategoryId")
        answ = model.ProductIDS(int(ram.read()))

        ram.close()
        key = 400
        if answ:

            for i in answ:
                self.verticalGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
                self.verticalGroupBox.setMinimumSize(QtCore.QSize(371, 361))
                self.verticalGroupBox.setMaximumSize(QtCore.QSize(371, 361))
                self.verticalGroupBox.setObjectName("verticalGroupBox")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
                self.verticalLayout.setObjectName("verticalLayout")
                self.label = QtWidgets.QLabel(self.verticalGroupBox)
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap(f"{i[4]}"))
                self.label.setObjectName("label")
                self.verticalLayout.addWidget(self.label)
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                self.verticalLayout.addLayout(self.horizontalLayout_5)
                self.label_3 = QtWidgets.QLabel(self.verticalGroupBox)
                self.label_3.setObjectName("label_3")
                self.verticalLayout.addWidget(self.label_3)
                self.label_2 = QtWidgets.QLabel(self.verticalGroupBox)
                self.label_2.setObjectName("label_2")
                self.verticalLayout.addWidget(self.label_2)
                self.pushButton_4 = QtWidgets.QPushButton(self.verticalGroupBox)
                self.pushButton_4.setObjectName(f"{i[0]}")
                self.verticalLayout.addWidget(self.pushButton_4)
                self.verticalLayout_4.addWidget(self.verticalGroupBox)
                self.label_3.setText(f"{i[2]}")
                self.label_2.setText(f"{i[1]}")
                self.pushButton_4.setText("Добавить в корзину")

    def ProductDef(self):
        s = self.sender().objectName()


        ram = open("RamCash/currentUser","rb")
        answ = model.GetBasIdByUser(ram.read())[0]
        print(answ)
        model.BusketProductsAdd(answ,s)
        ram.close()


    def CatAndBas(self):
        s = self.sender().objectName()
        if s == "Categories":
            from Categiories import windowPR
            windowPR.show()
            self.hide()
        else:
            from Busket import windowPR
            windowPR.show()
            self.hide()

windowPR = Yandex4()
