from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from unittest.mock import mock_open
import os.path
from ast import literal_eval

#[h,g,b,d]  
#[1,2,3,4]

RED, GREEN, YELLOW, CYAN = 1, 2, 3, 0
ANT_COLORS = (RED, GREEN, YELLOW, CYAN)
ANT_COULEURS = ('RED', 'GREEN', 'YELLOW', 'CYAN')
stop = FALSE

#case noire fourmi=pion_b
def MooveAnt():
    "Déplacement de la fourmi"
    global ant, case_n, directant
    print("-----")
    print("fourmi sur case noire: ",ant in case_n)
    print("direction fourmi: ",directant)
    if (ant in case_n):   ## si la fourmi est sur case noire, tourne -90° et efface case
        removecase_n()    ## l'effacer la case
        if directant==1:  ##  
            directant=2
            ant-=1        ##x-1
        elif directant==4:
            directant=1
            ant-=t        ##y-1
        elif directant==3:
            directant=4
            ant+=1        ##x+1
        else:
            directant=3
            ant+=t        ##y+1
    else:
        #[h,g,b,d]  
        #[1,2,3,4]
        case_n.append(ant)  ##si case blanche, tourne 90° et couleur noire (append ajoute la case)
        if directant==1:
            directant=4
            ant+=1          ##x+1
        elif directant==4:
            directant=3
            ant+=t          ##y+1
        elif directant==3:
            directant=2
            ant-=1          ##x-1
        else:
            directant=1
            ant-=t          ##y-1
    print("-->",directant)
    print(case_n)
    draw()
    positionAnt()

def removecase_n():
    global ant, case_n
    del case_n[case_n.index(ant)]
    x = ((ant%t))   
    y = (ant//t)
    can1.create_rectangle(x*case, y*case, (x*case)+case, (y*case)+case, fill='dark grey')


def draw():
    "On place les pions"
    global case_n, ant,t
    for rec in case_n:
        if rec != -1:
            x = ((rec%t))   #abscisse fourmi: reste de la division afin de récupére l'unité
            y = (rec//t)    #ordonnée fourmi: division entière afin de récupére la  dizaine
            can1.create_rectangle(x*case, y*case, (x*case)+case, (y*case)+case, fill='black')  #dessine un carré noir

def positionAnt(): #emplacement de la fourmis
        global ant,t,directant
        y = ((ant//t)*case) + case/2   #centre de la case
        x = ((ant%t)*case) + case/2
        can1.create_oval(x-15, y-15, x+15, y+15, fill=ANT_COULEURS[directant-1])   # dessiner la fourmi (c'est un cercle)

def programme():
    global case_n,nbre_iteration,selected,directant,ant,stop
    bt2.config(text="Pause")
    stop = not stop
    nbre_iteration=0
    t=10    ## Nombre de cases
    case = 40    ## Taille en pixel d'une case
    selected=1
    directant=1
    ant = t*(t+1)/2  ## Coordonnées de la fourmi au départ 55 (x=t/2 et y=t/2)
    case_n = []  ##Réinitiale le sol
    can1.create_rectangle(0, 0, (t*case), (t*case), fill='dark grey')   ##Crée un rectangle gris (couleur du sol) pour tout effacer
    positionAnt()
    fenetre.update()
    while(stop!=TRUE):
        fenetre.after(100,MooveAnt())
        nbre_iteration+=1
        fenetre.update()
    bt2.config(text="PLAY")
def save():
    global t,case_n,nbre_iteration
    
    with open(r"C:\save.txt", 'w+') as fic:  ## mettre le chemin vers le fichier
        chaine="Taille en pixel d'une case: "+str(t)
        itera="Nombre d'itération: "+str(nbre_iteration)
        fic.write(f'{chaine}\n{itera}\n{case_n}\n{int(ant)}')
    fic.close()

def load():
    global case_n,ant
    lignes = []
    fic = open(r"C:\save.txt", "r")   ## mettre le chemin vers le fichier
    contenu = fic.readlines()
    for ligne in contenu:
        lignes.append(ligne)
    case_n = literal_eval(lignes[2])  ## va permettre de redessiner les cases noires
    ant=int(lignes[3])                ## va permettrede redessiner la fourmi
    can1.create_rectangle(0, 0, (t*case), (t*case), fill='dark grey')   ##Crée un rectangle gris (couleur du sol) pour tout effacer
    fenetre.update()
    draw()
    positionAnt()
    fic.close()

def next():
    global nbre_iteration
    nbre_iteration+=1
    MooveAnt()

#_____Création de l'interface réunissant le sol et les boutons_______
def interface():
    "Dessine la GUI"
    global fenetre, can1,bt2, chaine, txt1, ant, selected, directant,t

    #----création de la fenetre----
    fenetre = Tk()
    fenetre.title("Fourmis de Langton")
    #----création de la surface graphique----
    can1 = Canvas(fenetre, width=case*t, height=case*t, bg='dark grey')
    can1.pack(side=TOP)
    #----creation de zone de texte----
    chaine = Label(fenetre)
    chaine.configure(text="", fg='red')
    chaine.pack()
    txt1 = Label(fenetre, text='')
    txt1.pack()
    bt2 = Button(fenetre, text='play', command=programme)
    bt2.pack(side=BOTTOM)
    quit_boutton = Button(fenetre, text='Quit', command=fenetre.quit)
    quit_boutton.pack(side = LEFT)
    bouton_next= Button(fenetre, text='next', command=next)
    bouton_next.pack(side=LEFT)
    bouton_load= Button(fenetre, text='load', command=load)
    bouton_save= Button(fenetre, text='save', command=save)
    bouton_load.pack(side=RIGHT)
    bouton_save.pack(side=RIGHT)
    fenetre.mainloop()

#--- Programme principal ---
t=10    ## Nombre de cases
case = 40    ## Taille en pixel d'une case
selected=1
directant=1
ant = t*(t+1)/2  ## Coordonnées de la fourmi au départ 55 (x=t/2 et y=t/2)
case_n = []

interface()