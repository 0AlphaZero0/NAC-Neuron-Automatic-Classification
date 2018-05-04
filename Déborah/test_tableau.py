# #!/usr/bin/env python
# #-*- coding: utf-8 -*-

from tkinter import *
#
#
# class Interface(Frame):
#
#
#
#     """Notre fenêtre principale.
#
#     Tous les widgets sont stockés comme attributs de cette fenêtre."""
#
#
#
#     def __init__(self, fenetre, **kwargs):
#
#         Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
#
#         self.pack(fill=BOTH)
#
#         self.nb_clic = 0
#
#
#
#         # Création de nos widgets
#
#         self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")
#
#         self.message.pack()
#
#
#
#         self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
#
#         self.bouton_quitter.pack(side="left")
#
#
#
#         self.bouton_cliquer = Button(self, text="Cliquez ici", fg="red",
#
#                 command=self.cliquer)
#
#         self.bouton_cliquer.pack(side="right")
#
#
#
#     def cliquer(self):
#
#         """Il y a eu un clic sur le bouton.
#
#
#
#         On change la valeur du label message."""
#
#
#
#         self.nb_clic += 1
#
#         self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)
#
#
#
# fenetre = Tk()
#
# interface = Interface(fenetre)
#
#
# interface.mainloop()
#
# interface.destroy()




# class IHM(Frame):
#     def __init__(self, fenetre, height, width):
#         Frame.__init__(self, fenetre)
#         self.numberLines = height
#         self.numberColumns = width
#         self.pack(fill=BOTH)
#         self.data = list()
#         for i in range(self.numberLines):
#             line = list()
#             for j in range(self.numberColumns):
#                 cell = Entry(self)
#                 cell.insert(0, 0)
#                 line.append(cell)
#                 cell.grid(row = i, column = j)
#             self.data.append(line)
#
#         self.results = list()
#         for i in range(self.numberColumns):
#             cell = Entry(self)
#             cell.insert(0, 0)
#             cell.grid(row = self.numberLines, column = i)
#             self.results.append(cell)
#         self.buttonSum =  Button(self, text="somme des colonnes", fg="red", command=self.sumCol)
#         self.buttonSum.grid(row = self.numberLines, column = self.numberColumns)
#
#     def sumCol(self):
#         for j in range(self.numberColumns):
#             result = int(0)
#             for i in range(self.numberLines):
#                 result += int(self.data[i][j].get())
#             self.results[j].delete(0, END)
#             self.results[j].insert(0, result)
#
# fenetre = Tk()
# interface = IHM(fenetre, 6, 5)
# interface.mainloop()


#from tkinter import *

# class ScrollableCanvas(Frame):
#      def __init__(self, parent, *args, **kw):
#         Frame.__init__(self, parent, *args, **kw)
#
#         canvas=Canvas(self,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
#
#         vbar=Scrollbar(self,orient=VERTICAL)
#         vbar.pack(side=RIGHT, fill=Y)
#         vbar.config(command=canvas.yview)
#
#         canvas.config(width=200,height=200)
#         canvas.config(yscrollcommand=vbar.set)
#         canvas.pack(side=LEFT,expand=True,fill=BOTH)
#
#         # create a frame inside the canvas which will be scrolled with it
#         self.interior = interior = Frame(canvas)
#         interior_id = canvas.create_window(0, 0, window=interior, anchor=NW )
#
#         # track changes to the canvas and frame width and sync them,
#         # also updating the scrollbar
#         def _configure_interior(event):
#             # update the scrollbars to match the size of the inner frame
#             size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
#             canvas.config(scrollregion="0 0 %s %s" % size)
#             if interior.winfo_reqwidth() != canvas.winfo_width():
#                 # update the canvas's width to fit the inner frame
#                 canvas.config(width=interior.winfo_reqwidth())
#         interior.bind('<Configure>', _configure_interior)
#
#         def _configure_canvas(event):
#             if interior.winfo_reqwidth() != canvas.winfo_width():
#                 # update the inner frame's width to fill the canvas
#                 canvas.itemconfigure(interior_id, width=canvas.winfo_width())
#         canvas.bind('<Configure>', _configure_canvas)
#
#
#
# class Main_frame(Frame):
#     # Init
#     def __init__(self, fenetre_principale=None):
#         Frame.__init__(self, fenetre_principale)
#         self.grid()
#         self.scrollable_canvas = ScrollableCanvas(self)
#         self.scrollable_canvas.grid(row=1,column=1)
#
#         colours = ['red','green','orange','white','yellow','blue','green','orange','white','yellow','blue','green','orange','white','yellow','blue','green','orange','white','yellow','blue']
#         test = ['0','0','1','0','0','1','1','0','1','0','0','1','1','0','1','1','0','1','1','0','1']
#
#         r = 0
#         for a in colours:
#             Label(self.scrollable_canvas.interior, text=a, relief=RIDGE,width=15,bg='white').grid(row=r,column=0)
#             r = r + 1
#
#         r = 0
#         for b in test:
#             Label(self.scrollable_canvas.interior, text=b, relief=RIDGE,width=10,bg='white').grid(row=r,column=1)
#             r = r + 1
#
#
# if __name__ == "__main__":
#     root = Tk()
#     root.title("tk")
#     interface = Main_frame(fenetre_principale=root)
#     interface.mainloop()

