import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from qt import Ui_MainWindow


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.shake)

    def shake(self):
        odd_list = []
        with open('file.txt') as f:
            print('hi')
            text = f.read().split('\n')

        for i in range(0, len(text)):
            if i % 2 != 0:
                print(text[i])
                self.textBrowser.append(text[i])
            else:
                odd_list.append(text[i])
        for i in odd_list:
            self.textBrowser.append(i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
