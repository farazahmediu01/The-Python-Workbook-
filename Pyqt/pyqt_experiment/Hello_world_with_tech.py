from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])

window = QtWidgets.QWidget(windowTitle='Tech with Tim PyQt5')
window.setGeometry(700, 150, 280, 80)

hello_msg = QtWidgets.QLabel('<h1>Media Squad.</h1>', parent=window)
hello_msg.move(60,15)

window.show()
app.exec_()
