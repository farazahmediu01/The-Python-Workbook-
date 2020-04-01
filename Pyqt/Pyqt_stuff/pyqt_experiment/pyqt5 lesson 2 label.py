import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)   # create app object

    w = QtWidgets.QWidget()                  # create window and set title
    w.setWindowTitle('Learning PyQt5')

    L1 = QtWidgets.QLabel(w)                 # add label to the window
    L1.setText('Hello World')                # set text to the label
    L1.move(120, 60)                         # move label

    w.setGeometry(500, 150, 300, 200)        # set window geomatry
    w.show()
    sys.exit(app.exec_())

window()
