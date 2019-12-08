from PyQt5 import QtWidgets

def sys():
    app = QtWidgets.QApplication([])
    
    window = QtWidgets.QWidget(windowTitle='Logo with Label')
    window.setGeometry(500, 200, 450, 450)

    window.show()
    app.exec_()
sys()
