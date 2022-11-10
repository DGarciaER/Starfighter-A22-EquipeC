import c31Geometry2 as c31

class CarreRouge:
    tailleCarreRouge = 40
    
    def __init__(self, container):
        
        # initialisation du Carre Rouge
        couleur = '#ed4242'
        self.carreRouge = c31.Carre(container, c31.Vecteur(225,225),self.tailleCarreRouge,0, couleur, couleur, 0)