from numpy import*
import numpy as np
from tkinter import*
from tkinter.messagebox import*
import sys
import pickle


##Matrice de départ
ligne1=['nClasse','IR','RMP','RH','ST','DTFS','SA','SD','fAHP']
ligne2=[i for i in range(1,10)]
ligne3=[i for i in range(1,10)]
ligne4=[i for i in range(1,10)]
ligne5=[i for i in range(1,10)]
ligne6=[i for i in range(1,10)]
ligne7=[i for i in range(1,10)]
ligne8=[i for i in range(1,10)]

M=[ligne1,ligne2,ligne3,ligne4,ligne5,ligne6,ligne7,ligne8]



##

def savetexte(n): # enregistrement des données dans un fichier
    fichier = open('data.txt','wb')
    pickle.dump(n,fichier)    # sérialisation
    fichier.close()

savetexte(M)

def recuptext(): # récupération des données
    fichier = open('data.txt','rb')
    M= pickle.load(fichier)    # désérialisation
    fichier.close()
    return(M)

M=recuptext()






## Fonctions utiles
def confirmer():#confirmer une action
    fenetre = Toplevel()
    bouton=Button(fenetre, text="Confirmer", command=fenetre.destroy)
    bouton.pack()



def regler(x,ligne,colonne):
    fenetre=Toplevel()
    s=Spinbox(fenetre, text=x,from_=0.0, to=4.00,increment=0.01)
    s.pack()
    x=s.get()
    bouton2=Button(fenetre, text="Fermer", width=10 ,command=fenetre.destroy, bg="red")
    bouton2.pack()
    return (x)
                                                                                                    #################################

## definition des valeurs du tableau

def afficher(number):
    print('Afficher', number)


def tableau():
    fenetre= Toplevel()
    M=recuptext()
    Button(fenetre, text="Enregistrer", width=10 ,command=savetexte(M), bg="green").grid(row=8, column=2)
    Button(fenetre, text="Fermer", width=10 ,command=fenetre.destroy, bg="red").grid(row=8, column=0)
    for colonne in range(len(M[0])):                              # Ligne 0 heure de la journée
        Valeur=M[0][colonne]
        Button(fenetre, text=str(Valeur),width=10).grid(row=0, column=colonne)
    for ligne in range (len(M)):                                # colonne 0 jour de la semaine
        Valeur=M[ligne][0]
        Button(fenetre, text=str(Valeur), width=10) .grid(row=ligne, column=0)
    for colonne in range(1,9):
        for ligne in range (1,len(M)):
            Value=M[ligne][colonne]
            Button(fenetre, text=Value,textvariable=Value, width=10,command=lambda x=Value,y=ligne,z=colonne:regler(x,y,z)).grid(row=ligne, column=colonne)

          #########

def insuline(M,glycemie,jour,heure):
    if glycemie>180:
        if heure==0:
            M[jour+1][heuremax]=int(M[jour+1][heuremax])+1
        else:
            M[jour+1][heure-1]=int(M[jour+1][heure-1])+1
    if glycemie<80:
        if heure==0:
            M[jour+1][heuremax]=int(M[jour+1][heuremax])-1
        else:
            M[jour+1][heure-1]=int(M[jour+1][heure-1])-1
            #########



##
class ScrollableCanvas(Frame):
     def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)

        canvas=Canvas(self,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))

        vbar=Scrollbar(self,orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=canvas.yview)

        canvas.config(width=200,height=200)
        canvas.config(yscrollcommand=vbar.set)
        canvas.pack(side=LEFT,expand=True,fill=BOTH)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior, anchor=NW )

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)


class app():
    #définition de la fenêtre
    fenetre = Tk()
    label = Label(fenetre, text="Classement des neurones", font=('courier', 15, 'bold'),height=3, fg="royalblue3")
    label.pack()
    #ouvrir le tableau
    bouton5=Button(fenetre, text="Tableau",width=20, command=tableau, bg="skyblue3")
    bouton5.pack()
    #bouton d'arrêt
    bouton=Button(fenetre, text="Fermer",width=20, command=fenetre.destroy, bg="skyblue3")
    bouton.pack()
    fenetre.mainloop()




#https://openclassrooms.com/forum/sujet/enregistrer-des-donnees-d-un-tableau-tkinter
#http://www.fil.univ-lille1.fr/~marvie/python/chapitre6.html
