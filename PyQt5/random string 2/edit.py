import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from main import Ui_MainWindow
from random import choice


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.all_operations()

    def all_operations(self):
        self.pushButton.clicked.connect(self.get_text)

    def get_text(self):
        with open('lines.txt', 'r') as f:
            a = choice(f.read().split('\n'))
            if a != '':
                self.textBrowser.setText(a)
                self.textBrowser.setStyleSheet('font-family:Segoe Script; font-size:15px')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = Main()
    application.show()

    sys.exit(app.exec())
