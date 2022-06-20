class client:
    
    def __init__(self,nom,prenom,age,cin,adem,num,ad):
        self.l=[]
        self.l.append(nom);
        self.l.append(prenom);
        self.l.append(age);
        self.l.append(cin);
        self.l.append(adem);
        self.l.append(num);
        self.l.append(ad);

    
    def affichage(self):
        print(self.l)