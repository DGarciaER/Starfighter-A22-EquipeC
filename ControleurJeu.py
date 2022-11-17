
from VueJeu import VueJeu
from tkinter import *
import tkinter as tk
import c31Geometry2 as c31



class ControleurJeu(tk.Frame):
    def __init__(self, container, window=None):
        super().__init__(window)
        # self.vueJeu = VueJeu()
        self.window = window
        
        #self.carreRouge = CarreRouge(container)
        #self.vaisseaux = Vaisseau(container)
        #self.vaisseaux.img_2.canvas
        #self.carreRouge.carreRouge.canvas.bind("<Motion>", self.moveCR)
        #self.vueJeu.afficherCarreRouge(self.carreRouge.carreRouge)

        
        




    # def my_callback(self,event):
    #       print( str(event.x) +","+ str(event.y))#affiche position en x et y de la souris


    #Add Image To canvas
    

    # def moveCR(self, event): # move Carré Rouge
    #     """
    #     Cette méthode permet de bouger le carré rouge dans le canvas.
    #     parametre:
    #     event
    #     """  
    #     global img
    #     img = PhotoImage(file="C:/Img/vaisseau.gif")
    #     self.my_img = self.my_canvas.create_image(event.x,event.y, image=img)#x=0, y=0
    #     self.my_label.config(text="Coordinates: x" + str(event.x) + "y : " + str(event.y) )
        # self.carreRouge.carreRouge.translateTo(c31.Vecteur(e.x, e.y))
        # self.carreRouge.carreRouge.set_position(c31.Vecteur(e.x,e.y))
        # self.vueJeu.afficherCarreRouge(self.carreRouge.carreRouge)

class Mouvement:
    def __init__(self):
        pass



    #fait bouger le vaisseau
    def moveVaisseau(self,e):
        pass
        # global imgVaisseau
        # On ajoute cette ligne pour ne pas dupliquer des vaisseaux en utilisant toujours le même vaisseau

        #Récupérer l'image de Vaisseau et reduire sa taille avec la méthode subsample


        # Créer une instance de Vaisseau et l'afficher dans l'aire de jeu en lui donnant une position x, y
        # instanceVaisseau = aireDeJeu.create_image(e.x,e.y, image=imgVaisseau)#x=0, y=0
        # self.positionVaiseau['x'] = e.x
        # self.positionVaiseau['y'] = e.y

    # def moveAsteroid(self,e):
    #     instanceAsteroid  = aireDe


                
       
        


    

    


    
        

       
        

        

