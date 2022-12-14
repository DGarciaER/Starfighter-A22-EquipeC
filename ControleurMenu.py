import tkinter as tk
from tkinter import *
from threading import Timer
from ControleurJeu import Mouvement, Ovnis, Shoot

from ModeleJeu import AireDeJeu, Asteroide, Niveau


class ControleurMenu(tk.Frame):
    def __init__(self, container, window=None):
        super().__init__(window)

        self.timerMoveMissile = 0
        self.timerMoveAsteroide = 0
        self.timerCreateAsteroide = 0
        self.timerCreateOvnis = 0
        self.timerMoveOvnis = 0
        self.vitesseOvni = 0
        
        self.aireDeJeu = AireDeJeu(container)
        self.mvmt = Mouvement(container)
        self.shoot = Shoot(container)
        self.ast = Asteroide(container)
        self.ovni = Ovnis(container)
        self.level = Niveau()

    
    def niveau_facile(self):
        if self.level.niveau == "facile":
            self.timerMoveMissile = 0.03
            self.timerMoveAsteroide = 0.03
            self.timerCreateAsteroide = 5
            self.timerCreateOvnis = 5
            self.timerMoveOvnis = 0.03
            self.vitesseOvni = 2
        
        elif self.level.niveau == "moyen":
            self.timerMoveMissile = 0.03
            self.timerMoveAsteroide = 0.03
            self.timerCreateAsteroide = 3
            self.timerCreateOvnis = 3
            self.timerMoveOvnis = 0.03
            self.vitesseOvni = 5

        elif self.level.niveau == "difficile":
            self.timerMoveMissile = 0.03
            self.timerMoveAsteroide = 0.03
            self.timerCreateAsteroide = 1
            self.timerCreateOvnis = 0.5
            self.timerMoveOvnis = 0.03
            self.vitesseOvni = 10
        


            # Le vaisseau se deplace en suivant la position de la souris
        self.aireDeJeu.canva.bind('<Motion>', self.mvmt.moveVaisseau())

            # Un missile est tiré lorsqu'on fait un click gauche de la souris
        self.aireDeJeu.canva.bind('<Button-1>', self.shoot.shootMissile())

        # Deux lasers sont tirés lorsqu'on fait un double-click gauche de la souris
        self.aireDeJeu.canva.bind('<Button-3>', self.shoot.shootLaser())
        
        wait = Timer(self.timerMoveMissile, self.mvmt.moveMissile())
        wait.start()
        waitA = Timer(self.timerCreateAsteroide, self.ast.createAsteroide())
        waitA.start()
        waitA = Timer(self.timerMoveAsteroide, self.ast.moveAsteroide())
        waitA.start()
        
        #creation ovnis
        waitB = Timer(self.timerCreateOvnis, self.ovni.createOvnis())
        waitB.start()
        waitB = Timer(self.timerMoveOvnis, self.ovni.moveOvnis())
        waitB.start()