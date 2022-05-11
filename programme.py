import tkinter as tk

N=100
LARGEUR = 500
HAUTEUR = 500
LARGEUR_CASE = LARGEUR // N
HAUTEUR_CASE = HAUTEUR // N


damier = None

bord = None


def init_damier():
    """Retourne une grille carrée vide
       dimension N+2, les éléments de la configuration vont de 1 à N
       les indices 0 et N+1 sont les bords et permettent de ne pas gérer
       de cas particuliers
    """
    global damier, bord
    damier = [[0 for i in range(N+2)] for j in range(N+2)]
    bord = [[0 for i in range(N+2)] for j in range(N+2)]
    for i in range(1, N+1):
        x = (i - 1) * LARGEUR_CASE
        for j in range(1, N+1):
            y = (j - 1) * HAUTEUR_CASE
            carre = canvas.create_rectangle(x, y, x+LARGEUR_CASE,
                                            y+HAUTEUR_CASE)
            damier[i][j] = carre


def affiche_damier(config):
    """Affiche la configuration donnée"""
    for i in range(1, N+1):
        for j in range(1, N+1):
            canvas.itemconfigure(damier[i][j])

def play():
    global stop
    if stop:
        stop = False
        bouton_play.configure(text="Stop")
        stabilize()
    else:
        stop = True
        bouton_play.configure(text="Start")
        canvas.after_cancel(id_after)

def pause():
    canvas.itemconfigure()

def next():
    canvas.itemconfigure()

def save():
    """Sauvegarde la config courante dans le fichier sauvegarde"""
    fic = open("save", "w")
    fic.write(str(N)+"\n")
    for i in range(1, N+1):
        for j in range(1, N+1):
            fic.write(str(bord[i][j]))
            fic.write("\n")
    fic.close()

def load():
    """Charge la configuration sauvegardée et la retourne si
    elle a même valeur N que la config courante, sinon retourne config vide
    """
    fic = open("save", "r")
    config = [[0 for i in range(N+2)] for j in range(N+2)]
    ligne = fic.readline()
    n = int(ligne)
    if n != N:
        fic.close()
        return config
    i = j = 1
    for ligne in fic:
        config[i][j] = int(ligne)
        j += 1
        if j == N + 1:
            j = 1
            i += 1
    fic.close()
    return config

racine = tk.Tk()
racine.title("Fourmi")
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR)
init_damier()
bouton_play = tk.Button(racine, text="play", command=play)
bouton_pause =tk.Button(racine, text="pause", command=pause)
bouton_next= tk.Button(racine, text='next', command=next)
bouton_load= tk.Button(racine, text='load', command=load)
bouton_save= tk.Button(racine, text='save', command=save)



canvas.grid(row=0, column=1, rowspan=6)
bouton_play.grid(row=0, column=1)
bouton_pause.grid(row=1, column=1)
bouton_next.grid(row=2, column=1)
bouton_load.grid(row=3, column=1)
bouton_save.grid(row=4, column=1)
racine.mainloop()
