import sys
from PyQt5 import QtWidgets, QtGui

def window():
    
    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()
    w.setWindowTitle('PyQt5_')
    
    L1 = QtWidgets.QLabel(w)
    L1.setText('Hello Python')
    L1.move(200, 55)

    L2 = QtWidgets.QLabel(w)
    L2.setPixmap(QtGui.QPixmap(r'C:\Users\faraz\OneDrive\Desktop\happy\Colour Sumatra\logo.png'))
    L2.move(80, 70)
    
    L3 = QtWidgets.QLabel(w)
    L3.setText("How are you")
    L3.move(200, 370)

    w.setGeometry(500, 200, 450, 450)
    w.show()
    sys.exit(app.exec_())

window()
