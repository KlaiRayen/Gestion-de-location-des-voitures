from PyQt5.QtWidgets import QMessageBox

class controle_saisie:
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
    def verif_mat(self,ch):
        i=0
        ch1=""
        while(ch[i].isnumeric()):
            i=i+1
            if i>2 or i<1:
                self.warn("la matricule doit etre sous la forme : [0-9]+tn[0-9]+")
                return False
        
        if(not(ch[i]=='t' and ch[i+1]=='n')):
            return False
        i=i+2
        if(len(mat)-i>4 or ch[i:].isnumeric==False):
            return False
        return True
        
        
        
        