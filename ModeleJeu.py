import tkinter as tk

class AireDeJeu:
    """
    Class AireDeJeu initialise l'aire jouable dans l'application.
    Prend le container comme parametre.
    """
    def __init__(self, container):
        self.height = 500
        self.width = 450 
        self.imageBackground = tk.PhotoImage(file='Images/Background.png').subsample(2,2)

        self.canva = tk.Canvas(container, height=self.height, width=self.width)
        self.canva.create_image(10,10, image=self.imageBackground)
        self.canva.grid(column=1, row=1, padx=20) # pour centrer et donner un padding
        # self.canva.config(cursor="none")

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

class Laser:
    """
    Cette classe permet de creer un laser, qui sera tire par l'utilisateur
    Parameters: Le container tkinter (AirDeJeu) et les coordonnes du laser
    """
    def __init__(self,container, xCoinDroitHaut, yCoinDroitHaut, xCoinDroitBas, yCoinDroitBas, ):
        # self.x = x
        # self.y = y
        self.rectangleLaser = container.canva.create_rectangle(xCoinDroitHaut, yCoinDroitHaut, xCoinDroitBas, yCoinDroitBas, fill="red")
        # self.imageMissile = tk.PhotoImage(file='Images/missile.png').subsample(3,3)
        # self.instanceMissile = container.canva.create_image(self.x, self.y, image=self.imageMissile)

class Ovni:
    def __init__(self,container, x, y):
        self.x = x
        self.y = y
        self.imageOvni = tk.PhotoImage(file='Images/ovni.png').subsample(4,4) #Creation de l'image Ovni
        self.instanceOvni = container.canva.create_image(self.x,self.y,anchor=tk.NW,image=self.imageOvni)
        
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
            self.imageAsteroide = tk.PhotoImage(file='Images/asteroide.gif').subsample(4,4) #Creation de l'image Asteroide
        else:
            self.imageAsteroide = tk.PhotoImage(file='Images/asteroideFlipped.png').subsample(4,4) #Creation de l'image Asteroide

        
        self.instanceAsteroide = container.canva.create_image(self.x, self.y, anchor=tk.NW,image=self.imageAsteroide) #Placer l'image dans le container
        
class Niveau:
    def __init__(self):
        self.niveau = "none"

    """methode pour definir le niveau facile du jeu"""
    
    def level_facile(self):
        self.niveau = "facile"

    def level_moyen(self):
        self.niveau = "moyen"

    def level_difficile(self):
        self.niveau = "difficile"
            