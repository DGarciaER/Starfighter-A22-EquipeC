import tkinter as tk
from ControleurJeu import ControleurJeu, Collision
from ModeleJeu import AireDeJeu, Vaiseau, Ovni, Missile, Asteroide, Laser, Niveau
from VueJeu import VueJeu
from tkinter import *
import threading
import random
from threading import Timer


if __name__ == "__main__":

    # créer une fenetre tk avec un titre, un background et des dimensions
    couleurTheme = "#41157A"
    
     # Si je fait par exemple print(tailleADJ["height"]), le output va être 500.

    """methode qui assigne une position aleatoire dans l'aire de jeu"""
    def randomPosition():
        return random.randint(0, 500)

    #creation fenetre root
    root = tk.Tk()
    root.title("Star Fighter")
    root.config(background= couleurTheme)
    root.geometry("510x680")

    # créer un containter et le centrer dans la fenetre tk
    mainContainer = tk.Frame(root, background= couleurTheme)
    mainContainer.pack() # pour centrer et donner un padding
    
    # créer un titre de jeu et le mettre dans un grid en lui donnant du padding
    titre = tk.Label(mainContainer, text="StarFighter", fg='#FFFC33', background= couleurTheme)
    titre.configure(font=("MV Boli", 25, "bold"))
    titre.grid(column=1, row=0, padx=10, pady=10)
                    
    # créer l'aire de jeu et le mettre dans un grid en lui donnant du padding
    aireDeJeu = AireDeJeu(mainContainer)
    vaisseau = Vaiseau(aireDeJeu)

    #--------------------------------------------------------------------------------------

    
    
    #----------------------------------------------------------------------------------------

    
    
    # créer un container pour afficher les statistiques en meme temps du jeu
    statsContainer = tk.Canvas(mainContainer, height=20, width=450,background= couleurTheme, highlightthickness=0)
    statsContainer.grid(column=1, row=3, padx=10, pady=5) # pour centrer et donner un padding

    # créer un container pour afficher le score
    score = tk.Label(statsContainer, text="   Score:  0  ", fg='#FFFD85',background= couleurTheme)
    score.grid(column=1, row=1, padx=10) # pour centrer et donner un padding

    # créer un container pour afficher la barre de vie
    lives = tk.Label(statsContainer, text="   Vies:  0  ", fg='#FFFD85',background= couleurTheme)
    lives.grid(column=2, row=1, padx=10) # pour centrer et donner un padding

    # créer un container pour afficher les abilités
    ability = tk.Label(statsContainer, text="   Abilités:  None  ", fg='#FFFD85',background= couleurTheme)
    ability.grid(column=3, row=1, padx=10) # pour centrer et donner un padding

    # créer un container des buttonset le mettre dans un grid en lui donnant du padding
    buttonsContainer = tk.Canvas(mainContainer, background= couleurTheme, highlightthickness=0)
    buttonsContainer.grid(column=1, row=4, padx=10, pady=20) # pour centrer et donner un padding
    couleurButtons = "#E22866"

    

    def niveau_facile():
     global timerMoveMissile 
     global timerMoveAsteroide 
     global timerCreateAsteroide 
     global timerCreateOvnis 
     global timerMoveOvnis 
     global vitesseOvni
     timerMoveMissile = 0
     timerMoveAsteroide = 0
     timerCreateAsteroide = 0
     timerCreateOvnis = 0
     timerMoveOvnis = 0
     vitesseOvni = 0
        
     if level.niveau == "facile":
            timerMoveMissile = 0.03
            timerMoveAsteroide = 0.03
            timerCreateAsteroide = 5
            timerCreateOvnis = 5
            timerMoveOvnis = 0.03
            vitesseOvni = 2
        
     elif level.niveau == "moyen":
            timerMoveMissile = 0.03
            timerMoveAsteroide = 0.03
            timerCreateAsteroide = 3
            timerCreateOvnis = 3
            timerMoveOvnis = 0.03
            vitesseOvni = 5

     elif level.niveau == "difficile":
            timerMoveMissile = 0.03
            timerMoveAsteroide = 0.03
            timerCreateAsteroide = 1
            timerCreateOvnis = 0.5
            timerMoveOvnis = 0.03
            vitesseOvni = 10
        


            # Le vaisseau se deplace en suivant la position de la souris
     aireDeJeu.canva.bind('<Motion>', moveVaisseau)

            # Un missile est tiré lorsqu'on fait un click gauche de la souris
     aireDeJeu.canva.bind('<Button-1>', shootMissile)

        # Deux lasers sont tirés lorsqu'on fait un double-click gauche de la souris
     aireDeJeu.canva.bind('<Button-3>', shootLaser)
        
     wait = Timer(timerMoveMissile,moveMissile)
     wait.start()
     waitA = Timer(timerCreateAsteroide, createAsteroide)
     waitA.start()
     waitA = Timer(timerMoveAsteroide, moveAsteroide)
     waitA.start()
        
        #creation ovnis
     waitB = Timer(timerCreateOvnis, createOvnis)
     waitB.start()
     waitB = Timer(timerMoveOvnis, moveOvnis)
     waitB.start()
       
            
        

