import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout
from notebook_ui import Ui_MainWindow


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Записная книжка')
        self.pushButton.clicked.connect(self.change_widget)

    def change_widget(self):
        name = self.lineEdit.text()
        tel = self.lineEdit_2.text()
        self.listWidget.addItem(f'{name} {tel}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
