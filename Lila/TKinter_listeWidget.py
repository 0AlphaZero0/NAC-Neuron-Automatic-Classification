#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from Tkinter import *
#https://docs.python.org/3/library/tkinter.html
#https://openclassrooms.com/courses/apprenez-a-programmer-en-python/des-interfaces-graphiques-avec-tkinter
#Xlib (C) the Xlib library to draw graphics on the screen.
try:
    try:
        from tkinter import * #Pour Python 2
    except:
        from Tkinter import * #Pour Python 3
except:
    raise ImportError('Wrapper Tk non disponible')


# On crée une fenêtre (la fenetre principale), racine de notre interface
fenetre = Tk()


# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text="Hello World", fg='red')

# On affiche le label dans la fenêtre, methode label sert a positionner objet dans fenetre
champ_label.pack()



#LES BOUTONS
#Bouton pour quitter application
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)
bouton_quitter.pack()


#LIGNE DE SAISIE
#cree une zone de texte ou l'utilisateur peut ecrire
var_texte = StringVar()
ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)
ligne_texte.pack()



#LES CASES A COCHER
var_case = IntVar()
case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)
case.pack()
#Pour controler etat de la case :
var_case.get() #si cochee = 1, si pas cochee = 0



# POUR FAIRE RADIO BUTTON = REGROUPEMENT DE BOUTONS, choix  a l'utilsateur de pouvoir prendre qu'un seul des boutons proposes. Il ne peut pas en cocher plusieurs parmi eux.
var_choix = StringVar()

choix_rouge = Radiobutton(fenetre, text="Rouge", variable=var_choix, value="rouge")
choix_vert = Radiobutton(fenetre, text="Vert", variable=var_choix, value="vert")
choix_bleu = Radiobutton(fenetre, text="Bleu", variable=var_choix, value="bleu")

choix_rouge.pack()
choix_vert.pack()
choix_bleu.pack()
#Pour interroger la variable associe au bouton :
var_choix.get()

#POUR FAIRE LISTES DEROULANTES, ici on peut selectionner un ou plusieurs elements
liste = Listbox(fenetre)
liste.pack()#creer la liste
#inserer dans la liste : et mettre end si on veut que ça s'insere à la fin. INSERT prend 2 parametre, la position ou l'inserer et l'element en lui meme
liste.insert(END, "Pierre")
liste.insert(END, "Feuille")
liste.insert(END, "Ciseau")
#pour acceder a la selection utiliser liste.cureselection() (pas trop compris a quoi ça sert)

#ORGANISER TOUS SES WIDGETS AVEC FRAME
cadre = Frame(fenetre, width=768, height=576, borderwidth=1)#on utilise Frame comme parent pour que le widget soit dans un cadre
cadre.pack(fill=BOTH)

message = Label(cadre, text="Notre fenêtre")
message.pack(side="top", fill=X) #top sert a placer notre widget en haut de so#pour acceder a la selection utiliser liste.cureselection() (pas trop compris a quoi ça sert)
#fill sert au widget à remplir le widfet parent soit en largeur avec X, soit en hauteur avec Y, soit les deux avec BOTH
#ORGANISER TOUS SES WIDGETS AVEC FRAME
cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
n parent, ici le cadre




# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
