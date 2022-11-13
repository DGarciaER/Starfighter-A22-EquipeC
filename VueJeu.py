from tkinter import Canvas

class VueJeu:

    def afficherCarreRouge(self, carreRouge):
        """Cette méthode affiche le carré rouge."""
        carreRouge.draw()
        
        
    
             
    def clear(self, container):
        """cette methose suprime la fenetre tout ce qui est dans la fenetre"""
        container = container.grid_slaves()
        for widget in container:
            widget.destroy()
    
