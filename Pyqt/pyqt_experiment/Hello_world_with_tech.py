import sys
from PyQt5 import QtWidgets


app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setWindowTitle('Real\'s PyQt5')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)


hello_msg = QtWidgets.QLabel('<h1>Media Squad.</h1>', parent=window)
hello_msg.move(60,15)

window.show()
sys.exit(app.exec_())
