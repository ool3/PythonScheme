import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout
from qt import Ui_MainWindow


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.default_settings()
        self.winner_people = True
        self.pushButton_2.clicked.connect(self.step_run)
        self.pushButton.clicked.connect(self.change_stones)

    def default_settings(self):
        self.plainTextEdit.setReadOnly(True)

    def step_run(self):
        if self.lineEdit.text():
            number = int(self.lineEdit.text())
            if int(self.lcdNumber.value()) > 0:
                if number <= 3:
                    self.lcdNumber.display(str(int(self.lcdNumber.value()) - number))
                    self.plainTextEdit.insertPlainText('Игрок взял -- {}\n'.format(number))
                    print(self.lcdNumber.value())
                    if int(self.lcdNumber.value()) >= 1:
                        self.robot_grap()
                    self.check_winner()
                else:
                    self.label_3.setText('Вы ввели больше чем 3')
            else:
                self.label_3.setText('Вы не ввели количество камней')

    def robot_grap(self):
        print('---------------------', self.lcdNumber.value())
        if int(self.lcdNumber.value()) >= 1:
            if int(self.lcdNumber.value()) % 2 == 0:
                self.lcdNumber.display(str(int(self.lcdNumber.value()) - 2))
                self.plainTextEdit.insertPlainText('Компьютер взял -- 2\n')
                if int(self.lcdNumber.value()) <= 0:
                    self.winner_people = False
            else:
                if int(self.lcdNumber.value()) != 1:
                    self.lcdNumber.display(str(int(self.lcdNumber.value()) - 3))
                    self.plainTextEdit.insertPlainText('Компьютер взял -- 3\n')
                else:
                    self.lcdNumber.display(str(int(self.lcdNumber.value()) - 1))
                    self.plainTextEdit.insertPlainText('Компьютер взял -- 1\n')
                if int(self.lcdNumber.value()) <= 0:
                    self.winner_people = False
            self.check_winner()

    def change_stones(self):
        self.label_3.setText('')
        self.plainTextEdit.clear()
        self.lcdNumber.display(str(self.spinBox.value()))
        self.robot_grap()

    def check_winner(self):
        if int(self.lcdNumber.value()) <= 0:
            if self.winner_people:
                self.label_3.setText('Выиграл человек')
            else:
                self.label_3.setText('Компьютер выиграл, хахаха')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
