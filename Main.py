import tkinter as tk
from ControleurJeu import ControleurJeu

if __name__ == "__main__":

    # créer une fenetre tk avec un titre, un background et des dimensions
    couleurTheme = "#41157A"
    root = tk.Tk()
    root.title("Star Fighter")
    root.config(background= couleurTheme)
    root.geometry("510x680")

    # créer un containter et le centrer dans la fenetre tk
    mainContainer = tk.Frame(root, background= couleurTheme)
    mainContainer.pack() # pour centrer et donner un padding
    
    # créer un titre de jeu et le mettre dans un grid en lui donnant du padding
    titre = tk.Label(mainContainer, text="Star Fighter", fg='#FFFC33', background= couleurTheme)
    titre.configure(font=("MV Boli", 25, "bold"))
    titre.grid(column=1, row=0, padx=10, pady=10)
                    
    # créer l'aire de jeu et le mettre dans un grid en lui donnant du padding
    aireDeJeu = tk.Canvas(mainContainer, height=500, width=450, background="#1C0934")
    aireDeJeu.grid(column=1, row=1, padx=20) # pour centrer et donner un padding   
    imgFile = 'Images/Background.png'
    img = tk.PhotoImage(file=imgFile)
    img_2 = img.subsample(2,2) #on reduit la taille de limage
    
    aireDeJeu.create_image(10,10, image=img_2) 

    # créer un container pour afficher les scores en meme temps du jeu.
    statsContainer = tk.Canvas(mainContainer, height=20, width=450,background= couleurTheme, highlightthickness=0)
    statsContainer.grid(column=1, row=3, padx=10, pady=5) # pour centrer et donner un padding

    score = tk.Label(statsContainer, text="   Score:  0  ", fg='#FFFD85',background= couleurTheme)
    score.grid(column=1, row=1, padx=10) # pour centrer et donner un padding

    lives = tk.Label(statsContainer, text="   Vies:  0  ", fg='#FFFD85',background= couleurTheme)
    lives.grid(column=2, row=1, padx=10) # pour centrer et donner un padding

    ability = tk.Label(statsContainer, text="   Abilités:  None  ", fg='#FFFD85',background= couleurTheme)
    ability.grid(column=3, row=1, padx=10) # pour centrer et donner un padding

    # créer un container des buttonset le mettre dans un grid en lui donnant du padding
    buttonsContainer = tk.Canvas(mainContainer, background= couleurTheme, highlightthickness=0)
    buttonsContainer.grid(column=1, row=4, padx=10, pady=20) # pour centrer et donner un padding

    couleurButtons = "#E22866"

    # créer un button qui commence une nouvelle session et le mettre dans un grid en lui donnant du padding
    buttonNouvSession = tk.Button(buttonsContainer, text="         Button1         ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'))
    buttonNouvSession.grid(column=1, row=1, padx=15)
    
    jeu = ControleurJeu(aireDeJeu)

    # créer un button qui affiche le menu score un nouveau jeu et le mettre dans un grid en lui donnant du padding
    buttonMenuScores = tk.Button(buttonsContainer, text="         Button2         ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'))
    buttonMenuScores.grid(column=2, row=1, padx=15)

    # créer un button quitte du programme et le mettre dans un grid en lui donnant du padding
    buttonQuitter = tk.Button(buttonsContainer, text="         Button3         ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'))
    buttonQuitter.grid(column=3, row=1, padx=15)
    
    # boocler la fenetre tk
    root.mainloop()