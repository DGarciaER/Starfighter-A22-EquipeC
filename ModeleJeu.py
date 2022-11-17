import tkinter as tk

class AireDeJeu:
    def __init__(self, container):
        self.height = 500
        self.width = 450 
        self.imageBackground = tk.PhotoImage(file='Images/Background.png').subsample(2,2)

        self.canva = tk.Canvas(container, height=self.height, width=self.width)
        self.canva.create_image(10,10, image=self.imageBackground)
        self.canva.grid(column=1, row=1, padx=20) # pour centrer et donner un padding

class Vaiseau:
    def __init__(self, container):
        self.imageVaisseau = tk.PhotoImage(file='Images/Vaisseau.png').subsample(2,2)
        self.x = 0
        self.y = 0

    def setPositions(self,x,y):
        self.x = x
        self.y = y


class Missile:
    def __init__(self,container, x, y):
        self.x = x
        self.y = y
        self.imageMissile = tk.PhotoImage(file='Images/missile.png').subsample(3,3)
        self.instanceMissile = container.canva.create_image(self.x, self.y, image=self.imageMissile)

class Ovni:
    def __init__(self,container, x, y):
        self.x = x
        self.y = y
        self.imageOvni = tk.PhotoImage(file='Images/ovni.png').subsample(4,4)
        self.instanceOvni = container.canva.create_image(self.x,self.y,anchor=tk.NW,image=self.imageOvni)
        
        