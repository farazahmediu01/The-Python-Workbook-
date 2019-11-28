import sys

from PyQt5.QtWidgets import *


class Window(QWidget):


    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Hello")

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("Media Squad")
        layout.addWidget(label, 0, 0)


app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
