# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rech_loc_cin.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from voiture import voiture
from agence import agence
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.columns=["Num","CIN","Date de location","Durée","Montant"]
        

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.columns[section])

        

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return 5

class Ui_Form(object):
    def __init__(self,agence):
        self.ag = agence
        self.l=[]
    def rechercher(self):
        mat = self.lineEdit_4.text()
        alternative=[]
        ok=0
        for ins in self.ag.liste_loc:
            l=[]
            if(mat==ins[2]):
                ok=1
                l.append(ins[0])
                l.append(ins[1])
                l.append(ins[3])
                l.append(ins[4])
                l.append(ins[5])
                alternative.append(l)
        if ok==0:
            self.warn("Matricule invalide")
        self.modal=TableModel(alternative)
        self.tableView_2.setModel(self.modal)
        self.horizontal_header = self.tableView_2.horizontalHeader()
        self.vertical_header = self.tableView_2.verticalHeader()
        self.horizontal_header.setSectionResizeMode(3)
        self.tableView_2.horizontalHeader().setStretchLastSection(True)
                       
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
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(560, 550)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 561, 551))
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(0, -5, 561, 551))
        self.label_4.setStyleSheet("border-image: url(:/images/abstract-gradient-blue-to-white-sq-format-thomas-woolworth.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 561, 551))
        self.label_5.setStyleSheet("background-color:rgba(0,0,0,120); \n"
"border-radius:7px; ")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 421, 41))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_6.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color :rgba(255,255,255,0.7)")
        self.label_6.setObjectName("label_6")
        self.tableView_2 = QtWidgets.QTableView(self.widget)
        self.tableView_2.setGeometry(QtCore.QRect(10, 150, 541, 391))
        self.tableView_2.setStyleSheet("")
        self.tableView_2.setObjectName("tableView_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"background-color : qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(20,47,78,0.6),stop:1 rgba(85,98,112,0.6));\n"
"color:rgba(255,255,255,0.8);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"background-color : qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(40,67,98,219),stop:1 rgba(105,118,132,226));\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"background-color : qlineargradient(spread:pad,x1:0,y1:0.505682,x2:1,y2:0.477,stop:0  rgba(20,47,78,0.6),stop:1 rgba(85,98,112,0.8));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 40, 221, 41))
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
        
        self.pushButton_2.clicked.connect(self.rechercher)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        alternative=[]
        self.modal=TableModel(alternative)
        self.tableView_2.setModel(self.modal)
        self.horizontal_header = self.tableView_2.horizontalHeader()
        self.vertical_header = self.tableView_2.verticalHeader()
        self.horizontal_header.setSectionResizeMode(3)
        self.tableView_2.horizontalHeader().setStretchLastSection(True)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "Recherche des locations par Matricule :"))
        self.pushButton_2.setText(_translate("Form", "Rechercher"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Matricule"))
import res_msgbox_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

