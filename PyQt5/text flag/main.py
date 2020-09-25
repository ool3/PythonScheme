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
        self.checked_btn = []
        self.pushButton.clicked.connect(self.change_text)

    def change_text(self):
        self.checked_btn.clear()
        for i in self.groupBox.children():
            for j in i.children():
                try:
                    print(j.isChecked())
                    if j.isChecked():
                        self.checked_btn.append(j.text())

                except Exception:
                    pass
        string_output = 'Прдметы:'
        couner = 0
        for i in self.checked_btn:
            if couner == 0 or couner == 1:
                string_output += ', ' + i
            else:
                string_output += ' и ' + i
            couner += 1
        self.label_4.setText(string_output)
        print(self.checked_btn)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
