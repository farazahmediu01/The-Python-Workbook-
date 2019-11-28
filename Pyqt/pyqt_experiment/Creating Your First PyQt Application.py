
import sys
# import QApplication, QLabel and QWidgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *

# Create instance of QApplication 
# it is like initialzing boject(app)
# if (sys.argv) not works try ([]) empty list.
app = QApplication(sys.argv) 


# Creating an instance for your Application GUI.
window = QWidgets()
window.setWindowTitle("Media Squad")
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)
