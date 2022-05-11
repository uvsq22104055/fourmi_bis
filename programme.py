import tkinter as tk

LARGEUR = 500
HAUTEUR = 500

def play():
    canvas.itemconfigure

racine = tk.Tk()
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR)
bouton_play = tk.Button(racine, text="play", command=play)

canvas.grid()
bouton_play.grid(row=0, column=1)

racine.mainloop()
