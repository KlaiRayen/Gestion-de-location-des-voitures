# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ajout_client.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QMessageBox
from agence import agence    
from client import client
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    
    def __init__(self,agence):
        self.ag = agence
    
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

        
    
    def remplir(self):
        if(len(self.lineEdit.text())==0 or self.ag.verif_alph(self.lineEdit.text())==False):
            self.warn("Nom invalide")
        elif(len(self.lineEdit_2.text())==0 or self.ag.verif_alph(self.lineEdit_2.text())==False):
            self.warn("Prenom invalide")
        elif(len(self.lineEdit_3.text())==0 or self.ag.verif_age(self.lineEdit_3.text())==False):
            self.warn("Age invalide")
        elif(len(self.lineEdit_4.text())!=8 or self.ag.verif_age(self.lineEdit_4.text())==False):
            self.warn("CIN invalide")
        elif(len(self.lineEdit_5.text())==0 or self.ag.verif_mail(self.lineEdit_5.text())==False):
            self.warn("E-mail invalide")
        elif(len(self.lineEdit_6.text())!=8 or self.ag.verif_age(self.lineEdit_6.text())==False):
            self.warn("Numéro invalide")
        elif(len(self.textEdit.toPlainText())==0):
            self.warn("Adresse invalide")
        else:
            c = client(self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text(),self.lineEdit_5.text(),self.lineEdit_6.text(),self.textEdit.toPlainText()) 
            self.ag.ajout_client(c.l)
            self.succ("Client ajouté avec succées")
            self.lineEdit_3.setText("");
            self.lineEdit_2.setText("");
            self.lineEdit_4.setText("");
            self.lineEdit_5.setText("");
            self.lineEdit_6.setText("");
            self.lineEdit.setText("");
            self.textEdit.setText("");

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(298, 652)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 301, 651))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 301, 651))
        self.label.setStyleSheet("border-image: url(:/images/grbl.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 301, 641))
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,180); \n"
"border-radius:7px; ")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(100, 10, 231, 31))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_3.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color :rgba(255,255,255,0.7)")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 110, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 170, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 230, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 290, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 350, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setClearButtonEnabled(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(30, 410, 231, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 540, 231, 31))
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
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 590, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"background-color : qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(20,47,78,0.6),stop:1 rgba(85,98,112,0.6));\n"
"color:rgba(255,255,255,0.6);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"background-color : qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(40,67,98,219),stop:1 rgba(105,118,132,226));\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"background-color : qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0  rgba(20,47,78,0.6),stop:1 rgba(85,98,112,0.6));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.remplir)
        self.pushButton_2.clicked.connect(Form.close)  

    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Ajouter client"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Nom"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Prenom"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Age"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "CIN"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Adresse E-mail"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "Num de télephone"))
        self.textEdit.setPlaceholderText(_translate("Form", "Adresse"))
        self.pushButton.setText(_translate("Form", "Ajouter"))
        self.pushButton_2.setText(_translate("Form", "Annuler"))
import res_msgbox_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())