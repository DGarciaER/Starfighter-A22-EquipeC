import random
from threading import Timer
from ControleurMenu import ControleurMenu
from ModeleJeu import AireDeJeu, Asteroide, Laser, Ovni, Missile
from VueJeu import VueJeu
from tkinter import *
import tkinter as tk
from functools import partial


class Mouvement(tk.Frame):

    def __init__(self):
        self.imageV = tk.PhotoImage(file='Images/Vaisseau.png').subsample(12,12)


    """Methode qui permet le mouvement du vaisseau lorsque la souris se deplace"""
    def moveVaisseau(self, vaisseau, aireDeJeu,e):

        # Récupérer l'image de Vaisseau et reduire sa taille avec la méthode subsample
        self.imageV = tk.PhotoImage(file='Images/Vaisseau.png').subsample(12,12)
        # Créer une instance de Vaisseau et l'afficher dans l'aire de jeu en lui donnant une position x, y
        aireDeJeu.canva.create_image(e.x,e.y, image=self.imageV)
        # Setter la position de vaiseau dans l'objet vaiseau
        vaisseau.setPositions(e.x,e.y)

    """Methode qui permet le mouvement des missiles"""
    def mouvMissiles(self, aireDeJeu, listeMissiles, timerMoveMissile):

        for missile in listeMissiles:
            aireDeJeu.canva.move(missile.instanceMissile, 0, -10)
            missile.y -=10

            if missile.y <= 0:
                aireDeJeu.canva.delete(missile.instanceMissile)
                listeMissiles.remove(missile)

        mouvMissileTimer = Timer(timerMoveMissile,partial(self.mouvMissiles,aireDeJeu, listeMissiles, timerMoveMissile))
        mouvMissileTimer.start()

    """Methode qui permet le mouvement des ovnis"""
    def moveOvnis(self, timerMoveOvnis, vitesseOvni, listeOvnis, aireDeJeu):
        
        for ovn in listeOvnis: # forEach qui passe dans toute la list listAsteroide
            # print(aste.direction)
                aireDeJeu.canva.move(ovn.instanceOvni,0 ,vitesseOvni)#deplacement de l'ovnis en x = 0, y = 2
                ovn.y += vitesseOvni
                
                if ovn.y >= 500:
                    aireDeJeu.canva.delete(ovn.instanceOvni)
                    listeOvnis.remove(ovn)
        
        mouvOvniTimer = Timer(timerMoveOvnis, partial(self.moveOvnis, timerMoveOvnis, vitesseOvni, listeOvnis, aireDeJeu))
        mouvOvniTimer.start()

    """Methode qui permet le mouvement des asteroides"""
    def moveAsteroide(self,timerMoveAsteroide, listAsteroide, aireDeJeu):
        
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




class Shoot(tk.Frame):
    def __init__(self):
        pass

        self.listeMissiles = []
        self.listLaser = []
        self.imageV = tk.PhotoImage(file='Images/Vaisseau.png').subsample(12,12)

    """Methode qui creer un missile et l'ajoute a la listeMissiles"""
    def shootMissile(self, aireDeJeu, event):
        self.listeMissiles.append(Missile(aireDeJeu, event.x, event.y))

    """Methode qui creer les lasers et les ajoute a la listLaser"""
    def shootLaser(self, aireDeJeu, vaisseau, event):
        if vaisseau.laserCooldown == False:
            vaisseau.laserCooldown = True
            self.listLaser.append(Laser(aireDeJeu, (event.x - self.imageV.width()/4 - 4), 0, (event.x - self.imageV.width()/4 - 2), event.y))
            self.listLaser.append(Laser(aireDeJeu, (event.x + self.imageV.width()/4 + 3), 0, (event.x + self.imageV.width()/4 + 5), event.y))
            aireDeJeu.canva.after(1000, partial(self.deleteLaser, aireDeJeu))
            aireDeJeu.canva.after(5000, partial(self.resetCooldown, vaisseau))
    
    def resetCooldown(self, vaisseau):
        vaisseau.laserCooldown = False
        print( "in resetCooldown")

    """Methode qui supprime les lasers"""
    def deleteLaser(self, aireDeJeu):
        aireDeJeu.canva.delete(self.listLaser[1].rectangleLaser)
        del self.listLaser[1]
        aireDeJeu.canva.delete(self.listLaser[0].rectangleLaser)   
        del self.listLaser[0]
        print('laser deleted')



class PlayerControl:    # FIXME erreur de parametre quand on appelle perte_hp
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

    def __init__(self):
        self.listeOvnis = []
        self.listAsteroides = []

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


class Collision:

    def vaseau_ennemie(self, vaisseau, listeOvnis, playerControl):
         
        equivalance = 31
         
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
                    
    
    def missiles_ovnis(self, listeMissiles, listeOvnis, playerControl):
        
        equivalance = 0
        
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

                        
    def vaisseau_asteroids(self, vaisseau, listeAsteroids):
        equivalance = 0

        VY = vaisseau.y      #position Y milieu du carré rouge 
        VX = vaisseau.x      #position X milieu du carré rouge 
        VL = vaisseau.x - vaisseau.imageVaisseau.width()/2 + equivalance      #position gauche du carré rouge 
        VR = vaisseau.x + vaisseau.imageVaisseau.width()/2 - equivalance      #position droite du carré rouge
        VT = vaisseau.y - vaisseau.imageVaisseau.height()/2 + equivalance     #position haut du carré rouge
        VB = vaisseau.y + vaisseau.imageVaisseau.height()/2 - equivalance     #position bas du carré rouge

        for asteroid in listeAsteroids:

            AL = asteroid.x                           #position gauche du pion
            AR = asteroid.x + asteroid.imageAsteroide.width()  #position droite du pion
            AT = asteroid.y                           #position haut du pion
            AB = asteroid.y + asteroid.imageAsteroide.height() #position bas du pion

            # la logique des collisions avec RB
            if VT <= AB and VT >= AT or VY <= AB and VY >= AT or VB >= AT and VB <= AB:
                if VR >= AL and VR <= AR or VL <= AR and VL >= AL or VX <= AR and VX >= AL:
                    print("asteroid")    

    def verfierToutesCollisions(self, vaisseau, listeOvnis, listeMissiles, listeAsteroides, playerControl):
        self.vaseau_ennemie(vaisseau,listeOvnis, playerControl)
        self.missiles_ovnis(listeMissiles,listeOvnis, playerControl)
        self.vaisseau_asteroids(vaisseau,listeAsteroides)
        verifierCollisionsTimer = Timer(0.2,partial(self.verfierToutesCollisions, vaisseau, listeOvnis, listeMissiles, listeAsteroides, playerControl))
        verifierCollisionsTimer.start()       
                        
                        
                        
                        



                        