#------------------------------------------------------------------------------------------------------------------------------
   
    level =  Niveau()
    def afficherChoixLevel():
        #creation de la fenetre
        fenetreLevel = tk.Tk()
        fenetreLevel.title("Choix du niveau")
        fenetreLevel.geometry("400x400")
        buttonsContainerAlignement = tk.Canvas(fenetreLevel, highlightthickness=0)
        buttonsContainerAlignement.pack() # pour centrer et donner un padding
        buttonEasyLevel = Button(buttonsContainerAlignement, text="Facile", command=level.level_facile)
        buttonMediumLevel = Button(buttonsContainerAlignement, text="Moyen", command=level.level_moyen)
        buttonHardLevel = Button(buttonsContainerAlignement, text="Difficile", command=level.level_difficile)
        buttonCommencer = Button(buttonsContainerAlignement, text="Commencer", command=niveau_facile)
        buttonCommencer.grid(column=4, row=1,padx=15)
        buttonEasyLevel.grid(column=1, row=1,padx=15)
        buttonMediumLevel.grid(column=2, row=1, padx=15)
        buttonHardLevel.grid(column=3, row=1, padx=15)
       
   
        
        



    #---------------------------------------------------------------------------------------------------------------------------------------------------------------
    # définir l'objet controleur
    jeu = ControleurJeu(aireDeJeu.canva)

    # créer un button qui commence une nouvelle session et le mettre dans un grid en lui donnant du padding
    buttonNouvSession = tk.Button(buttonsContainer, text="         Nouvelle session         ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'),command=afficherChoixLevel)
    buttonNouvSession.grid(column=1, row=1, padx=15)

    # créer un button qui affiche le menu score un nouveau jeu et le mettre dans un grid en lui donnant du padding
    buttonMenuScores = tk.Button(buttonsContainer, text="         Scores         ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'))
    buttonMenuScores.grid(column=2, row=1, padx=15)

    # créer un button quitte du programme et le mettre dans un grid en lui donnant du padding
    buttonQuitter = tk.Button(buttonsContainer, text="         Quitter         ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'))
    buttonQuitter.grid(column=3, row=1, padx=15)

    




    # Creation des listes qui serviront à contenir les différents éléments du jeu
    listMissile = []
    listAsteroide = []
    listLaser = []
    listeOvnis = []
    collision = Collision()

    # FIXME variable qui facilite la manipulation du vaisseau?
    imageV = vaisseau.imageVaisseau
   
    """Methode qui permet le mouvement du vaisseau lorsque la souris se deplace"""
    def moveVaisseau(e):

        # On ajoute cette ligne pour ne pas dupliquer des vaisseaux en utilisant toujours le même vaisseau
        global imageV

        #Récupérer l'image de Vaisseau et reduire sa taille avec la méthode subsample
        # Créer une instance de Vaisseau et l'afficher dans l'aire de jeu en lui donnant une position x, y
        imageV = tk.PhotoImage(file='Images/Vaisseau.png').subsample(12,12)
        
        # FIXME non utilise...
        instanceV = aireDeJeu.canva.create_image(e.x,e.y, image=imageV)

        vaisseau.setPositions(e.x,e.y)
        

        collision.vaseau_ennemie(vaisseau,listeOvnis)
        

    """Methode qui permet le mouvement des missiles"""
    def moveMissile():
        for missile in listMissile:
            aireDeJeu.canva.movex(missile.instanceMissile, 0, -10)
            missile.y -=10

            if missile.y <= 0:
                aireDeJeu.canva.delete(missile.instanceMissile)
                listMissile.remove(missile)
                # print('deleted')

        wait = Timer(0.03,moveMissile)
        wait.start()

    """Methode qui creer un missile et l'ajoute a la listMissile"""
    def shootMissile(event):
        listMissile.append(Missile(aireDeJeu, event.x, event.y))

    x = 0 
    imageA = vaisseau.imageVaisseau 

    """Methode qui creer un asteroide et l'ajoute a la listAsteroide"""
    def createAsteroide():
        
        if random.randint(0,1) == 0:
            # on fait partir l'asteroide a gauche
            x = random.randint(25,200)
            # print(x)
            listAsteroide.append(Asteroide(aireDeJeu,x,-40,"bas-droit"))

        else:
            #on fait partir l'asteroide à droite
            x = random.randint(250,425)
            listAsteroide.append(Asteroide(aireDeJeu,x,-40,"bas-gauche"))


        waitA = Timer(8, createAsteroide)
        waitA.start()

    """Methode qui permet le mouvement des asteroides"""
    def moveAsteroide():
        
        for aste in listAsteroide: # forEach qui passe dans toute la list listAsteroide
            # print(aste.direction)

            if aste.direction == "bas-droit":
                aireDeJeu.canva.move(aste.instanceAsteroide,5 ,5)
                aste.y += 5
                aste.x += 5

            elif aste.direction == "bas-gauche":
                aireDeJeu.canva.move(aste.instanceAsteroide,-5 ,5)
                aste.y += 5
                aste.x -= 5


            if aste.y >= 500:
                aireDeJeu.canva.delete(aste.instanceAsteroide)
                listAsteroide.remove(aste)

                # print('deleted')
            

        newWait = Timer(0.03, moveAsteroide)
        newWait.start()

    

    '''methode pour creer des ovnis avec une postion x aleatoire'''
    def createOvnis():
        if random.randint(0,1) == 0:
            # on fait partir l'ovnis a gauche
            x = random.randint(25,200)
            listeOvnis.append(Ovni(aireDeJeu,x,-40))

        else:
            #on fait partir l'ovnis à droite
            x = random.randint(250,425)
            listeOvnis.append(Ovni(aireDeJeu,x,-40))

        print(timerMoveOvnis)

        waitB = Timer(timerCreateOvnis, createOvnis)#cree un ovnis a chaque 3s
        waitB.start()

    """Methode qui permet le mouvement des ovnis"""
    def moveOvnis():
        
        for ovn in listeOvnis: # forEach qui passe dans toute la list listAsteroide
            # print(aste.direction)
                aireDeJeu.canva.move(ovn.instanceOvni,0 ,vitesseOvni)#deplacement de l'ovnis en x = 0, y = 2
                ovn.y += vitesseOvni
                
                if ovn.y >= 500:
                    aireDeJeu.canva.delete(ovn.instanceOvni)
                    listeOvnis.remove(ovn)
        
        newWait = Timer(timerMoveOvnis, moveOvnis)
        newWait.start()

   
        
    """Methode qui creer les lasers et les ajoute a la listLaser"""
    def shootLaser(event):
        if vaisseau.laserCooldown == False:
            vaisseau.laserCooldown = True
            listLaser.append(Laser(aireDeJeu, (event.x - imageV.width()/4 - 4), 0, (event.x - imageV.width()/4 - 2), event.y))
            listLaser.append(Laser(aireDeJeu, (event.x + imageV.width()/4 + 3), 0, (event.x + imageV.width()/4 + 5), event.y))
            aireDeJeu.canva.after(1000, deleteLaser)
            aireDeJeu.canva.after(5000, resetCooldown)
   
    def resetCooldown():
        vaisseau.laserCooldown = False
        print( "in resetCooldown")

    """Methode qui supprime les lasers"""
    def deleteLaser():
        aireDeJeu.canva.delete(listLaser[1].rectangleLaser)
        del listLaser[1]
        aireDeJeu.canva.delete(listLaser[0].rectangleLaser)   
        del listLaser[0]
        print('laser deleted')



   #Lancement du jeu a partir d'ici--------------------------------------------------

    afficherChoixLevel()
   
   
    # waitNiveau = Timer(1,niveau_facile)
    # waitNiveau.start()
        
 # FIN DE PARTIE

# boocler la fenetre tk
root.mainloop()