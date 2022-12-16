class Niveau:
    '''Classe pour definir le niveau de difficulté du jeu'''
    def __init__(self):
        self.niveau = "none"
    
    def level_facile(self):
        self.niveau = "facile"

    def level_moyen(self):
        self.niveau = "moyen"

    def level_difficile(self):
        self.niveau = "difficile"