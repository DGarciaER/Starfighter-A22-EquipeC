import tkinter as tk
from tkinter import *
from functools import partial
from tkinter import simpledialog


class ControleurMenu(tk.Frame):
    def __init__(self):
        self.timerMoveMissile = 0.03
        self.timerMoveAsteroide = 0.03
        self.timerCreateAsteroide = 3
        self.timerCreateOvnis = 2
        self.timerMoveOvnis = 0.03
        self.vitesseOvni = 4

    
    def niveau(self, level):

        # jeu.start_timer()
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

    def afficherChoixLevel(self,menu,level,enregistrer,jeu):
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
        buttonEnregistrer = Button(buttonsContainerAlignement, text="Enregistrer", command=partial(enregistrer.askUsername, jeu))
        buttonCommencer.grid(column=1, row=4,padx=15, pady=10)
        buttonEasyLevel.grid(column=1, row=1,padx=15, pady=10)
        buttonMediumLevel.grid(column=1, row=2, padx=15, pady=10)
        buttonHardLevel.grid(column=1, row=3, padx=15, pady=10)
        buttonEnregistrer.grid(column=2, row=2, padx=15)

class Enregistrer:
    def __init__(self):
        pass

    def askUsername(self,jeu):
        """Fonction pour demander le nom de lutilisateur. Cette fonctione est appelle lorsque lutilisateur clique sur nouvelle session ou quitter"""
        #simpledialog demande le nom a lutilisateur
        jeu.setUsername(simpledialog.askstring("Save", "Entrer votre nom pour enregistrer"))
        #si il clique sur annuler, rien ne se passe
        if jeu.username == None:
            pass
        elif jeu.username == "\n":
            jeu.listScore = []
        else:
            if len(jeu.listScore) != 0:
                jeu.openCSV(jeu.listScore, jeu.username)
                jeu.listScore = []