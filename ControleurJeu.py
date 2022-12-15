import random
from threading import Timer
import time
from ControleurMenu import ControleurMenu
from ModeleJeu import Asteroide, Laser, Ovni, Missile, Mine, PowerUp, Explosion
from VueJeu import VueJeu
from tkinter import *
import tkinter as tk
from functools import partial


class Mouvement(tk.Frame):
    '''
    Classe mouvement, qui s'occupe de tout ce qui a un rapport avec un mouvement des objets du jeu (vaisseau, missile, ovnis, asteroides, etc)
    Prend comme parametre un objet tkinter
    '''

    def __init__(self):
        pass


    
    def moveVaisseau(self, vaisseau, aireDeJeu,e):
        """Methode qui permet le mouvement du vaisseau lorsque la souris se deplace"""

        # Récupérer l'image de Vaisseau et reduire sa taille avec la méthode subsample
        self.imageV = tk.PhotoImage(file='Images/Vaisseau.png').subsample(12,12)
        # Créer une instance de Vaisseau et l'afficher dans l'aire de jeu en lui donnant une position x, y
        aireDeJeu.canva.create_image(e.x,e.y, image=self.imageV)
        # Setter la position de vaiseau dans l'objet vaiseau
        vaisseau.setPositions(e.x,e.y)

    
    def mouvMissiles(self, aireDeJeu, listeMissiles, timerMoveMissile):
        """Methode qui permet le mouvement des missiles"""

        #Boucle for each qui va passer dans la liste des missiles qui existent deja
        for missile in listeMissiles:
            aireDeJeu.canva.move(missile.instanceMissile, 0, -10)
            missile.y -=10

            #Si le missile depasse la partie en haut de l'aire de jeu (y <= 0), supprimer le missile, pour eviter de se retrouver avec plein de missiles.
            if missile.y <= 0:
                aireDeJeu.canva.delete(missile.instanceMissile)
                listeMissiles.remove(missile)
        
        #Timer threads
        mouvMissileTimer = Timer(timerMoveMissile,partial(self.mouvMissiles,aireDeJeu, listeMissiles, timerMoveMissile))
        mouvMissileTimer.start()

    
    def moveOvnis(self, timerMoveOvnis, vitesseOvniY,vitesseOvniX, listeOvnis, aireDeJeu):
        """Methode qui permet le mouvement des ovnis"""
        
        vitesseHorizontalDroite = vitesseOvniX
        vitesseHorizontalGauche = -vitesseOvniX

        for ovn in listeOvnis: # forEach qui passe dans toute la list listAsteroide
                
                ovn.y += vitesseOvniY
                if(ovn.x >= 400):               # Si x >= 400, ca veut dire que l'ovni est a gauche de l'aire de jeu.
                    ovn.direction = "left"      # On s'en sert en bas pour definir si il faut bouger l'ovni a gauche ou a droite

                elif(ovn.x <= 5):               # Si x >= 400, ca veut dire que l'ovni est a gauche de l'aire de jeu.
                    ovn.direction = "right"     # On s'en sert en bas pour definir si il faut bouger l'ovni a gauche ou a droite

                if(ovn.direction == "right"):
                    aireDeJeu.canva.move(ovn.instanceOvni,vitesseHorizontalDroite ,vitesseOvniY)#deplacement de l'ovnis en x = 0, y = 2
                    ovn.x += vitesseHorizontalDroite
                else:
                    aireDeJeu.canva.move(ovn.instanceOvni,vitesseHorizontalGauche ,vitesseOvniY)#deplacement de l'ovnis en x = 0, y = 2
                    ovn.x += vitesseHorizontalGauche

                
                # Si y >= 500, veut dire que l'ovni est en dehors de l'aire de jeu, donc on supprime
                if ovn.y >= 600:
                    aireDeJeu.canva.delete(ovn.instanceOvni)
                    listeOvnis.remove(ovn)
        
        mouvOvniTimer = Timer(timerMoveOvnis, partial(self.moveOvnis, timerMoveOvnis, vitesseOvniY,vitesseOvniX, listeOvnis, aireDeJeu))
        mouvOvniTimer.start()

    
    def moveAsteroide(self,timerMoveAsteroide, listAsteroide, aireDeJeu):
        """Methode qui permet le mouvement des asteroides"""
        
        for aste in listAsteroide: # forEach qui passe dans toute la list listAsteroide

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
            
        mouvAsteroideTimer = Timer(timerMoveAsteroide, partial(self.moveAsteroide, timerMoveAsteroide, listAsteroide, aireDeJeu))
        mouvAsteroideTimer.start()

    def mouvMines(self,listeMine, aireDeJeu):
        vitesseMine = 3
        for mine in listeMine:
            aireDeJeu.canva.move(mine.instanceMine,0 ,vitesseMine)#deplacement de l'ovnis en x = 0, y = 2
            mine.y += vitesseMine
            
            if mine.y >= 600:
                aireDeJeu.canva.delete(mine.instanceMine)
                listeMine.remove(mine)

        mouvMineTimer = Timer(0.03, partial(self.mouvMines, listeMine, aireDeJeu))
        mouvMineTimer.start()

    
    def movePowerUp(self, timerMovePU, vitessePU, listePU, aireDeJeu):
        """Methode qui permet le mouvement des powerup"""

        for pu in listePU: # forEach qui passe dans toute la list listAsteroide
                
            pu.y += vitessePU

            aireDeJeu.canva.move(pu.instancePU, 0,vitessePU)
                
            if pu.y >= 600:
                aireDeJeu.canva.delete(pu.instancePU)
                listePU.remove(pu)
        
        mouvPUTimer = Timer(timerMovePU, partial(self.movePowerUp, timerMovePU, vitessePU, listePU, aireDeJeu))
        mouvPUTimer.start()




