from PyQt5 import QtWidgets, QtGui

app = QtWidgets.QApplication([])

window = QtWidgets.QWidget(windowTitle='Pythagorus')
window.setGeometry(200,100,1066,568)

L1_python = QtWidgets.QLabel(r'<h1>Qt\Python<\h1>', parent=window)
L1_python.move(500,100)

L2_vs = QtWidgets.QLabel(r'<h1>VS</h1>', parent=window)
L2_vs.move(200,300)

L3_cpp = QtWidgets.QLabel(r'<h1>Qt\C++<\h1>',parent=window)
L3_cpp.move(200,500)

P1_qt = QtWidgets.QLabel(window)
P1_qt.setPixmap(QtGui.QPixmap(r'D:\Downloads\python\Python\Programs\visual studio code\Starting from Introduction\Pyqt\images\qt_logo.png'))

P2_py = QtWidgets.QLabel(window)
P2_py.setPixmap(QtGui.QPixmap(r'D:\Downloads\python\Python\Programs\visual studio code\Starting from Introduction\Pyqt\images\python_logo.png'))
#P2_py.move()

P3_cpp = QtWidgets.QLabel(window)
P3_cpp.setPixmap(QtGui.QPixmap(r'D:\Downloads\python\Python\Programs\visual studio code\Starting from Introduction\Pyqt\images\cpp_logo.png'))

window.show()
app.exec_()