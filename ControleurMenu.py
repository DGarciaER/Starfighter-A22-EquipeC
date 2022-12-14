import tkinter as tk
from tkinter import *
from functools import partial


class ControleurMenu(tk.Frame):
    def __init__(self):
        self.timerMoveMissile = 0.03
        self.timerMoveAsteroide = 0.03
        self.timerCreateAsteroide = 3
        self.timerCreateOvnis = 2
        self.timerMoveOvnis = 0.03
        self.vitesseOvni = 4

    
    def niveau(self, level):
        if level.niveau == "facile":
            self.timerMoveMissile = 0.03
            self.timerMoveAsteroide = 0.03
            self.timerCreateAsteroide = 5
            self.timerCreateOvnis = 5
            self.timerMoveOvnis = 0.03
            self.vitesseOvni = 2
            print("facile")
        
        elif level.niveau == "moyen":
            self.timerMoveMissile = 0.03
            self.timerMoveAsteroide = 0.03
            self.timerCreateAsteroide = 3
            self.timerCreateOvnis = 3
            self.timerMoveOvnis = 0.03
            self.vitesseOvni = 5
            print("moyen")

        elif level.niveau == "difficile":
            self.timerMoveMissile = 0.03
            self.timerMoveAsteroide = 0.03
            self.timerCreateAsteroide = 1
            self.timerCreateOvnis = 0.5
            self.timerMoveOvnis = 0.03
            self.vitesseOvni = 10
            print("fadicafasdcile")
        

class Choix:
    def __init__(self):
        pass

    def afficherChoixLevel(self,menu,level):
    #creation de la fenetre
        fenetreLevel = tk.Tk()
        fenetreLevel.title("Choix du niveau")
        fenetreLevel.geometry("300x300")
        buttonsContainerAlignement = tk.Canvas(fenetreLevel, highlightthickness=0)
        buttonsContainerAlignement.pack() # pour centrer et donner un padding
        buttonEasyLevel = Button(buttonsContainerAlignement, text="Facile", command=level.level_facile)
        buttonMediumLevel = Button(buttonsContainerAlignement, text="Moyen", command=level.level_moyen)
        buttonHardLevel = Button(buttonsContainerAlignement, text="Difficile", command=level.level_difficile)
        buttonCommencer = Button(buttonsContainerAlignement, text="Commencer", command=partial(menu.niveau, level))
        buttonCommencer.grid(column=1, row=4,padx=15, pady=10)
        buttonEasyLevel.grid(column=1, row=1,padx=15, pady=10)
        buttonMediumLevel.grid(column=1, row=2, padx=15, pady=10)
        buttonHardLevel.grid(column=1, row=3, padx=15, pady=10)