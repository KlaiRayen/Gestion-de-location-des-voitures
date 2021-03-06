# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'supp_loc.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


from PyQt5.QtWidgets import QMessageBox
from location import location
from agence import agence

class Ui_Form(object):
    def __init__(self,agence):
        self.ag = agence
        self.l=[]

    def succ(self,str):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(str)
        msgBox.setWindowTitle("Ajout reussie")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
    
    def warn(self,str):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(str)
        msgBox.setWindowTitle("Msg Error")      
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()         
        
    def supploc(self):
        num = self.lineEdit_4.text()
        if (self.ag.num_valide(num)==False):
            self.warn("Numero invalide")
        else:
            for i in self.ag.liste_loc:
                if str(i[0])==num:
                    mat=i[2]
                    v = self.ag.rechercher_voiture(mat)
                    v[3]="1"
                    self.ag.liste_loc.remove(i)
                    self.succ("Suppression reussie")
                    self.lineEdit_4.setText("")
                    break
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(510, 450)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 511, 261))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 511, 251))
        self.label.setStyleSheet("border-image: url(:/images/abstract-gradient-blue-to-white-sq-format-thomas-woolworth.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 511, 261))
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,180); \n"
"border-radius:7px; ")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(130, 30, 291, 31))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_3.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color :rgba(255,255,255,0.7)")
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(260, 110, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :white;\n"
"padding-bottom:7px ;")
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(140, 170, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"background-color : qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(20,47,78,0.6),stop:1 rgba(85,98,112,0.6));\n"
"color:rgba(255,255,255,0.6);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color : qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(40,67,98,219),stop:1 rgba(105,118,132,226));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"background-color : qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0  rgba(20,47,78,0.6),stop:1 rgba(85,98,112,0.6));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 210, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
"background-color : qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(20,47,78,0.6),stop:1 rgba(85,98,112,0.6));\n"
"color:rgba(255,255,255,0.6);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_3:hover{\n"
"background-color : qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(40,67,98,219),stop:1 rgba(105,118,132,226));\n"
"}\n"
"QPushButton#pushButton_3:pressed{\n"
"background-color : qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0  rgba(20,47,78,0.6),stop:1 rgba(85,98,112,0.6));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(70, 110, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :white;\n"
"padding-bottom:7px ;")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.pushButton.clicked.connect(self.supploc)
        self.pushButton_3.clicked.connect(Form.close)  
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Suppression d\'une location"))
        self.pushButton.setText(_translate("Form", "Supprimer"))
        self.pushButton_3.setText(_translate("Form", "Fermer"))
        self.label_4.setText(_translate("Form", "Numero de location :"))
import res_msgbox_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
