import c31Geometry2 as c31
import tkinter as tk

class CarreRouge:
    tailleCarreRouge = 40
    
    def __init__(self, container):
        
        # initialisation du Carre Rouge
        couleur = '#ed4242'
        self.carreRouge = c31.Carre(container, c31.Vecteur(225,225),self.tailleCarreRouge,0, couleur, couleur, 0)
        self.imgFile = 'Images/Vaisseau.gif'
        self.img = tk.PhotoImage(file=self.imgFile)
        
        #Evenement pour le carre
        self.img_2 = self.img.subsample(12,12) #on reduit la taille de limage
        # self.image = 
        
        self.carreRouge.canvas.create_image(10,10,anchor=tk.NW, image=self.img_2)




