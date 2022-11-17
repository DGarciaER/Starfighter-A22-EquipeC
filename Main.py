import tkinter as tk
from ControleurJeu import ControleurJeu
from ModeleJeu import AireDeJeu, Vaiseau, Ovni, Missile
from VueJeu import VueJeu
from tkinter import *
import threading
import random
from threading import Timer


if __name__ == "__main__":

    # créer une fenetre tk avec un titre, un background et des dimensions
    couleurTheme = "#41157A"

     # Si je fait par exemple print(tailleADJ["height"]), le output va être 500.


    def randomPosition():
        return random.randint(0, 500)


    root = tk.Tk()
    root.title("Star Fighter")
    root.config(background= couleurTheme)
    root.geometry("510x680")

    # créer un containter et le centrer dans la fenetre tk
    mainContainer = tk.Frame(root, background= couleurTheme)
    mainContainer.pack() # pour centrer et donner un padding
    
    # créer un titre de jeu et le mettre dans un grid en lui donnant du padding
    titre = tk.Label(mainContainer, text="Star Fighter", fg='#FFFC33', background= couleurTheme)
    titre.configure(font=("MV Boli", 25, "bold"))
    titre.grid(column=1, row=0, padx=10, pady=10)
                    
    # créer l'aire de jeu et le mettre dans un grid en lui donnant du padding
   
    aireDeJeu = AireDeJeu(mainContainer)
    vaisseau = Vaiseau(aireDeJeu)

    listeOvnis = []
    ovni = Ovni(aireDeJeu, randomPosition(),-3)


    # créer un container pour afficher les statistiques en meme temps du jeu.
    statsContainer = tk.Canvas(mainContainer, height=20, width=450,background= couleurTheme, highlightthickness=0)
    statsContainer.grid(column=1, row=3, padx=10, pady=5) # pour centrer et donner un padding

    score = tk.Label(statsContainer, text="   Score:  0  ", fg='#FFFD85',background= couleurTheme)
    score.grid(column=1, row=1, padx=10) # pour centrer et donner un padding

    lives = tk.Label(statsContainer, text="   Vies:  0  ", fg='#FFFD85',background= couleurTheme)
    lives.grid(column=2, row=1, padx=10) # pour centrer et donner un padding

    ability = tk.Label(statsContainer, text="   Abilités:  None  ", fg='#FFFD85',background= couleurTheme)
    ability.grid(column=3, row=1, padx=10) # pour centrer et donner un padding

    # créer un container des buttonset le mettre dans un grid en lui donnant du padding
    buttonsContainer = tk.Canvas(mainContainer, background= couleurTheme, highlightthickness=0)
    buttonsContainer.grid(column=1, row=4, padx=10, pady=20) # pour centrer et donner un padding

    couleurButtons = "#E22866"

    # # définir l'objet controleur
    jeu = ControleurJeu(aireDeJeu.canva)

    # créer un button qui commence une nouvelle session et le mettre dans un grid en lui donnant du padding
    buttonNouvSession = tk.Button(buttonsContainer, text="         Button1         ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'))
    buttonNouvSession.grid(column=1, row=1, padx=15)

    # créer un button qui affiche le menu score un nouveau jeu et le mettre dans un grid en lui donnant du padding
    buttonMenuScores = tk.Button(buttonsContainer, text="         Button2         ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'))
    buttonMenuScores.grid(column=2, row=1, padx=15)

    # créer un button quitte du programme et le mettre dans un grid en lui donnant du padding
    buttonQuitter = tk.Button(buttonsContainer, text="         Button3         ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'))
    buttonQuitter.grid(column=3, row=1, padx=15)

    listMissile = []


    # instanceV = vaisseau.instanceVaisseau
    imageV = vaisseau.imageVaisseau
   
    def moveVaisseau(e):

        global imageV
        # On ajoute cette ligne pour ne pas dupliquer des vaisseaux en utilisant toujours le même vaisseau

        #Récupérer l'image de Vaisseau et reduire sa taille avec la méthode subsample


        # Créer une instance de Vaisseau et l'afficher dans l'aire de jeu en lui donnant une position x, y
        imageV = tk.PhotoImage(file='Images/Vaisseau.png').subsample(2,2)

        instanceV = aireDeJeu.canva.create_image(e.x,e.y, image=imageV)#x=0, y=0
        vaisseau.setPositions(e.x,e.y)

        print(vaisseau.x)
        print(vaisseau.y)
        # vaisseau.x = e.x
        # vaisseau.y = e.y
        

    def moveMissile():
        for missile in listMissile:
            aireDeJeu.canva.move(missile.instanceMissile, 0, -10)
            missile.y -=10

            if missile.y <= 0:
                aireDeJeu.canva.delete(missile.instanceMissile)
                listMissile.remove(missile)
                print('deleted')

        wait = Timer(0.03,moveMissile)
        wait.start()

        

    def shoot(event):
        listMissile.append(Missile(aireDeJeu, event.x, event.y))
   

    # # Quand on clique sur le vaisseau et bouge le souris
    aireDeJeu.canva.bind('<Motion>', moveVaisseau)

    # #quand on click sur le vaisseau quelque chose se passe
    aireDeJeu.canva.bind('<Button-1>', shoot)

    wait = Timer(0.03,moveMissile)
    wait.start()
    
    
    # FIN DE PARTIE

    # boocler la fenetre tk
    root.mainloop()