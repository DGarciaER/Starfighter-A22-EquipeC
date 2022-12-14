
import random
from threading import Timer
from ControleurMenu import ControleurMenu
from ModeleJeu import AireDeJeu, Asteroide, Laser, Ovni, Vaiseau, Missile
from VueJeu import VueJeu
from tkinter import *
import tkinter as tk
import c31Geometry2 as c31



class ControleurJeu(tk.Frame):
    def __init__(self, container, window=None):
        super().__init__(window)
    
        self.window = window


class Mouvement(tk.Frame):

    def __init__(self, container, window=None):
        super().__init__(window)

        self.aireDeJeu = AireDeJeu(container)
        self.vaisseau = Vaiseau(self.aireDeJeu)
        self.imageV = self.vaisseau.imageVaisseau


        """Methode qui permet le mouvement du vaisseau lorsque la souris se deplace"""
    def moveVaisseau(self, e):

        #Récupérer l'image de Vaisseau et reduire sa taille avec la méthode subsample
        # Créer une instance de Vaisseau et l'afficher dans l'aire de jeu en lui donnant une position x, y
        self.imageV = tk.PhotoImage(file='Images/Vaisseau.png').subsample(12,12)

        # FIXME non utilise...
        instanceV = self.aireDeJeu.canva.create_image(e.x,e.y, image=self.imageV)

        self.vaisseau.setPositions(e.x,e.y)

class Shoot(tk.Frame):
    def __init__(self, container, window=None):
        super().__init__(window)

        self.listeMissiles = []
        self.listLaser = []
        
        self.imageV = self.vaisseau.imageVaisseau
        self.aireDeJeu = AireDeJeu(container)
        self.vaisseau = Vaiseau(self.aireDeJeu)

    def shootMissile(self, event):
        self.listeMissiles.append(Missile(self.aireDeJeu, event.x, event.y))

    def moveMissile(self):
        for missile in self.listeMissiles:
            self.aireDeJeu.canva.move(missile.instanceMissile, 0, -10)
            missile.y -=10

            if missile.y <= 0:
                self.aireDeJeu.canva.delete(missile.instanceMissile)
                self.listeMissiles.remove(missile)
                # print('deleted')
        wait = Timer(0.03, self.moveMissile())
        wait.start()

    """Methode qui creer les lasers et les ajoute a la listLaser"""
    def shootLaser(self ,event):
        if self.vaisseau.laserCooldown == False:
            self.vaisseau.laserCooldown = True
            self.listLaser.append(Laser(self.aireDeJeu, (event.x - self.imageV.width()/4 - 4), 0, (event.x - self.imageV.width()/4 - 2), event.y))
            self.listLaser.append(Laser(self.aireDeJeu, (event.x + self.imageV.width()/4 + 3), 0, (event.x + self.imageV.width()/4 + 5), event.y))
            self.aireDeJeu.canva.after(1000, self.deleteLaser())
            self.aireDeJeu.canva.after(5000, self.resetCooldown())
    
    def resetCooldown(self):
        self.vaisseau.laserCooldown = False
        print( "in resetCooldown")

    """Methode qui supprime les lasers"""
    def deleteLaser(self):
        self.aireDeJeu.canva.delete(self.listLaser[1].rectangleLaser)
        del self.listLaser[1]
        self.aireDeJeu.canva.delete(self.listLaser[0].rectangleLaser)   
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


class Ovnis(tk.Frame):

    def __init__(self, container, window=None):
        super().__init__(window)
        self.listeOvnis = []

        self.aireDeJeu = AireDeJeu(container)
        self.cMenu = ControleurMenu(self.aireDeJeu)
    
    def createOvnis(self):
        if random.randint(0,1) == 0:
            # on fait partir l'ovnis a gauche
            x = random.randint(25,200)
            self.listeOvnis.append(Ovni(self.aireDeJeu,x,-40))

        else:
            #on fait partir l'ovnis à droite
            x = random.randint(250,425)
            self.listeOvnis.append(Ovni(self.aireDeJeu,x,-40))

        print(self.cMenu.timerMoveOvnis)

        waitB = Timer(self.cMenu.timerCreateOvnis, self.createOvnis())#cree un ovnis a chaque 3s
        waitB.start()

    """Methode qui permet le mouvement des ovnis"""
    def moveOvnis(self):
        
        for ovn in self.listeOvnis: # forEach qui passe dans toute la list listAsteroide
            # print(aste.direction)
                self.aireDeJeu.canva.move(ovn.instanceOvni,0 ,self.cMenu.vitesseOvni)#deplacement de l'ovnis en x = 0, y = 2
                ovn.y += self.cMenu.vitesseOvni
                
                if ovn.y >= 500:
                    self.aireDeJeu.canva.delete(ovn.instanceOvni)
                    self.listeOvnis.remove(ovn)
        
        newWait = Timer(self.cMenu.timerMoveOvnis, self.moveOvnis())
        newWait.start()


    



class Asteroides(tk.Frame):
    def __init__(self, container, window=None):
        super().__init__(window)
        self.listAsteroides = []

        self.aireDeJeu = AireDeJeu(container)
    
    def createAsteroide(self):
        
        if random.randint(0,1) == 0:
            # on fait partir l'asteroide a gauche
            x = random.randint(25,200)
            # print(x)
            self.listAsteroide.append(Asteroide(self.aireDeJeu,x,-40,"bas-droit"))

        else:
            #on fait partir l'asteroide à droite
            x = random.randint(250,425)
            self.listAsteroide.append(Asteroide(self.aireDeJeu,x,-40,"bas-gauche"))


        waitA = Timer(8, self.createAsteroide())
        waitA.start()

    """Methode qui permet le mouvement des asteroides"""
    def moveAsteroide(self):
        
        for aste in self.listAsteroide: # forEach qui passe dans toute la list listAsteroide
            # print(aste.direction)

            if aste.direction == "bas-droit":
                self.aireDeJeu.canva.move(aste.instanceAsteroide,5 ,5)
                aste.y += 5
                aste.x += 5

            elif aste.direction == "bas-gauche":
                self.aireDeJeu.canva.move(aste.instanceAsteroide,-5 ,5)
                aste.y += 5
                aste.x -= 5


            if aste.y >= 500:
                self.aireDeJeu.canva.delete(aste.instanceAsteroide)
                self.listAsteroide.remove(aste)

                # print('deleted')
            

        newWait = Timer(0.03, self.moveAsteroide())
        newWait.start()



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
                    PlayerControl.perte_hp()
                    
                
            # print(OL)
            # print(ovni.imageOvni.width())
            # print(OR)
            # print("taille de image vaisseau: " + str(vaisseau.imageVaisseau.width()/2))
            # print("Position of souris: " + str(e.x))
            # print("Position of vaisseau-top: " + str(VL))
    
    def missiles_ovnis(self, listeMissiles, listeOvnis, player):
        
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
                        player.score += 1
                        print(player.score)

                        
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
                        
                        
                        
                        



                        