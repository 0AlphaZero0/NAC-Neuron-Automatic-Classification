# #!/usr/bin/env python
# #-*- coding: utf-8 -*-

from numpy import*
import numpy as np
from tkinter import*
from tkinter.messagebox import*
import sys
import pickle

fenetre=Tk()
#
# label=Label(fenetre)
# label.pack
# for ligne in range (10):
#     for colonne in range(9):
#         Button(fenetre, text='L%s-C%s' % (ligne, colonne),borderwidth=1).grid(row=ligne, column=colonne)
#
# fenetre.mainloop

def tableau():
    fenetre= Toplevel()
    Button(fenetre, text="Enregistrer", width=10 ,command=savetexte(M), bg="skyblue3").grid(row=8, column=2)
    Button(fenetre, text="Fermer", width=10 ,command=fenetre.destroy, bg="skyblue3").grid(row=8, column=0)
    for ligne in range (10):
        for colonne in range(9):
            Button(fenetre, text='L%s-C%s' % (ligne, colonne),borderwidth=1).grid(row=ligne, column=colonne)

fenetre.mainloop()
