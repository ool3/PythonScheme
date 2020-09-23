import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from qt import Ui_MainWindow


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow, 
        # остальное без изменений
        self.setupUi(self)
        self.pushButton.clicked.connect(self.find_date)
        self.all_dates = {}

    def find_date(self):
        string_date = self.calendarWidget.selectedDate().getDate()
        if int(string_date[1]) <= 9:
            string_date = (string_date[0], '0' + str(string_date[1]), string_date[-1])
        if int(string_date[2]) <= 9:
            string_date = (string_date[0], str(string_date[1]), '0' + str(string_date[-1]))
        line_edit = self.lineEdit.text()
        a = f'{string_date[0]}-{string_date[1]}-{string_date[2]} - {line_edit}'
        self.all_dates[
            f'{string_date[0]}-{string_date[1]}-{string_date[2]}-{self.timeEdit.time().toString()}'] = line_edit
        self.listWidget.clear()
        for key in sorted(self.all_dates.keys()):
            self.listWidget.addItem(f'{key} - {self.all_dates[key]}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