class Shoot(tk.Frame):
    '''
    Cette classe s'occupe de tout ce qui a un rapport avec l'action de tirer 
    (Le vaisseau tire un missile/laser(ET cooldown laser), les ovnis tirent une mine, etc)
    '''

    def __init__(self):
        pass

        self.listeMissiles = []
        self.listLaser = []
        self.listMine = []
        self.imageV = tk.PhotoImage(file='Images/Vaisseau.png').subsample(12,12)

    """Methode qui creer un missile et l'ajoute a la listeMissiles"""
    def shootMissile(self, aireDeJeu, vaisseau, event):
        print(vaisseau.missileCooldown)
        if vaisseau.missileCooldown == False:
            vaisseau.missileCooldown = True
            self.listeMissiles.append(Missile(aireDeJeu, event.x, event.y))
            aireDeJeu.canva.after(350, partial(self.resetMissileCooldown, vaisseau))

    def resetMissileCooldown(self, vaisseau):
        vaisseau.missileCooldown = False

    """Methode qui creer les lasers et les ajoute a la listLaser"""
    def shootLaser(self, aireDeJeu, vaisseau, event):
        if vaisseau.laserCooldown == False:
            vaisseau.laserCooldown = True
            self.listLaser.append(Laser(aireDeJeu, (event.x - self.imageV.width()/4 - 4), 0, (event.x - self.imageV.width()/4 - 2), event.y))
            self.listLaser.append(Laser(aireDeJeu, (event.x + self.imageV.width()/4 + 3), 0, (event.x + self.imageV.width()/4 + 5), event.y))
            aireDeJeu.canva.after(1000, partial(self.deleteLaser, aireDeJeu))
            aireDeJeu.canva.after(5000, partial(self.resetLaserCooldown, vaisseau))

    def shootMine(self,timerShootMine, listeOvnis, aireDeJeu):
        for ovni in listeOvnis:
            self.listMine.append(Mine(aireDeJeu, ovni.x + 26, ovni.y + 20))

        shootMineTimer = Timer(timerShootMine, partial(self.shootMine, timerShootMine, listeOvnis, aireDeJeu))
        shootMineTimer.start()

    def resetLaserCooldown(self, vaisseau):
        vaisseau.laserCooldown = False

    """Methode qui supprime les lasers"""
    def deleteLaser(self, aireDeJeu):
        aireDeJeu.canva.delete(self.listLaser[1].rectangleLaser)
        del self.listLaser[1]
        aireDeJeu.canva.delete(self.listLaser[0].rectangleLaser)   
        del self.listLaser[0]
        print('laser deleted')



class PlayerControl:    # FIXME erreur de parametre quand on appelle perte_hp
    '''
    Cette classe s'occupe de controler les informations sur
    Un utilisateur: augmenter son score, ses points de vie, etc.
    '''
    def __init__(self, player):
        self.player = player

    def augmentation_score(self):
        self.player.score += 1
    
    def augmentation_hp(self):
        if self.player.hp < 10:
            self.player.hp += 1

    def perte_hp(self):
        if self.player.hp > 0:
            self.player.hp -= 1

    def updatePlayer(self, scoreLabel, hpLabel):
        scoreLabel.config(text="Score:  "+ str(self.player.score))
        hpLabel.config(text="Vies:  " + str(self.player.hp))

        updatePlayerTimer = Timer(0.1, partial(self.updatePlayer, scoreLabel, hpLabel))
        updatePlayerTimer.start()


