# import QtWidgets to get access to GUI.
import sys
from PyQt5 import QtWidgets


def window():
    # create an application object for event loop.
    app = QtWidgets.QApplication(sys.argv)

    # create a Qwidget as top level window.
    w = QtWidgets.QWidget()

    # name that window.
    w.setWindowTitle('Media Squad')

    # show our window.
    w.show()

    # start an event loop.
    sys.exit(app.exec_())


window()
