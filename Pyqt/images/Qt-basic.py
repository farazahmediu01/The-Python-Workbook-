from PyQt5 import QtWidgets, QtGui

app    = QtWidgets.QApplication([])
window = QtWidgets.QWidget(windowTitle='Pythagorus')

L1     = QtWidgets.QLabel(window)
L2     = QtWidgets.QLabel(window)

L1.setText('Hello Qt: ')
L2.setText('Along with Python')

window.setGeometry(200,100,1066,568)
window.show()
app.exec()