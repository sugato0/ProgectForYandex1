import random
import sqlite3


class Yandex1DB:
    def __init__(self, data_base):
        self.con = sqlite3.connect(data_base)

        self.cur = self.con.cursor()

    def Yandex1(self, Login, Password) -> bool:
        arg = (str(Login), str(Password),)

        answ = self.cur \
            .execute("SELECT * FROM 'User' WHERE login = ? AND password = ?;", arg) \
            .fetchall()

        return bool(len(answ))

    def isUser(self, Login,d = 0) -> bool:
        answ = self.cur \
            .execute("SELECT * FROM 'User' WHERE login = ? ;", (str(Login),)) \
            .fetchall()
        if d == 0:
            return bool(len(answ))
        if d == 1:
            return answ

    def categories(self):
        answ = self.cur \
            .execute("SELECT * FROM 'Categories';") \
            .fetchall()
        if not bool(len(answ)):
            print("категорий не имеется")
            return False
        else:
            return answ

    def Yandex2(self, Login, Password) -> bool:
        try:
            if not self.isUser(Login):
                cort = (str(Login), str(Password),random.randint(0,10000000))

                self.cur.execute("INSERT INTO 'User' VALUES (NULL,?,?,?)", cort)
                self.con.commit()
                return True
            else:
                print("такой пользователь уже существует")
        except Exception as e:
            print(e)
            return False

    def ProductIDS(self, category_id):
        try:
            answ = self.cur \
                .execute("SELECT * FROM Product WHERE categories_id = ? ;", (int(category_id),)) \
                .fetchall()
            return answ
        except:
            print("Что-то не так проверьте корректность вводимых данных")

    def BusketProductsAdd(self,basketId, ProductsId):
        try:
            print(ProductsId)
            self.cur.execute("INSERT INTO Basket(id, product_id) VALUES (?,?)", (int(basketId[0]), int(ProductsId),))
            self.con.commit()
        except Exception as e:
            print(e)
    def GetBasIdByUser(self,userId):
        try:
            answ = self.cur \
                .execute("SELECT busket_id FROM User WHERE id = ? ;", (int(userId),)) \
                .fetchall()
            return answ
        except:
            print("Что-то не так проверьте корректность вводимых данных")
    def BusketProductsGet(self,idUser):

        answ = self.cur \
            .execute("SELECT * FROM Basket WHERE id IN (SELECT busket_id FROM User WHERE id = ?)",
                     (int(idUser),))\
            .fetchall()
        if answ:
            return answ
        else:
            print("В корзине пустовато")
            return answ



