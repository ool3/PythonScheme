import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('p4.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.compare_text)
        self.text_1 = []
        self.counter = 0
        self.counter_2 = 0
        self.setWindowTitle('Антиплагиат 000001V')

    def compare_text(self):
        self.text_1.clear()
        for i in self.plainTextEdit_first.toPlainText().replace(' ', '').split('\n'):
            self.text_1.append(i.split('=')[-1])
        self.counter = len(self.text_1)
        list_2 = self.plainTextEdit_second.toPlainText().replace(' ', '').split('\n')
        print(self.text_1, list_2, self.counter)
        self.counter_2 = len(list_2)
        for i in range(len(list_2)):
            try:
                if ''.join(list_2[i]).split('=')[-1] != self.text_1[i]:
                    print(''.join(list_2[i]).split('=')[-1], self.text_1[i])
                    if self.counter >= 0:
                        self.counter -= 1
                        self.counter_2 -= 1
            except:
                pass
        print()
        if len(list_2) == len(self.text_1):
            number = round(self.counter * 100 / len(self.text_1), 2)
        else:
            if len(list_2) > len(self.text_1):
                number = round((self.counter / len(list_2)) * 100, 2)
            else:
                number = round(self.counter_2 / len(self.text_1) * 100, 2)
        percent = self.doubleSpinBox.value()
        if self.counter <= -1:
            self.counter = 0

        self.statusBar.showMessage('Код похож на {}%'.format(number))
        print(number, percent)
        if number < int(percent):
            self.statusBar.setStyleSheet('background-color: green')
        else:
            self.statusBar.setStyleSheet('background-color: red')

        # Имя элемента совпадает с objectName в QTDesigner


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
