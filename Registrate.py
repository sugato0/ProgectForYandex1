from PyQt5 import QtWidgets

from Static import yandex2

from modelPath import model


class Yandex2(QtWidgets.QMainWindow, yandex2.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py

        super().__init__()
        self.password = None
        self.login = None
        self.setupUi(self)
        

        # обработка нажатий
        self.pushButton.clicked.connect(self.RegANDProductWindow)

    def RegANDProductWindow(self):
        self.login = self.lineEdit_4.text()
        self.password = self.lineEdit_2.text()
        if self.login or self.password:
            if model.Yandex2(self.login, self.password):
                self.rum = open("RamCash/currentUser", "w")
                if model.isUser(self.login):
                    s = model.isUser(self.login, 1)[0][0]
                    self.rum.write(str(s))
                self.rum.close()
                from Categiories import windowPR
                windowPR.show()
                self.hide()
            else:
                print("произошла ошибка попробуйте снова")
        else:
            print("Not correct login and password")

window = Yandex2()  # Создаём объект класса ExampleApp

# Показываем окно
