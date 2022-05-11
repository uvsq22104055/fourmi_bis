import tkinter as tk

LARGEUR = 500
HAUTEUR = 500

def play():
    canvas.itemconfigure()

def pause():
    canvas.itemconfigure()

def next():
    canvas.itemconfigure()

racine = tk.Tk()
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR)
bouton_play = tk.Button(racine, text="play", command=play)
bouton_pause =tk.Button(racine, text="pause", command=pause)
bouton_next= tk.Button(racine, text='pause', command=pause)

canvas.grid()
bouton_play.grid(row=0, column=1)
bouton_pause.grid(row=1, column=1)
bouton_next.grid(row=2, column=1)
racine.mainloop()
