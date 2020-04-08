import sys

from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])
window = QtWidgets.QWidget(windowTitle='Hello Qt')

window = QtWidgets.QWidget()
window.setWindowTitle('Hello Qt')

print(window.windowTitle())
window.show()

app.exec_()
'''
print("\nsys.version",sys.version)
print("\nsys.implementation.name",sys.implementation.name)
print("\nsys.implementation.version",sys.implementation.version)
print("\nsys.executable",sys.executable)
print("\nsys.path",sys.path)
'''
