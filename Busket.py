from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize, QRect, QMargins
from PyQt5 import QtWidgets, uic
import sys

from PyQt5 import QtCore, QtGui

from Static import yandex5

from modelPath import model
class Yandex5(QtWidgets.QMainWindow, yandex5.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)








    def ProductCategory(self):
        s = self.sender().objectName()






windowPR = Yandex5()
