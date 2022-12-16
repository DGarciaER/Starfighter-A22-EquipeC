import random
import tkinter as tk

class AireDeJeu:
    """
    Class AireDeJeu initialise l'aire jouable dans l'application.
    Prend le container comme parametre.
    """
    def __init__(self, container):
        self.height = 500
        self.width = 450 
        self.imageBackground = tk.PhotoImage(file='Images/Background.png').subsample(2,2) #Image de fond
        
        self.canva = tk.Canvas(container, height=self.height, width=self.width)
        self.canva.create_image(10,10, image=self.imageBackground)
        self.canva.grid(column=1, row=1, padx=20) # pour centrer et donner un padding
        self.canva.config(cursor="none")
        # self.canva.configure(bg="black")
        # self.imageBackground = None
        

class Player:
    '''
    Cette classe initialise un joueur. L'utilisateur commence toujours une partie avec 0 de score et 10 points de vie (HealthPoints)
    '''
    def __init__(self):
        self.score = 0
        self.hp = 10 #Points de vie


class Vaiseau:
    """
    Class Vaiseau permet l'initialisation de l'objet vaisseau, controlable par l'utilisateur
    Parameters: Container, pour pouvoir placer le vaisseau dans l'air de jeu.
    """
    def __init__(self, container):
        self.imageVaisseau = tk.PhotoImage(file='Images/Vaisseau.png').subsample(6,6)
        self.x = 0
        self.y = 0
        self.laserCooldown = False
        self.missileCooldown = False

    def setPositions(self,x,y):
        self.x = x
        self.y = y


class Missile:
    """
    Class Missile permet d'initialiser un objet missile, prend les coordonnes ainsi que le container tkinter comme paramatre.
    """
    def __init__(self,container, x, y):
        self.x = x
        self.y = y
        self.imageMissile = tk.PhotoImage(file='Images/missile.png').subsample(3,3)
        self.instanceMissile = container.canva.create_image(self.x, self.y, image=self.imageMissile)

class Mine:
    """
    Class Mines permet d'initialiser un objet mine, prend les coordonnes ainsi que le container tkinter comme paramatre.
    """
    def __init__(self,container, x, y):
        self.x = x
        self.y = y
        self.imageMine = tk.PhotoImage(file='Images/mine.png').subsample(7,7)
        self.instanceMine = container.canva.create_image(self.x, self.y, image=self.imageMine)

class Laser:
    """
    Cette classe permet de creer un laser, qui sera tire par l'utilisateur
    Parameters: Le container tkinter (AirDeJeu) et les coordonnes du laser
    """
    def __init__(self,container, xCoinGaucheHaut, yCoinGaucheHaut, xCoinDroitBas, yCoinDroitBas, ):
        self.rectangleLaser = container.canva.create_rectangle(xCoinGaucheHaut, yCoinGaucheHaut, xCoinDroitBas, yCoinDroitBas, fill="red")
        self.x = xCoinGaucheHaut + ((xCoinDroitBas - xCoinGaucheHaut)/2) # x c'est la moitie du width du laser

class Ovni:
    '''
    Cette classe s'occupe d'initialiser un objet ovni. Il comprend les cordonees ainsi que l'image de l'ovni.
    '''
    def __init__(self,container, x, y):
        self.x = x
        self.y = y
        self.imageOvni = tk.PhotoImage(file='Images/ovni.png').subsample(4,4) #Creation de l'image Ovni
        self.instanceOvni = container.canva.create_image(self.x,self.y,anchor=tk.NW,image=self.imageOvni)
        self.direction = "right"
        
class Asteroide:
    """
    Cette classe permet l'initialisation d'un asteroide dans l'air de jeu,
    Parameters: Les cordonnes (X, Y) ainsi que la direction de l'asteroide.
    """
    def __init__(self,container, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        if self.direction == "bas-droit":
            self.imageAsteroide = tk.PhotoImage(file='Images/asteroide.gif').subsample(4,4)                             #Creation de l'image Asteroide
        else:
            self.imageAsteroide = tk.PhotoImage(file='Images/asteroideFlipped.png').subsample(4,4)                      #Creation de l'image Asteroide
        self.instanceAsteroide = container.canva.create_image(self.x, self.y, anchor=tk.NW,image=self.imageAsteroide)   #Placer l'image dans le container
        

class PowerUp:
    '''
    Cette classe permet d'initialiser les bonus (power up). Elle est utilise dans controleur jeu.
    '''
    def __init__(self,container, x, y):
        self.x = x
        self.y = y
        # On defini ici, de façon aleatoire (50% de chance), si le bonus est un bonus de vie ou un bonus de score.
        if random.randint(0,1) == 0:
            self.type = "Score"
            self.imagePU = tk.PhotoImage(file='Images/powerUP_Score.png').subsample(7,7) #Creation de l'image Powerup TODO generation aleatoire pour l'image et string? pour differencier quel powerup c'est
        else:
            self.type = "Lives"
            self.imagePU = tk.PhotoImage(file='Images/powerUP_vie.png').subsample(10,10)
            
        print(self.type)
        
        self.instancePU = container.canva.create_image(self.x,self.y,anchor=tk.NW,image=self.imagePU)
    
class Explosion:
    '''
    Cette classe permet d'initialiser les explosions. Elle est utilise dans controleur jeu.
    '''
    def __init__(self,container, x, y):
        self.x = x
        self.y = y
        self.imageExplosion = tk.PhotoImage(file='Images/explosion1.png').subsample(15,15) #Creation de l'image Explosion
        self.instanceExplosion = container.canva.create_image(self.x,self.y,anchor=tk.NW,image=self.imageExplosion)