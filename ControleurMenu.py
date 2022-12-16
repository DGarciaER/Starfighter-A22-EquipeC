import tkinter as tk
from tkinter import *
from functools import partial
from tkinter import simpledialog
import csv

from ModeleJeu import Player



class ControleurMenu(tk.Frame):
    '''
    Cette classe permet de modifier les parametres du jeu (tel que la vitesse des ovnis, le nombre d'ovnis qui apparaissent par secondes, etc.) selon
    la difficulté choisi par l'utilisateur, dans la methode afficherChoixLevel() de la classe Choix.
    '''
    def __init__(self): #Constructeur
        self.commence = False
        self.timerMoveMissile = 0.03
        self.timerMoveAsteroide = 0.03
        self.timerCreateAsteroide = 3   #Taux d'apparition des ovnis, 1 mine chaque x secondes
        self.timerCreateOvnis = 3       #Taux d'apparition des ovnis, 1 mine chaque x secondes
        self.timerMoveOvnis = 0.03
        self.vitesseOvniY = 0
        self.vitesseOvniX = 0
        self.timerShootMine = 2         #Taux d'apparition des mines laissées par les ovnis, 1 mine chaque x secondes
        self.timerCreatePU = 5          #Taux d'apparition des bonus (PowerUp), 1 bonus chaque x secondes
        self.timerMovePU = 0.03
        self.vitessePU = 2              #Vitesse des bonus (PowerUp)

    
    def niveau(self, level, fenetreLevel):
        '''
        Cette methode s'occupe de modifier les reglages du jeu en fonction de la difficulté choisi par l'utilisateur
        '''

        #Si le niveau de difficulte choisi est FACILE:
        if level.niveau == "facile":
            self.timerMoveMissile = 0.03
            self.timerMoveAsteroide = 0.03
            self.timerCreateAsteroide = 1       
            self.timerCreateOvnis = 5           
            self.timerMoveOvnis = 0.03
            self.vitesseOvniY = 2
            self.vitesseOvniX = 6
            self.timerShootMine = 4             
            self.timerCreatePU = 5              
            self.timerMovePU = 0.03
            self.vitessePU = 2                  
            self.commence = True
            fenetreLevel.destroy()
        
        #Si le niveau de difficulte choisi est MOYEN:
        elif level.niveau == "moyen":
            self.timerMoveMissile = 0.03
            self.timerMoveAsteroide = 0.03
            self.timerCreateAsteroide = 3
            self.timerCreateOvnis = 2
            self.timerMoveOvnis = 0.03
            self.vitesseOvniY = 5
            self.vitesseOvniX = 8
            self.timerShootMine = 2.5
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
            self.timerCreateOvnis = 1
            self.timerMoveOvnis = 0.03
            self.vitesseOvniY = 10
            self.vitesseOvniX = 12
            self.timerShootMine = 1.5
            self.timerCreatePU = 5
            self.timerMovePU = 0.03
            self.vitessePU = 2
            self.commence = True
            fenetreLevel.destroy()
        

        

class Choix:
    '''
    Cette classe s'occupe de proposer les differents choix de difficultés du jeu à l'utilisateur. 
    '''
    def __init__(self):
        pass

    def afficherChoixLevel(self,menu,level,jeu):#enregistrer
        #creation de la fenetre pour le choix de la difficulté
        couleurTheme = "#41157A"
        fenetreLevel = tk.Tk()
        fenetreLevel.title("Choix du niveau")
        fenetreLevel.geometry("300x300")
        buttonsContainerAlignement = tk.Canvas(fenetreLevel, highlightthickness=0,background=couleurTheme)
        buttonsContainerAlignement.pack() # pour centrer et donner un padding
        buttonEasyLevel = Button(buttonsContainerAlignement, text="Facile", command=level.level_facile, background='#FFFC33')
        buttonMediumLevel = Button(buttonsContainerAlignement, text="Moyen", command=level.level_moyen, background='#FFFC33')
        buttonHardLevel = Button(buttonsContainerAlignement, text="Difficile", command=level.level_difficile, background='#FFFC33')
        buttonCommencer = Button(buttonsContainerAlignement, text="Commencer", command=partial(menu.niveau, level, fenetreLevel), background='#FFFC33')
        buttonCommencer.grid(column=1, row=4,padx=15, pady=10)
        buttonEasyLevel.grid(column=1, row=1,padx=15, pady=10)
        buttonMediumLevel.grid(column=1, row=2, padx=15, pady=10)
        buttonHardLevel.grid(column=1, row=3, padx=15, pady=10)
        fenetreLevel.mainloop()

