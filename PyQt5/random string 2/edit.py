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
        try:
            with open('lines.txt') as f:
                a = choice(f.read().split('\n'))
                if a != '':
                    self.textBrowser.setText(a)
                    self.textBrowser.setStyleSheet('font-family:Segoe Script; font-size:15px')
        except Exception:
            with open('lines.txt', 'w') as f:
                f.write('''I believe that holidays should be a change.

Most people like a change. If they live in the country they like to go to a big town and spend their time looking at the shop windows and visiting cinemas, theatres and museums.

If they live in the city, they like to go the some quiet place in the hills or by the sea, do nothing but walking, swimming or lying in the sun.

So, on holidays most people don’t like doing things they have to do all year round.
My friends spend most of their free time driving around the country and sightseeing.
As for me, I find travelling by car very tiring. It makes no difference if I drive a car or just sit as a passenger.
I will try to explain. When I drive, it usually takes too much of me — too much nerves.
When I am a passenger, I always feel tensed as my legs and arms hurt.
It is because I hate too much sitting. So, after driving I’m usually exhausted.

hello

oh my god''')
                self.get_text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = Main()
    application.show()

    sys.exit(app.exec())
