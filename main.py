import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from code1 import Ui_MainWindow
from agence import agence
class main:
    
    def __init__(self):
        self.ag = agence()
        self.fen = QtWidgets.QMainWindow()
        self.ui =Ui_MainWindow(self.ag)
        self.ui.setupUi(self.fen)
        self.fen.show()
        

app = QtWidgets.QApplication(sys.argv)
window=main()
app.exec_()


        

    
    
   