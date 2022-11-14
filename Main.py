import tkinter as tk
from ControleurJeu import ControleurJeu
from tkinter import *
import threading


if __name__ == "__main__":

    # créer une fenetre tk avec un titre, un background et des dimensions
    couleurTheme = "#41157A"

    # un dictionnaire qui contient la longueur et la largeur du canvas Aire De Jeu.
    tailleADJ = {
        "height": 500,
        "width": 450
    } # Si je fait par exemple print(tailleADJ["height"]), le output va être 500.

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
    aireDeJeu = tk.Canvas(mainContainer, height=tailleADJ['height'], width=tailleADJ['width'])
    aireDeJeu.grid(column=1, row=1, padx=20) # pour centrer et donner un padding

    # Récupérer l'image de background et reduire sa taille avec la methode subsample() 
    imgBackground = tk.PhotoImage(file='Images/Background.png').subsample(2,2)

    # Mettre l'image de background dans le canva aireDeJeu
    aireDeJeu.create_image(10,10, image=imgBackground) 

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
    jeu = ControleurJeu(aireDeJeu)

    # créer un button qui commence une nouvelle session et le mettre dans un grid en lui donnant du padding
    buttonNouvSession = tk.Button(buttonsContainer, text="         Button1         ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'))
    buttonNouvSession.grid(column=1, row=1, padx=15)

    # créer un button qui affiche le menu score un nouveau jeu et le mettre dans un grid en lui donnant du padding
    buttonMenuScores = tk.Button(buttonsContainer, text="         Button2         ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'))
    buttonMenuScores.grid(column=2, row=1, padx=15)

    # créer un button quitte du programme et le mettre dans un grid en lui donnant du padding
    buttonQuitter = tk.Button(buttonsContainer, text="         Button3         ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'))
    buttonQuitter.grid(column=3, row=1, padx=15)


    # NOTE cette partie ne doit pas être dans le fichier main
    # DÉBUT DE PARTIE

    #Récupérer l'image de Vaisseau et reduire sa taille avec la méthode subsample
    imgVaisseau = PhotoImage(file='Images/Vaisseau.png').subsample(2,2)

    # Créer une instance de Vaisseau et l'afficher dans l'aire de jeu en lui donnant une position x, y
    instanceVaisseau = aireDeJeu.create_image((tailleADJ['width'] - imgVaisseau.width())/2,400,anchor=NW,image=imgVaisseau)#x=0, y=0
    
    #Récupérer l'image de Ovni et reduire sa taille avec la méthode subsample
    imgOvni = PhotoImage(file='Images/ovni.png').subsample(4,4)

    # Créer une instance de Ovni et l'afficher dans l'aire de jeu en lui donnant une position x, y
    instanceOvni = aireDeJeu.create_image((tailleADJ['width'] - imgOvni.width())/2,90,anchor=NW,image=imgOvni)#x=0, y=0

    #Creer un missile
    laserImg = PhotoImage(file='Images/missile.png')
    

    
    #fait bouger le vaisseau
    def move(e):

        global imgVaisseau
        # On ajoute cette ligne pour ne pas dupliquer des vaisseaux en utilisant toujours le même vaisseau

        #Récupérer l'image de Vaisseau et reduire sa taille avec la méthode subsample
        imgVaisseau = PhotoImage(file='Images/Vaisseau.png').subsample(2,2)

        # Créer une instance de Vaisseau et l'afficher dans l'aire de jeu en lui donnant une position x, y
        instanceVaisseau = aireDeJeu.create_image(e.x,e.y, image=imgVaisseau)#x=0, y=0



    def moveLaser():
        global laser, missileLoop
        #fait monter le missile de 10 px toute les 10 ms
        aireDeJeu.move(laser, 0, -10)
        #rappel la fonction toutes les 100ms
        missileLoop = root.after(10, moveLaser)
        

    def shoot(event):
        global laser, missileLoop
        try:
            root.after_cancel(missileLoop)
            aireDeJeu.delete(laser)
            laser = aireDeJeu.create_image(event.x,event.y, image=laserImg)
            moveLaser()
        except NameError:
            laser = aireDeJeu.create_image(event.x,event.y, image=laserImg)
            moveLaser()
   

    # Quand on clique sur le vaisseau et bouge le souris
    aireDeJeu.bind('<Motion>', move)

    #quand on click sur le vaisseau quelque chose se passe
    aireDeJeu.bind('<Button-1>', shoot)
    
    # FIN DE PARTIE

    # boocler la fenetre tk
    root.mainloop()