import sys
import sqlite3
from PyQt5 import QtWidgets
from ui import Ui_MainWindow
from acc import ProfileUI

class ConnectDB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def execute_sql(self, sql, params=None):
        try:
            if params is None:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, params)
            self.connection.commit()
        except sqlite3.DatabaseError as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Exception in _query: {e}")

    def select_sql(self, sql, params=None):
        self.execute_sql(sql, params)
        return self.cursor.fetchall()

    def insert_sql(self, sql, params=None):
        self.execute_sql(sql, params)

    def close_db(self):
        self.cursor.close()
        self.connection.close()

# Класс главного окна, наследующий от QMainWindow и использующий ваш UI
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = ConnectDB("C:/dev/projects/App/db.db")  # Укажите путь к вашей базе данных
        self.ui.pushButton.clicked.connect(self.authenticate)

    def authenticate(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        # Проверка на пустые поля
        if not username or not password:
            self.ui.label_3.setText("Введите данные!")
            return

        # Формирование SQL запроса
        sql = "SELECT * FROM users WHERE username=? AND password=?"

        # Выполнение запроса
        result = self.db.select_sql(sql, (username, password))

        if result:
            level = "Администратор" if username.lower() == "admin" else "Пользователь"
            self.user_data = {"username": username, "password": password, "level": level} # Сохраняем данные пользователя
            self.ui.label_3.setText("Успешный вход!")
            self.open_profile()
        else:
            self.ui.label_3.setText("Ошибка!")

    # Не забудьте добавить метод для закрытия соединения с БД при закрытии приложения
    def closeEvent(self, event):
        self.db.close_db()
        super(MainWindow, self).closeEvent(event)

    def open_profile(self):
        self.close()  # Закрыть текущее окно авторизации
        self.profile_window = ProfileWindow(self.user_data)  # Создаем новое окно профиля
        self.profile_window.show()  # Показываем окно профиля

class ProfileWindow(QtWidgets.QMainWindow):
    def __init__(self, user_data):
        super(ProfileWindow, self).__init__()
        self.ui = ProfileUI()
        self.ui.setupUi(self)
        self.ui.label_3.setText(f"Логин: {user_data['username']}")
        self.ui.label_4.setText(f"Пароль: {user_data['password']}")
        self.ui.label_5.setText(f"Ваш уровень: {user_data['level']}")  # Отображение уровня доступа
        self.ui.pushButton.clicked.connect(self.logout)

    def logout(self):
        self.close()  # Закрываем текущее окно профиля
        self.main_window = MainWindow()  # Создаем новое окно авторизации
        self.main_window.show()  # Показываем окно авторизации

# Функция main, которая запускает приложение
def main():
    app = QtWidgets.QApplication(sys.argv)  # Создание экземпляра QApplication
    main_window = MainWindow()               # Создание экземпляра вашего окна
    main_window.show()                       # Отображение окна
    sys.exit(app.exec_())                    # Запуск основного цикла приложения

if __name__ == '__main__':
    main()