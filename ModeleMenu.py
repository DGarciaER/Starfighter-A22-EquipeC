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