class Spawns(tk.Frame):

    '''
    Cette classe s'occupe de la generation des objets dans l'aire de jeu (Generation des ovnis, des asteroides ainsi que des bonus (Power Up))
    '''

    def __init__(self):
        self.listeOvnis = []
        self.listAsteroides = []
        self.listPU = []

    '''methode pour creer des ovnis avec une postion x aleatoire'''
    def createOvnis(self, timerCreateOvnis, aireDeJeu):

        if random.randint(0,1) == 0:
            # on fait partir l'ovnis a gauche
            x = random.randint(25,200)
            self.listeOvnis.append(Ovni(aireDeJeu,x,-40))
        else:
            #on fait partir l'ovnis à droite
            x = random.randint(250,425)
            self.listeOvnis.append(Ovni(aireDeJeu,x,-40))

        createOvniTimer = Timer(timerCreateOvnis, partial(self.createOvnis, timerCreateOvnis, aireDeJeu))#cree un ovnis a chaque 3s
        createOvniTimer.start()

    """Methode qui creer un asteroide et l'ajoute a la listAsteroide"""
    def createAsteroide(self,timerCreateAsteroide, aireDeJeu):
        
        if random.randint(0,1) == 0:
            # on fait partir l'asteroide a gauche
            x = random.randint(25,200)
            self.listAsteroides.append(Asteroide(aireDeJeu,x,-40,"bas-droit"))

        else:
            #on fait partir l'asteroide à droite
            x = random.randint(250,425)
            self.listAsteroides.append(Asteroide(aireDeJeu,x,-40,"bas-gauche"))


        createAstroideTimer = Timer(timerCreateAsteroide, partial(self.createAsteroide, timerCreateAsteroide, aireDeJeu))
        createAstroideTimer.start()

    '''methode pour creer des powerup avec une postion x aleatoire'''
    def createPU(self, timerCreatePU, aireDeJeu):

        if random.randint(0,1) == 0:
            # on fait partir le powerup a gauche
            x = random.randint(25,200)
            self.listPU.append(PowerUp(aireDeJeu,x,-40))
        else:
            #on fait partir le powerup à droite
            x = random.randint(250,425)
            self.listPU.append(PowerUp(aireDeJeu,x,-40))

        createPUTimer = Timer(timerCreatePU, partial(self.createPU, timerCreatePU, aireDeJeu))  #cree un powerup a chaque n secondes
        createPUTimer.start()