class Enregistrer:

    def __init__(self):
        self.username = ""

    def openCSV(self, nom, score,jeu):
        '''Fonction pour enregistrer les noms d'utilisateurs ainsi que leurs scores pour la session

        :param score: le score de la partie (format 00:00:00) enregistre dans une liste a chauque partie fini, et le sauvegarde dans le fichier csv que quand l'utilisateur rentre son nom (ou non)
        :type score: string 
        :param username: le nom d'utilisateur insire dans avec le boutton "Quitter" ou "Nouvelle score"
        :type username: string
        '''
        nom = nom[:-1]
        f = open('score.csv', 'a', newline='')
        temps = "Temps : "+ jeu.minutes_string + ":" + jeu.seconds_string + ":" + jeu.milliseconds_string # Variable utilisé pour sauvegarder le temps de l'utilisateur dans le fichier csv
        nomT = "Nom : " + nom
        scoreT = "Score : " + str(score)
        writer = csv.writer(f)
        
        writer.writerow([nomT, scoreT, temps])
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


    def askUsername(self,player,jeu):
        """Fonction pour demander le nom de lutilisateur. Cette fonctione est appelle lorsque lutilisateur clique sur nouvelle session ou quitter"""
        #simpledialog demande le nom a lutilisateur
        self.setUsername(simpledialog.askstring("Save", "Entrer votre nom pour enregistrer"))
        #si il clique sur annuler, rien ne se passe
        if self.username == None:
            pass
        if len(self.username) > 0:
            #ecrire dans le ficheier
            self.openCSV(self.username,player.score,jeu)#recuper timer, scores


    #
    def deleteScore(self):
        """Fonction pour supprimer les scores """
        
        f = open("score.csv", "w")
        f.truncate()
        f.close()

    def AfficherScores(self):
        """Fonction pour afficher les scores, fonction appelé lorsqu'on click sur le boutton SCORE"""
        
        #creation du widget
        couleurTheme = "#41157A"
        self.fenetreScore = tk.Tk()
        self.fenetreScore.config(background= couleurTheme)
        self.fenetreScore.title("Scores")
        self.fenetreScore.geometry("400x400") # Dimensions
        buttonsContainerAlignement = tk.Canvas(self.fenetreScore, highlightthickness=0, background='#FFFC33')
        buttonsContainerAlignement.pack() # pour centrer et donner un padding
        scoresLabel = Label(buttonsContainerAlignement, text="LES SCORES :",background='#FFFC33')
        scoresLabel.grid(column=1,row=1,padx=15)
        buttonExit = Button(buttonsContainerAlignement, text="Retour",command=self.fenetreScore.destroy, background='#FFFC33')
        buttonSuppimer = Button(buttonsContainerAlignement, text="Supprimer scores",command= self.deleteScore,background='#FFFC33')
        buttonExit.grid(column=2, row=1,padx=15)
        buttonSuppimer.grid(column=3, row=1, padx=15)
        scrollbar = Scrollbar(self.fenetreScore)
        scrollbar.pack( side = RIGHT, fill = Y )
        canvascore = Listbox(self.fenetreScore, yscrollcommand = scrollbar.set )
        
        

        canvascore.pack( fill = BOTH, padx= 50, expand=True )
        scrollbar.config( command = canvascore.yview )

        scores = []  # creation du tableau scores   

        #ouverture du fichier CSV
        with open("score.csv",'r') as r:
            obj = csv.reader(r, delimiter="\n")
            for i in obj:
                ligne = i
                scores.append(ligne)
            print(scores)
        r.close()
        
        #On passe à travers tout les scores
        for i in scores:
            canvascore.insert(END, i)