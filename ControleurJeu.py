from ModeleJeu import CarreRouge
from VueJeu import VueJeu
import tkinter as tk
import c31Geometry2 as c31



class ControleurJeu(tk.Frame):
    def __init__(self, container, window=None):
        super().__init__(window)
        self.vueJeu = VueJeu()
        self.window = window
        
        self.carreRouge = CarreRouge(container)
        # self.carreRouge.carreRouge.canvas.bind("<Motion>", self.moveCR)
        #self.vueJeu.afficherCarreRouge(self.carreRouge.carreRouge)



    def my_callback(self,event):
          print( str(event.x) +","+ str(event.y))#affiche position en x et y de la souris



    def moveCR(self, e): # move Carré Rouge
        """
        Cette méthode permet de bouger le carré rouge dans le canvas.
        parametre:
        event
        """  
        self.carreRouge.carreRouge.translateTo(c31.Vecteur(e.x, e.y))
        self.carreRouge.carreRouge.set_position(c31.Vecteur(e.x,e.y))
        self.vueJeu.afficherCarreRouge(self.carreRouge.carreRouge)
                
       
        


    

    


    
        

       
        

        

