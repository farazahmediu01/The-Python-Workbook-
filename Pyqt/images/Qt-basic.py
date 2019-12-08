from PyQt5 import QtWidgets, QtGui

app = QtWidgets.QApplication([])

window = QtWidgets.QWidget(windowTitle='Pythagorus')
window.setGeometry(200,100,1066,568)

L1_python = QtWidgets.QLabel(r'<h1>Qt\Python<\h1>', parent=window)
L1_python.move(200,100)

L2_vs = QtWidgets.QLabel(r'<h1>VS</h1>', parent=window)
L2_vs.move(200,300)

L3_cpp = QtWidgets.QLabel(r'<h1>Qt\C++<\h1>',parent=window)
L3_cpp.move(200,500)

P1     = QtWidgets.QLabel(window)

P2     = QtWidgets.QLabel(window)
P3     = QtWidgets.QLabel(window


window.show()
app.exec()