class voiture:
    
    def __init__(self,mat,mar,coul,date,prix):
        self.l=[]
        self.l.append(mat);
        self.l.append(mar);
        self.l.append(coul);
        self.l.append("1");
        self.l.append(date);
        self.l.append(prix);
    
    def affichage(self):
        print(self.l)

    def set_loc(self):
        self.l[3]="0"      
    def set_coul(self,c):
        self.l[2]=c
    def set_prix(self,p):
        self.l[5]=p
        
    