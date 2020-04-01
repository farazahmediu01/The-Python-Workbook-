import sys
from PyQt5 import QtWidgets, uic

def window():    
    app = QtWidgets.QApplication(sys.argv)

    w = uic.loadUi(r"C:\Users\faraz\OneDrive\Desktop\happy\xml.ui")
    #w.setWindowTitle('Media Player')
    w.show()

    sys.exit(app.exec_())

window()

