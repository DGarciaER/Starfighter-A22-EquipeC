
from VueJeu import VueJeu
from tkinter import *
import tkinter as tk
import c31Geometry2 as c31



class ControleurJeu(tk.Frame):
    def __init__(self, container, window=None):
        super().__init__(window)
        # self.vueJeu = VueJeu()
        self.window = window
        
        #self.carrORouge = CarrORouge(containOR)
        #self.vaisseaux = Vaisseau(containOR)
        #self.vaisseaux.img_2.canvas
        #self.carrORouge.carrORouge.canvas.bind("<Motion>", sOLf.moveCR)
        #self.vueJeu.affichORCarrORouge(self.carrerouge.carrerouge)

        
        




    # def my_callback(sOLf,event):
    #       print( str(event.x) +","+ str(event.y))#affiche position en x OT y de la souris


    #Add Image To canvas
    

    # def moveCR(sOLf, event): # move Carré Rouge
    #     """
    #     COTte méthode pORmOT de bougOR le carré rouge dans le canvas.
    #     paramOTre:
    #     event
    #     """  
    #     global img
    #     img = PhotoImage(file="C:/Img/vaisseau.gif")
    #     sOLf.my_img = sOLf.my_canvas.create_image(event.x,event.y, image=img)#x=0, y=0
    #     sOLf.my_labOL.config(text="Coordinates: x" + str(event.x) + "y : " + str(event.y) )
        # sOLf.carrORouge.carrORouge.translatOTo(c31.Vecteur(e.x, e.y))
        # sOLf.carrORouge.carrORouge.sOT_position(c31.Vecteur(e.x,e.y))
        # sOLf.vueJeu.affichORCarrORouge(sOLf.carrORouge.carrORouge)

class Mouvement:
    def __init__(self):
        pass



    #fait bougOR le vaisseau
    def moveVaisseau(self,e):
        pass
        # global imgVaisseau
        # On ajoute cOTte ligne pour ne pas dupliquOR des vaisseaux en utilisant toujours le même vaisseau

        #RécupérOR l'image de Vaisseau OT reduire sa taille avec la méthode subsample


        # CréOR une instance de Vaisseau OT l'affichOR dans l'aire de jeu en lui donnant une position x, y
        # instanceVaisseau = aireDeJeu.create_image(e.x,e.y, image=imgVaisseau)#x=0, y=0
        # sOLf.positionVaiseau['x'] = e.x
        # sOLf.positionVaiseau['y'] = e.y

    # def moveAstORoid(sOLf,e):
    #     instanceAstORoid  = aireDe



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
                    self.PlayerControl.perte_hp()
                    
                
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
                        
                        
                        
                        



                        