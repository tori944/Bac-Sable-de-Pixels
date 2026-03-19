from init import *
from random import *

class Cellule :
    global NbColumn

    listeCellules = []

    def __init__(self, coA, coB, column):
        Cellule.listeCellules.append(self)

        self.id = Cellule.listeCellules.index(self)
        self.etat = 0

        self.column = column

        self.coA = coA
        self.coB = coB

        self.rec = canvas.create_rectangle(coA, coB, coA+10, coB+10, fill='black', outline="grey")

        # canvas.tag_bind(self.rec, "<Button-1>", self.clicG) 
        # canvas.tag_bind(self.rec, "<Button-3>", self.clicD)
        canvas.focus_set()                                  # pour le clavier
        canvas.bind("<Key>", self.clavier)                  # idem
        #canvas.bind("<KeyPress>", self.clavier)                  # idem
        canvas.tag_bind(self.rec, "<Button-1>", self.clicG)  # pour le clic gauche
        canvas.tag_bind(self.rec, "<Button-3>", self.clicD)  # pour le clic gauche
        

    ###### Les Voisines Id ######

    def get_id (self):
        return self.id 
    
    def get_etat (self):
        return self.etat
    
    def get_column (self):
        return self.column

    def set_etat (self, etat, couleur):  
        self.etat = etat
        canvas.itemconfig(self.rec, fill=couleur) 

    def voisinesID (self): # liste des id des voisines 

        myId = self.get_id()
        myColumn = self.get_column()
        
        idVoisines = [NbColumn-1, NbColumn, NbColumn+1, -1, 1, (-NbColumn)-1, (-NbColumn), (-NbColumn)+1]   # en réalité ce id voisine  = ces_valeurs + self.id

        if myColumn == NbColumn-1 :     # si les cellules sont hors du tableau coté droit
            del idVoisines[7]
            del idVoisines[4]
            del idVoisines[2]
        
        if myColumn == 0 :              # si les cellules sont hors du tableau coté gauche
            del idVoisines[5]
            del idVoisines[3]
            del idVoisines[0]

        listeVoisinesID = []

        for i in (idVoisines):          # ne prendre que celle qui figure dans la liste (ne dépasse ni en haut ni en bas)
            if 0 <= myId + i < len(Cellule.listeCellules):
                listeVoisinesID.append(myId+i)

        return listeVoisinesID


    def clicG (self, event):
        print("il y a eu un clic gauche")
        canvas.itemconfig(self.rec, fill = "orange")    
        
    def clicD (self, event):
        print("il y a eu un clic droit")   
        
    def clavier (self, event):
        touche = event.keysym
        print("il y a eu une touche pressé : ", touche)
