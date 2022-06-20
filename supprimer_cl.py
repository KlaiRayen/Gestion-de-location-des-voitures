# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'supprimer_cl.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


from agence import agence

class Ui_Form(object):
    def __init__(self,agence):
        self.ag = agence
        self.v = None
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

    def rechercher(self):            
        mat =self.lineEdit.text()
        self.v = self.ag.rechercher_cl(mat)
        if(self.v is None):
            self.warn("Client invalide")
            self.lineEdit_3.setText("");
            self.lineEdit_6.setText("");
            self.lineEdit_10.setText("");
            self.lineEdit_8.setText("");
            self.lineEdit_12.setText("");
            self.lineEdit_14.setText("");

        else:
            self.lineEdit_3.setText(self.v[0]);
            self.lineEdit_6.setText(self.v[1]);
            self.lineEdit_8.setText(self.v[2]);
            self.lineEdit_12.setText(self.v[4]);
            self.lineEdit_10.setText(self.v[5]);
            self.lineEdit_14.setText(self.v[6]);

            
    def supprimer(self):
        if(self.v is None):
            self.warn("client invalide")
        else:
            self.ag.supprimer_client_cin(self.v)
            self.succ("Client supprimé avec succés")
            self.lineEdit.setText("");
            self.lineEdit_3.setText("");
            self.lineEdit_6.setText("");
            self.lineEdit_10.setText("");
            self.lineEdit_8.setText("");
            self.lineEdit_12.setText("");
            self.lineEdit_14.setText("");

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(397, 558)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-1, -11, 401, 571))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 5, 401, 571))
        self.label.setStyleSheet("border-image: url(:/images/1610495931_1596555352_873352025.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 401, 561))
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,180); \n"
"border-radius:7px; ")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color : white ;\n"
"color:rgba(255,255,255,0.6);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 60, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit.setText("")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(80, 120, 241, 31))
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
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 160, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 160, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(40, 210, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setClearButtonEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 210, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setClearButtonEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setGeometry(QtCore.QRect(40, 260, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_7.setClearButtonEnabled(False)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setGeometry(QtCore.QRect(120, 260, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setPlaceholderText("")
        self.lineEdit_8.setClearButtonEnabled(False)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_9.setGeometry(QtCore.QRect(40, 310, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setPlaceholderText("")
        self.lineEdit_9.setClearButtonEnabled(False)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_10.setGeometry(QtCore.QRect(120, 310, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setPlaceholderText("")
        self.lineEdit_10.setClearButtonEnabled(False)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_11.setGeometry(QtCore.QRect(40, 360, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setPlaceholderText("")
        self.lineEdit_11.setClearButtonEnabled(False)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_12.setGeometry(QtCore.QRect(170, 360, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setPlaceholderText("")
        self.lineEdit_12.setClearButtonEnabled(False)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_13.setGeometry(QtCore.QRect(40, 410, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setPlaceholderText("")
        self.lineEdit_13.setClearButtonEnabled(False)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_14.setGeometry(QtCore.QRect(120, 410, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,0.7);\n"
"padding-bottom:7px ;")
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setPlaceholderText("")
        self.lineEdit_14.setClearButtonEnabled(False)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 520, 241, 31))
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
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 470, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4{\n"
"background-color : qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(20,47,78,0.6),stop:1 rgba(85,98,112,0.6));\n"
"color:rgba(255,255,255,0.6);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_4:hover{\n"
"background-color : qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(40,67,98,219),stop:1 rgba(105,118,132,226));\n"
"}\n"
"QPushButton#pushButton_4:pressed{\n"
"background-color : qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0  rgba(20,47,78,0.6),stop:1 rgba(85,98,112,0.6));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.rechercher)
        self.pushButton_4.clicked.connect(self.supprimer)
        self.pushButton_3.clicked.connect(Form.close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Suppréssion d\'un client"))
        self.lineEdit.setPlaceholderText(_translate("Form", "CIN"))
        self.pushButton.setText(_translate("Form", "Rechercher"))
        self.lineEdit_4.setText(_translate("Form", "Nom :"))
        self.lineEdit_5.setText(_translate("Form", "Prenom :"))
        self.lineEdit_7.setText(_translate("Form", "Age :"))
        self.lineEdit_9.setText(_translate("Form", "Num :"))
        self.lineEdit_11.setText(_translate("Form", "Adresse e-mail :"))
        self.lineEdit_13.setText(_translate("Form", "Adresse :"))
        self.pushButton_3.setText(_translate("Form", "Fermer"))
        self.pushButton_4.setText(_translate("Form", "Supprimer"))
import res_msgbox_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
