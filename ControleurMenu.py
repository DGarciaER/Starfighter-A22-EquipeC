import tkinter as tk
from tkinter import *
from functools import partial
from tkinter import simpledialog
import csv


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
        buttonEnregistrer = Button(buttonsContainerAlignement, text="Enregistrer", command=partial(enregistrer.askUsername))
        buttonCommencer.grid(column=1, row=4,padx=15, pady=10)
        buttonEasyLevel.grid(column=1, row=1,padx=15, pady=10)
        buttonMediumLevel.grid(column=1, row=2, padx=15, pady=10)
        buttonHardLevel.grid(column=1, row=3, padx=15, pady=10)
        buttonEnregistrer.grid(column=2, row=2, padx=15)

class Enregistrer:
    def __init__(self):
        self.username = ""

    def openCSV(self, score, username):
        '''Fonction pour enregistrer les noms d'utilisateurs ainsi que leurs scores pour la session

        :param score: le score de la partie (format 00:00:00) enregistre dans une liste a chauque partie fini, et le sauvegarde dans le fichier csv que quand l'utilisateur rentre son nom (ou non)
        :type score: string 
        :param username: le nom d'utilisateur insire dans avec le boutton "Quitter" ou "Nouvelle score"
        :type username: string
        '''
        f = open('score.csv', 'a', newline='')
        writer = csv.writer(f)
        writer.writerow([username, score])
        f.close()

    def setUsername(self, x):
        '''Setter pour le username. Utilise dans le main pour prendre le nom avec simpledialogs.askstring. Ensuite on utilise le username dans openCSV()
        
        :param x: le return de la fonction simpledialogs.askstring, c'est a dire le nom d'utilisateur entree par l'usager
        :type x: string
        '''
        if not x == None: # La fonction simpledialogs.askstring a deux boutton, 'OK' et 'Cancel'. Quand on appuie sur 'OK' la fonction retourne ce qu'il y a dans le text box (string
            # vide si on n'ecrit rien) et le type None quand on appuie sur cancel. 
            self.username = x + "\n"
        else:
            self.username = x


    def askUsername(self):
        """Fonction pour demander le nom de lutilisateur. Cette fonctione est appelle lorsque lutilisateur clique sur nouvelle session ou quitter"""
        #simpledialog demande le nom a lutilisateur
        self.setUsername(simpledialog.askstring("Save", "Entrer votre nom pour enregistrer"))
        #si il clique sur annuler, rien ne se passe
        if self.username == None:
            pass
        # elif jeu.username == "\n":
        #     jeu.listScore = []
        if len(self.username) > 0:
            #ecrire dans le ficheier
            self.openCSV(3,self.username)
        # else:
        #     if len(jeu.listScore) != 0:

        #         jeu.openCSV(jeu.listScore, jeu.username)
        #         jeu.listScore = []