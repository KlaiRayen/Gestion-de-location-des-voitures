
class agence:
    def __init__(self):
        self.liste_v=[]
        self.liste_cl=[]
        self.liste_loc=[]

    def ajout_loc(self,l):
        self.liste_loc.append(l)
    def ajout_voiture(self,l):
        self.liste_v.append(l)
    def ajout_client(self,l):
        self.liste_cl.append(l)
    
    def afficher(self):
        print(self.liste_v)
        print(self.liste_cl)
    
    def rechercher_voiture(self,mat):
        for i in self.liste_v:
            if i[0]==mat:
                return i
        return None
    def rechercher_cl(self,mat):
        for i in self.liste_cl:
            if i[3]==mat:
                return i
        return None
    
    def rechercher_loc(self,num):
        for i in self.liste_loc:
            if i[0]==num:
                return i
        return None
    
    def supprimer_voiture_mat(self,v):
        self.liste_v.remove(v)
        
    def supprimer_client_cin(self,v):
        self.liste_cl.remove(v)
        
        
    def get_prix(self,mat):
        for i in self.liste_v:
            if i[0]==mat :
                return i[5]
            
    def change_loc(self,mat):
        for i in range(len(self.liste_v)):
            if self.liste_v[i][0]==mat:
                self.liste_v[i][3]="0"
                
    def verif_dispo(self):
        for i in self.liste_v:
            if i[3]=="1":
                return True
        return False
    
    def cin_valide(self,cin):
        for i in range(len(self.liste_cl)):
            if self.liste_cl[i][3]==cin:
                return True
        return False
        
    def num_valide(self,num):
        for i in self.liste_loc:
            if str(i[0])==num:
                return True
        return False
    def verif_mat(self,ch):
        ch1=""
        if len(ch)==0 and len(ch)<4 :
            return False
        i=0
        while(ch[i].isnumeric()):
            ch1=ch1+ch[i]
            i=i+1
            if i+1>len(ch):
                return False
        if(i==0):
            return False
        if(not(ch[i]=='t' and ch[i+1]=='n')):
            return False
        
        if(int(ch1[:len(ch1)-1])==0):
            return False
        if i>3 or i<1:
            return False
        
        
        i=i+2
        if(len(ch[i:])>4 or len(ch[i:])==0 or ch[i:].isnumeric()==False):
            return False
        if(int(ch[i:])==0):
            return False
        return True
    
    def verif_coul(self,coul):
        for i in coul:
            if i.isnumeric():
                return False
        return True
    
    def verif_alph(self,nom):
        for i in nom:
            if(i.isnumeric()):
                return False
        return True
    def verif_age(self,age):
        for i in age:
            if(i.isalpha() or i==' '):
                return False
        return True
    
    def verif_date(self,dt):
        if(len(dt)!=10):
            return False
        if(dt[2]!='/' and dt[5]!='/'):
            return False
        jj=dt[0]+dt[1]
        mm=dt[3]+dt[4]
        aa=dt[6]+dt[7]+dt[8]+dt[9]
        if(jj.isnumeric==False or mm.isnumeric==False or aa.isnumeric==False):
            return False
        if ( int(jj)<=0 or int(jj)>31 or int(mm)<=0 or int(mm)>12 or int(aa)<1900 or int(aa)>2022):
            return False
        
    def verif_mail(self,ch):
        for i in ch:
            if i==' ':
                return False
        i=0
        while(ch[i]!='@'):
            i=i+1
            if(i==len(ch)-1):
                return False
        ch1=ch[i:]
        if(ch1!="@gmail.com"):
            return False           
        return True
        