# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2dates.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


from PyQt5.QtCore import Qt
from agence import agence    
import datetime
import time


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.columns=["Matricule","Marque","Couleur","Prix de location","Date"]
        

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
    
    
        
    
    
    def rechercher(self):
        d1 = self.dateTimeEdit.text()
        d2 = self.dateTimeEdit_2.text()
        newdate1 = time.strptime(d1, "%d/%m/%Y %H:%M")
        newdate2 = time.strptime(d2, "%d/%m/%Y %H:%M")
        alternative=[]
        if (newdate1>=newdate2):
            self.warn("date invalide")
        else:
            for i in self.ag.liste_loc:
                l=[]
                date_1 = datetime.datetime.strptime(str(i[3]), "%d/%m/%Y %H:%M")
                d3=str(date_1 + datetime.timedelta(days=int(i[4])))
                ch=d3[8]+d3[9]+"/"+d3[5]+d3[6]+"/"+d3[0]+d3[1]+d3[2]+d3[3]+ " " + d3[11]+d3[12]+d3[13]+d3[14]+d3[15]
                if (d1==i[3] and ch==d2):
                    v= self.ag.rechercher_voiture(i[2])
                    l.append(v[0])
                    l.append(v[1])
                    l.append(v[2])
                    l.append(v[5])
                    l.append(v[4])
                    alternative.append(l)
                    if(len(alternative)==0):
                        self.warn("pas de voitures lou??es entre ces deux dates")

            self.modal=TableModel(alternative)
            self.tableView_2.setModel(self.modal)
            self.horizontal_header = self.tableView_2.horizontalHeader()
            self.vertical_header = self.tableView_2.verticalHeader()
            self.horizontal_header.setSectionResizeMode(3)
            self.tableView_2.horizontalHeader().setStretchLastSection(True)
    def warn(self,str):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(str)
        msgBox.setWindowTitle("Msg Error")      
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_() 
                
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(561, 578)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 561, 591))
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(0, -5, 561, 581))
        self.label_4.setStyleSheet("border-image: url(:/images/abstract-gradient-blue-to-white-sq-format-thomas-woolworth.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 561, 581))
        self.label_5.setStyleSheet("background-color:rgba(0,0,0,120); \n"
"border-radius:7px; ")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 450, 41))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_6.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color :rgba(255,255,255,0.7)")
        self.label_6.setObjectName("label_6")
        self.tableView_2 = QtWidgets.QTableView(self.widget)
        self.tableView_2.setGeometry(QtCore.QRect(10, 180, 541, 391))
        self.tableView_2.setStyleSheet("")
        self.tableView_2.setObjectName("tableView_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 130, 221, 31))
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
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(80, 60, 51, 41))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_7.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color :rgba(255,255,255,0.7)")
        self.label_7.setObjectName("label_7")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(130, 60, 141, 51))
        self.dateTimeEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,1);\n"
"padding-bottom:7px ;")
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(290, 60, 41, 41))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_8.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color :rgba(255,255,255,0.7)")
        self.label_8.setObjectName("label_8")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(340, 60, 141, 51))
        self.dateTimeEdit_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border : none ;\n"
"border-bottom : 2px solid rgba(105,118,132,255);\n"
"color :rgba(255,255,255,1);\n"
"padding-bottom:7px ;")
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")

        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        alternative=[]
        self.modal=TableModel(alternative)
        self.tableView_2.setModel(self.modal)
        self.horizontal_header = self.tableView_2.horizontalHeader()
        self.vertical_header = self.tableView_2.verticalHeader()
        self.horizontal_header.setSectionResizeMode(3)
        self.tableView_2.horizontalHeader().setStretchLastSection(True)
        
        self.pushButton_2.clicked.connect(self.rechercher)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "Recherche des voitures lou??es entre 2 dates"))
        self.pushButton_2.setText(_translate("Form", "Rechercher"))
        self.label_7.setText(_translate("Form", "Du :"))
        self.label_8.setText(_translate("Form", "au"))
import res_msgbox_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
