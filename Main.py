import tkinter as tk
from functools import partial
from ControleurJeu import Collision, Mouvement, PlayerControl, Shoot, Spawns, ControleurJeu, Verification
from ControleurMenu import ControleurMenu, Choix, Enregistrer
from ModeleJeu import AireDeJeu, Player, Vaiseau
from ModeleMenu import Niveau
from threading import Timer


if __name__ == "__main__":

    # Affichage du menu et la récuperation des choix

    #Initialisation des objets du jeu
    jeu = ControleurJeu()
    enregistrer = Enregistrer()
    menu = ControleurMenu()
    level = Niveau()
    choix = Choix()
    choix.afficherChoixLevel(menu, level, jeu)

   

    def commencerJeu():
        print(menu.commence)
        if menu.commence:
            # créer une fenetre tk avec un titre, un background et des dimensions
            couleurTheme = "#41157A"
            
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
            
            # créer un container pour afficher les statistiques en meme temps du jeu
            statsContainer = tk.Canvas(mainContainer, height=20, width=450,background= couleurTheme, highlightthickness=0)
            statsContainer.grid(column=1, row=3, padx=10, pady=5) # pour centrer et donner un padding

            # créer un container pour afficher le score
            scoreLabel = tk.Label(statsContainer, text="   Score:  " , fg='#FFFD85',background= couleurTheme)
            scoreLabel.grid(column=1, row=1, padx=10) # pour centrer et donner un padding

            # créer un container pour afficher la barre de vie
            hpLabel = tk.Label(statsContainer, text="   Vies:  ", fg='#FFFD85',background= couleurTheme)
            hpLabel.grid(column=2, row=1, padx=10) # pour centrer et donner un padding

            # créer un container des buttonset le mettre dans un grid en lui donnant du padding
            buttonsContainer = tk.Canvas(mainContainer, background= couleurTheme, highlightthickness=0)
            buttonsContainer.grid(column=1, row=4, padx=10, pady=20) # pour centrer et donner un padding
            couleurButtons = "#E22866"

            # créer un player qui contient les scores et les vies
            player = Player()

            #---------------------------------------------------------------------------------------------------------------------------
            buttonEnregistrer = tk.Button(buttonsContainer, text="    Enregistrer    ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'), command=partial(enregistrer.askUsername, player,jeu))
            buttonEnregistrer.grid(column=1, row=1, padx=15)

            # créer un button qui affiche le menu score un nouveau jeu et le mettre dans un grid en lui donnant du padding
            buttonMenuScores = tk.Button(buttonsContainer, text="    Scores    ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'), command=partial(enregistrer.AfficherScores))
            buttonMenuScores.grid(column=2, row=1, padx=15)

            # créer un button quitte du programme et le mettre dans un grid en lui donnant du padding
            buttonQuitter = tk.Button(buttonsContainer, text="    Quitter    ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'), command=root.destroy)
            buttonQuitter.grid(column=3, row=1, padx=15)

            #-------------------------------------------------------------------------------------------------------------------------------
            
            # créer l'aire de jeu et le mettre dans un grid en lui donnant du padding
            aireDeJeu = AireDeJeu(mainContainer)
            
            jeu.create_widget(statsContainer) #HUD
            jeu.startTimer() #Timer, commence en mem


            # controler le player
            playerControl = PlayerControl(player)
            verif = Verification()
            vaisseau = Vaiseau(aireDeJeu)
            spawns = Spawns()
            mvmt = Mouvement()
            shoot = Shoot()
            collision = Collision()

            # Le vaisseau se deplace en suivant la position de la souris
            aireDeJeu.canva.bind('<Motion>', partial(mvmt.moveVaisseau, vaisseau, aireDeJeu, jeu))

            # # Un missile est tiré lorsqu'on fait un click gauche de la souris
            aireDeJeu.canva.bind('<Button-1>', partial(shoot.shootMissile, aireDeJeu, vaisseau))
            # On bouge le missile vers le haut
            mvmt.mouvMissiles(aireDeJeu, shoot.listeMissiles, menu.timerMoveMissile, jeu)

            # Deux lasers sont tirés lorsqu'on fait un click droit de la souris
            aireDeJeu.canva.bind('<Button-3>', partial(shoot.shootLaser, aireDeJeu, vaisseau))

            # creation ovnis
            spawns.createOvnis(menu.timerCreateOvnis, aireDeJeu, jeu)

            # creation astroides
            spawns.createAsteroide(menu.timerCreateAsteroide, aireDeJeu, jeu)

            # creation powerup
            spawns.createPU(menu.timerCreatePU, aireDeJeu, jeu)

            # mouvement des ovnis
            mvmt.moveOvnis(menu.timerMoveOvnis, menu.vitesseOvniY, menu.vitesseOvniX, spawns.listeOvnis, aireDeJeu, jeu)

            # mouvement des astroides
            mvmt.moveAsteroide(menu.timerMoveAsteroide, spawns.listAsteroides, aireDeJeu, jeu)

            # mouvement des powerup
            mvmt.movePowerUp(menu.timerMovePU, menu.vitessePU, spawns.listPU, aireDeJeu, jeu)

            # shoot mines des ovnis
            shoot.shootMine(menu.timerShootMine, spawns.listeOvnis, aireDeJeu, jeu)

            # mouvement de mines
            mvmt.mouvMines(shoot.listMine, aireDeJeu, jeu)
                
            # verifier les collision entre tout les objets du jeu
            collision.verfierToutesCollisions(vaisseau,spawns.listeOvnis, shoot.listeMissiles ,spawns.listAsteroides, shoot.listMine, shoot.listLaser ,spawns.listPU, level.niveau, player, playerControl, aireDeJeu)    #TODO ajouter collision avec powerup

            # faire raffraichir les stats du player tout a long du jeu
            playerControl.updatePlayer(scoreLabel, hpLabel)

            # FIN DE PARTIE

            # boocler la fenetre tk
            verif.verifHP(player, jeu, aireDeJeu)
            root.mainloop()

            
        else:
            commencerJeuTimer = Timer(0.03, commencerJeu)
            commencerJeuTimer.start()

    commencerJeu()