class Collision:

    '''
    Cette classe s'occupe des collisions entre les objets
    '''
    def __init__(self):
        self.listExplosion = []
    

    def vaisseau_ennemie(self, vaisseau, listeOvnis, playerControl, aireDeJeu): # Collision entre un vaisseau et un ovni
         
        equivalance = 31 # taille du cadre de l'image
         
        VY = vaisseau.y      #position Y milieu du carré rouge 
        VX = vaisseau.x      #position X milieu du carré rouge 
        VL = vaisseau.x - vaisseau.imageVaisseau.width()/2 + equivalance      #position gauche du carré rouge 
        VR = vaisseau.x + vaisseau.imageVaisseau.width()/2 - equivalance      #position droite du carré rouge
        VT = vaisseau.y - vaisseau.imageVaisseau.height()/2 + equivalance     #position haut du carré rouge
        VB = vaisseau.y + vaisseau.imageVaisseau.height()/2 - equivalance     #position bas du carré rouge


        for ovni in listeOvnis:
            
            OL = ovni.x                           #position gauche du pion
            OR = ovni.x + ovni.imageOvni.width()  #position droite du pion
            OT = ovni.y                           #position haut du pion
            OB = ovni.y + ovni.imageOvni.height() #position bas du pion

            # la logique des collisions avec RB
            if VT <= OB and VT >= OT or VY <= OB and VY >= OT or VB >= OT and VB <= OB:
                if VR >= OL and VR <= OR or VL <= OR and VL >= OL or VX <= OR and VX >= OL:
                    playerControl.perte_hp()
                    self.startExplosion(aireDeJeu, ovni.x, ovni.y)
                    listeOvnis.remove(ovni)
                    
    
    def missiles_ovnis(self, listeMissiles, listeOvnis, playerControl, aireDeJeu): # Collision entre un missile et un ovni
        
        equivalance = 0 # taille du cadre de l'image
        
        for missile in listeMissiles:

            MY = missile.y      #position Y milieu du carré rouge 
            MX = missile.x      #position X milieu du carré rouge 
            ML = missile.x - missile.imageMissile.width()/2 + equivalance      #position gauche du carré rouge 
            MR = missile.x + missile.imageMissile.width()/2 - equivalance      #position droite du carré rouge
            MT = missile.y - missile.imageMissile.height()/2 + equivalance     #position haut du carré rouge
            MB = missile.y + missile.imageMissile.height()/2 - equivalance     #position bas du carré rouge

            for ovni in listeOvnis:
            
                OL = ovni.x                           #position gauche du pion
                OR = ovni.x + ovni.imageOvni.width()  #position droite du pion
                OT = ovni.y                           #position haut du pion
                OB = ovni.y + ovni.imageOvni.height() #position bas du pion

                # la logique des collisions avec RB
                if MT <= OB and MT >= OT or MY <= OB and MY >= OT or MB >= OT and MB <= OB:
                    if MR >= OL and MR <= OR or ML <= OR and ML >= OL or MX <= OR and MX >= OL:
                        playerControl.augmentation_score()
                        # ovni.imageOvni = tk.PhotoImage(file='Images/explosion.png').subsample(4,4)
                        # ovni.instanceOvni = container.canva.create_image(self.x,self.y,anchor=tk.NW,image=self.imageOvni)
                        # time.sleep(2)
                        self.startExplosion(aireDeJeu, ovni.x, ovni.y)
                        listeOvnis.remove(ovni)
                        listeMissiles.remove(missile)
                        print("Collision missile-ovni")
                        # faire apparaitre explosion


                        
    def vaisseau_asteroids(self, vaisseau, listeAsteroids, difficulte, player, aireDeJeu): #Collision entre le vaisseau de l'utilisateur et un asteroide

        equivalanceV = 31

        VY = vaisseau.y      #position Y milieu du carré rouge 
        VX = vaisseau.x      #position X milieu du carré rouge 
        VL = vaisseau.x - vaisseau.imageVaisseau.width()/2 + equivalanceV      #position gauche du carré rouge 
        VR = vaisseau.x + vaisseau.imageVaisseau.width()/2 - equivalanceV      #position droite du carré rouge
        VT = vaisseau.y - vaisseau.imageVaisseau.height()/2 + equivalanceV + 10   #position haut du carré rouge
        VB = vaisseau.y + vaisseau.imageVaisseau.height()/2 - equivalanceV     #position bas du carré rouge

        for asteroid in listeAsteroids:

            if asteroid.direction == "bas-droit":
                equivalance = 20 # taille du cadre de l'image 
                AL = asteroid.x + equivalance                     #position gauche du pion
                AR = asteroid.x + asteroid.imageAsteroide.width()  #position droite du pion
                AT = asteroid.y + equivalance                         #position haut du pion
                AB = asteroid.y + asteroid.imageAsteroide.height()#position bas du pion
            else:
                AL = asteroid.x                     #position gauche du pion
                AR = asteroid.x + asteroid.imageAsteroide.width() - 20#position droite du pion
                AT = asteroid.y + 30                         #position haut du pion
                AB = asteroid.y + asteroid.imageAsteroide.height()#position bas du pion

            # la logique des collisions avec RB
            if VT <= AB and VT >= AT or VY <= AB and VY >= AT or VB >= AT and VB <= AB:
                if VR >= AL and VR <= AR or VL <= AR and VL >= AL or VX <= AR and VX >= AL:
                    print("asteroid")
                    if difficulte == "facile":
                        if player.hp <= 1:
                            player.hp = 0
                        else:
                            player.hp = 1
                    else:
                        player.hp = 0   # se fait aussi avec un setter (meilleure pratique)
                    self.startExplosion(aireDeJeu, asteroid.x, asteroid.y)
                    listeAsteroids.remove(asteroid)
                    # faire apparaitre explosion

    def vaisseau_PowerUp(self, vaisseau, listPU, playerControl): # Detecte collision entre le vaisseau et un bonus
        
        equivalance = 31 # taille du cadre de l'image
         
        VY = vaisseau.y      #position Y milieu du carré rouge 
        VX = vaisseau.x      #position X milieu du carré rouge 
        VL = vaisseau.x - vaisseau.imageVaisseau.width()/2 + equivalance      #position gauche du carré rouge 
        VR = vaisseau.x + vaisseau.imageVaisseau.width()/2 - equivalance      #position droite du carré rouge
        VT = vaisseau.y - vaisseau.imageVaisseau.height()/2 + equivalance     #position haut du carré rouge
        VB = vaisseau.y + vaisseau.imageVaisseau.height()/2 - equivalance     #position bas du carré rouge


        for pu in listPU:
            
            PL = pu.x                           #position gauche du pion
            PR = pu.x + pu.imagePU.width()  #position droite du pion
            PT = pu.y                           #position haut du pion
            PB = pu.y + pu.imagePU.height() #position bas du pion

            # la logique des collisions avec RB
            if VT <= PB and VT >= PT or VY <= PB and VY >= PT or VB >= PT and VB <= PB:
                if VR >= PL and VR <= PR or VL <= PR and VL >= PL or VX <= PR and VX >= PL:
                    if pu.type == "Score":
                        playerControl.augmentation_score()
                    else:
                        playerControl.augmentation_hp()
                    listPU.remove(pu)

    def vaisseau_mine(self, vaisseau, listeMine, player, aireDeJeu): # Detecte une collision entre un vaisseau et une mine
         
        equivalanceXR = 0 # taille du cadre de l'image
        equivalanceXL = 40 # taille du cadre de l'image
        equivalancey = 60 # taille du cadre de l'image
         
        VY = vaisseau.y      #position Y milieu du carré rouge 
        VX = vaisseau.x      #position X milieu du carré rouge 
        VL = vaisseau.x - vaisseau.imageVaisseau.width()/2 + equivalanceXL      #position gauche du carré rouge 
        VR = vaisseau.x + vaisseau.imageVaisseau.width()/2 - equivalanceXR      #position droite du carré rouge
        VT = vaisseau.y - vaisseau.imageVaisseau.height()/2 + equivalancey     #position haut du carré rouge
        VB = vaisseau.y + vaisseau.imageVaisseau.height()/2 - 20    #position bas du carré rouge


        for mine in listeMine:
            
            ML = mine.x - 5                         #position gauche du pion
            MR = mine.x + mine.imageMine.width()    #position droite du pion
            MT = mine.y                             #position haut du pion
            MB = mine.y + mine.imageMine.height()   #position bas du pion

            # la logique des collisions avec RB
            if VT <= MB and VT >= MT or VY <= MB and VY >= MT or VB >= MT and VB <= MB:
                if VR - 2 >= ML and VR - 2 <= MR or VL - 4 <= MR and VL - 4 >= ML or VX <= MR and VX >= ML:
                    if player.hp <= 3:
                        player.hp = 0
                    else:
                        player.hp -= 3
                    self.startExplosion(aireDeJeu, mine.x, mine.y)
                    listeMine.remove(mine)
                    

    def laser_ovnis(self, vaisseau, listLaser, listeOvnis, playerControl, aireDeJeu): # Detecte une collision entre un laser et un ovni
        
        for laser in listLaser:
            for ovni in listeOvnis:
                if laser.x >= ovni.x and laser.x <= ovni.x + ovni.imageOvni.width() and vaisseau.y >= ovni.y:
                    print("x du laser")
                    print(laser.x)
                    print("x du ovni")
                    print(ovni.x)
                    print("voila, le laser est op")
                    playerControl.augmentation_score()
                    self.startExplosion(aireDeJeu, ovni.x, ovni.y)
                    listeOvnis.remove(ovni)

    def startExplosion(self, aireDeJeu, x, y):
        equivalenceX = 34
        equivalenceY = 17
        self.listExplosion.append(Explosion(aireDeJeu,x - equivalenceX, y - equivalenceY))
        print(len(self.listExplosion))
        aireDeJeu.canva.after(500, partial(self.deleteExplosion, aireDeJeu))

    def deleteExplosion(self, aireDeJeu):
        aireDeJeu.canva.delete(self.listExplosion[0].imageExplosion)
        del self.listExplosion[0]

    def verfierToutesCollisions(self, vaisseau, listeOvnis, listeMissiles, listeAsteroides, listeMine, listLaser , listPU, difficulte, player, playerControl, aireDeJeu):
        self.vaisseau_ennemie(vaisseau,listeOvnis, playerControl, aireDeJeu)
        self.missiles_ovnis(listeMissiles,listeOvnis, playerControl, aireDeJeu)
        self.vaisseau_asteroids(vaisseau,listeAsteroides, difficulte, player, aireDeJeu)
        self.vaisseau_PowerUp(vaisseau, listPU, playerControl)
        self.vaisseau_mine(vaisseau, listeMine, player, aireDeJeu)
        self.laser_ovnis(vaisseau, listLaser, listeOvnis, playerControl, aireDeJeu)
        verifierCollisionsTimer = Timer(0.03,partial(self.verfierToutesCollisions, vaisseau, listeOvnis, listeMissiles, listeAsteroides, listeMine, listLaser, listPU, difficulte, player, playerControl, aireDeJeu))
        verifierCollisionsTimer.start()       
                        
                        
                        
