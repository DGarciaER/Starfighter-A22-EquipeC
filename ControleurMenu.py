import tkinter as tk
from tkinter import *
from functools import partial
from tkinter import simpledialog
import csv


class ControleurMenu(tk.Frame):
    '''
    Cette classe permet de modifier les parametres du jeu (tel que la vitesse des ovnis, le nombre d'ovnis qui apparaissent par secondes, etc.) selon
    la difficulté choisi par l'utilisateur, dans la methode afficherChoixLevel() de la classe Choix.
    '''
    def __init__(self): #Constructeur
        self.commence = False
        self.timerMoveMissile = 0.03
        self.timerMoveAsteroide = 0.03
        self.timerCreateAsteroide = 3
        self.timerCreateOvnis = 3
        self.timerMoveOvnis = 0.03
        self.vitesseOvniY = 0
        self.vitesseOvniX = 0
        self.timerShootMine = 2
        self.timerCreatePU = 5
        self.timerMovePU = 0.03
        self.vitessePU = 2

    
    def niveau(self, level, fenetreLevel):
        '''
        Cette methode s'occupe de modifier les reglages du jeu en fonction de la difficulté choisi par l'utilisateur
        '''

        # jeu.start_timer()

        #Si le niveau de difficulte choisi est FACILE:
        if level.niveau == "facile":
            self.timerMoveMissile = 0.03
            self.timerMoveAsteroide = 0.03
            self.timerCreateAsteroide = 1       #Taux d'apparition des ovnis, 1 mine chaque x secondes
            self.timerCreateOvnis = 10           #Taux d'apparition des ovnis, 1 mine chaque x secondes
            self.timerMoveOvnis = 0.03
            self.vitesseOvniY = 2
            self.vitesseOvniX = 6
            self.timerShootMine = 5             #Taux d'apparition des mines laissées par les ovnis, 1 mine chaque x secondes
            self.timerCreatePU = 5              #Taux d'apparition des bonus (PowerUp), 1 bonus chaque x secondes
            self.timerMovePU = 0.03
            self.vitessePU = 2                  #Vitesse des bonus (PowerUp)
            self.commence = True
            fenetreLevel.destroy()
        
        #Si le niveau de difficulte choisi est MOYEN:
        elif level.niveau == "moyen":
            self.timerMoveMissile = 0.03
            self.timerMoveAsteroide = 0.03
            self.timerCreateAsteroide = 3
            self.timerCreateOvnis = 3
            self.timerMoveOvnis = 0.03
            self.vitesseOvniY = 5
            self.vitesseOvniX = 8
            self.timerShootMine = 3
            self.timerCreatePU = 5
            self.timerMovePU = 0.03
            self.vitessePU = 2
            self.commence = True
            fenetreLevel.destroy()
            
        #Si le niveau de difficulte choisi est DIFFICILE:
        elif level.niveau == "difficile":
            self.timerMoveMissile = 0.03
            self.timerMoveAsteroide = 0.03
            self.timerCreateAsteroide = 1
            self.timerCreateOvnis = 0.5
            self.timerMoveOvnis = 0.03
            self.vitesseOvniY = 10
            self.vitesseOvniX = 12
            self.timerShootMine = 4
            self.timerCreatePU = 5
            self.timerMovePU = 0.03
            self.vitessePU = 2
            self.commence = True
            fenetreLevel.destroy()
        

        

class Choix:
    def __init__(self):
        pass

    def afficherChoixLevel(self,menu,level,enregistrer,jeu):
        #creation de la fenetre pour le choix de la difficulté
        fenetreLevel = tk.Tk()
        fenetreLevel.title("Choix du niveau")
        fenetreLevel.geometry("300x300")
        buttonsContainerAlignement = tk.Canvas(fenetreLevel, highlightthickness=0)
        buttonsContainerAlignement.pack() # pour centrer et donner un padding
        buttonEasyLevel = Button(buttonsContainerAlignement, text="Facile", command=level.level_facile)
        buttonMediumLevel = Button(buttonsContainerAlignement, text="Moyen", command=level.level_moyen)
        buttonHardLevel = Button(buttonsContainerAlignement, text="Difficile", command=level.level_difficile)
        buttonCommencer = Button(buttonsContainerAlignement, text="Commencer", command=partial(menu.niveau, level, fenetreLevel))
        buttonEnregistrer = Button(buttonsContainerAlignement, text="Enregistrer", command=partial(enregistrer.askUsername))
        buttonCommencer.grid(column=1, row=4,padx=15, pady=10)
        buttonEasyLevel.grid(column=1, row=1,padx=15, pady=10)
        buttonMediumLevel.grid(column=1, row=2, padx=15, pady=10)
        buttonHardLevel.grid(column=1, row=3, padx=15, pady=10)
        buttonEnregistrer.grid(column=2, row=2, padx=15)
        fenetreLevel.mainloop()

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