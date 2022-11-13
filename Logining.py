import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets

from Static import yandex1
from modelPath import model




class Yandex1(QtWidgets.QMainWindow, yandex1.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py

        super().__init__()
        self.login = None
        self.password = None
        self.setupUi(self)
        # обработка нажатий
        self.pushButton.clicked.connect(self.onClickLogining)
        self.pushButton_2.clicked.connect(self.onClickRegistrate)

    # нажимаем на кнопку 'зарегистрироваться'
    def onClickRegistrate(self):
        from Registrate import window
        window.show()
        self.hide()


    # нажимаем на кнопку 'вход'
    def onClickLogining(self):

        if self.pushButton:
            # берем текст из полей
            self.login = self.lineEdit_3.text()
            self.password = self.lineEdit.text()

            if self.login and self.password:
                # проверяем есть ли такой пользователь
                if model.Yandex1(self.login, self.password):
                    self.rum = open("RamCash/currentUser", "w")
                    if model.isUser(self.login):
                        s = model.isUser(self.login, 1)[0][0]
                        self.rum.write(str(s))
                    self.rum.close()
                    from Categiories import windowPR
                    windowPR.show()
                    self.hide()
                else:
                    print("not such login or password")
                    pass
                    # write not such user and try registrate
            else:
                print("enter login or password")
                # написать ввести чего-нибудь если не введено
                pass


def LoginWindow():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Yandex1()  # Создаём объект класса ExampleApp

    window.show()  # Показываем окно
    sys.exit(app.exec_())  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    LoginWindow()  # то запускаем функцию main()