class ControleurJeu(tk.Frame):
    '''
    Cette classe s'occupe du chronometre dans le jeu
    '''

    def __init__(self):

        self.update_time = ''
        self.running = False #Pour controller l'etat du timer (en marche ou non)
        
        #On initialise les variables de temps a 0
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0

        #On initialise les variables string a des chaines vides. Pour l'affichage et sauvegarder les scores (temps)
        self.minutes_string = ""
        self.seconds_string = ""
        self.milliseconds_string = ""

        #variables score/csv
        self.listScore = []
        self.username = ''

        self.gameOver = False

        #PARTIE POUR TIMER **-----------------------------------------------------------------------------------**    
    
    
    def create_widget(self, container):
        '''Fonction pour créer le label du timer'''
        self.stopwatch_label = tk.Label(container, text='Timer:  00:00:00', fg='#FFFD85',background= "#41157A")
        self.stopwatch_label.grid(column=3, row=1, padx=10)

    def startTimer(self):
        '''Fonction pour commencer le timer. Appeler lorsqu'on click sur le carre rouge'''
        if not self.running:                                        # Si le timer n'est en marche,
                self.running = True                                 # Alors on met la variable a True
                self.updateTimer()                                  # Et on commence le timer

    def pauseTimer(self):
        '''Fonction pour arreter le timer, on l'appel quand l'utilisateur perds'''
        if self.running:                                            # Si le timer est en marche,
            self.stopwatch_label.after_cancel(self.update_time)     # Stop le update du timer
            self.running = False                                    # On remet la variable à False
           
    def resetTimer(self):
        '''Cette fonction s'occupe de reinitialiser le timer, on l'appel lorsqu'on recommence une nouvelle partie'''
        if self.running:                                            # Si le timer est en marche,
            self.stopwatch_label.after_cancel(self.update_time)     # Alors on arrete le timer
            self.running = False                                    # On remet la variable à False
        #On remet les variables et le label du timer a zero
        self.minutes, self.seconds, self.milliseconds = 0, 0, 0
        self.stopwatch_label.config(text='00:00:00')

    def updateTimer(self):
        '''Cette fonction s'occupe de mettre a jour les valeurs (millisecondes, secondes et minutes) et les valeurs_string(Pour affichage et sauvegarder les scores)'''

        #Conditions pour update les valeurs
        if self.running:                                            # SI le timer est en marche,
            self.milliseconds += 1                                  # +1 milliseconde
            if self.milliseconds == 100:                            # SI les millisecondes arrives a 1000,
                self.seconds += 1                                   # Alors les secondes augmenteront de 1
                self.milliseconds = 0                               # Et on remet les millisecondes a 0
            if self.seconds == 60:                                  # SI les secondes arrivent à 60,
                self.minutes += 1                                   # Alors +1 minute
                self.seconds = 0                                    # Et on remet les secondes à 0
            #On transforme les ints en string
            self.minutes_string = f'{self.minutes}' if self.minutes > 9 else f'0{self.minutes}'
            self.seconds_string = f'{self.seconds}' if self.seconds > 9 else f'0{self.seconds}'
            self.milliseconds_string = f'{self.milliseconds}' if self.milliseconds > 9 else f'0{self.milliseconds}'
            self.stopwatch_label.config(text='Timer:  ' + self.minutes_string + ':' + self.seconds_string + ':' + self.milliseconds_string)
            self.update_time = self.stopwatch_label.after(10, self.updateTimer) #Variabe update_time, appelé dans pauseTimer() et resetTimer() avec .after_cancel

