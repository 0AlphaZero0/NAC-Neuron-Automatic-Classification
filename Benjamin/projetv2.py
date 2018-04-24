 # coding: utf-8
from Tkinter import *
#import Tkinter, Tkconstants, tkFileDialog
import tkFileDialog

######Definitions


def Chargementtest(): #### Permet de retourner le chemin absolue permet l'acces au fichier
	name = tkFileDialog.askopenfilename(initialdir = "/",title = "Selection du fichier test",filetypes = (("Fichier csv","*.csv"),("Fichier texte","*.txt"),("Tous les fichiers","*.*")))
	print (name)
	return (name)
######Recuperer cette putain d'entrée<<<<<<<<<<<<<<<<


def Chargemententrainement():
	entrainement=Tk()
	entrainement.title("Le fichier d'entraînement")
	app.geometry("800x600+600+300")
	textefichier="Avez-vous un jeu d'essai?"
	fichiers=Label(entrainement,text=textefichier)
	fichiers.pack()
	global variableatester
	variableatester=StringVar()
	variableatester.set('True')
	R1 = Radiobutton(entrainement, text="Option 1", variable=variableatester, value='False',command=resultatsappui)
	R1.pack( anchor = W )
	R2 = Radiobutton(entrainement, text="Option 2", variable=variableatester, value='False', command=resultatsappui)
	R2.pack(anchor = W)
	print variableatester
	#radio0 = Radiobutton(entrainement, text="Appui prolonge", variable=variableatester, value=0, command=resultatsappui)
	#radio1 = Radiobutton(entrainement, text="Oui", variable=variableatester, value=1, command=resultatsappui)
	#radio2 = Radiobutton(entrainement, text="Non", variable=variableatester, value=2, command=resultatsappui)
	#radio3 = Button(entrainement, text="Valider", command=entrainement.destroy,width=10)
	#radio1.pack(side="top");radio2.pack(side="bottom");radio3.pack();radio0.pack()

	entrainement.mainloop()

def resultatsappui():
	print str(variableatester.get())
	if variableatester==0:
			nameentrainement = tkFileDialog.askopenfilename(initialdir = "/",title = "Selection du fichier entrainement",filetypes = (("Fichier csv","*.csv"),("Fichier texte","*.txt"),("Tous les fichiers","*.*")))
			print (nameentrainement)
			return (nameentrainement)
	if variableatester==1:
			nomentrainement=()####Chemin de notre fichier test


	#text1=Label(entrainement,text="Choisir le fichier d'entraînement",fg="black",bg="white")

def Parametres(): #### A faire suivant les paramètres sortant
	print "Selection et fixation des paramètres"

def Lanceranalyse():
	print "Lancer l'analyse"

def presentation():
	presentation=Tk()
	presentation.title("Presentation")
	app.geometry("800x600+600+300")
	textepresentation="Actuellement etudiant en master I à l'Université de Bordeaux,\n nous avons pour projet de classer des neurones en deux types : Type I et Type II. \n"
	text=Label(presentation,text=textepresentation)
	text.pack()
	presentation.mainloop()

def explicationlogiciel():
	explication=Tk()
	explication.title("Le logiciel")
	app.geometry("1000x500+600+300")
	texteexplication="Présentation du logiciel : \n - Chargement du fichier test : Prend en entrée le fichier test au format .csv et .txt où l'analyse va être réalisé \n - Choisir le fichier d'entrainement : Si le client dispose d'un fichier d'entraînement ayant les types de neurones, il peut le charger sinon un jeu lui sera fourni \n - Paramètres : Concerne le reglage des paramètres à prendre un compte pour l'analyse \n  - Lancer : Permet de lancer l'analyse et d'y afficher les resultats dans une nouvelle fenetre"   ###A mettre en forme
	text=Label(explication, text=texteexplication)
	text.pack()
	explication.mainloop()


def alert():#####Commande bouton du haut
    showinfo("fonctionne")



#####Fenetre principale
app = Tk()
app.title("Classification neuronale") # donne un titre à la fenêtre
app.geometry("800x600+600+300") # place la fenêtre


######## Creation de tous les boutons de chargement
text=Label(app, text="Classification Neuronale", fg="Black", bg="white")   #####Mettre en gras et en gros (titre)
b1= Button(app, text="Chargement du fichier test", command=Chargementtest, width=25)
b2= Button(app, text="Choisir le fichier d'entraînement", fg="black", command=Chargemententrainement,width=25)
b3= Button(app, text="Paramètres", fg="black",command=Parametres,width=25)
b4= Button(app, text="Lancer", fg="black", command=Lanceranalyse)
b5= Button(app, text="Quitter", fg="black", command=app.destroy,width=10)
b1.place(x=300, y=100, width=200, height=40)
b2.place(x=300, y=170, width=200, height=40)
b3.place(x=300, y=240, width=200, height=40)
b4.place(x=300, y=470, width=200, height=50)
b5.place(x=300, y=550, width=200, height=25)
text.place(x=300, y=0, width=200, height=50)

###### Barre de menu
menubar = Menu(app)
menu1 = Menu(menubar, tearoff=0)
menu1.add_separator()
menu1.add_command(label="Créer un nouveau projet", command=alert)
menu1.add_separator()
menu1.add_command(label="Ouvrir un projet", command=alert)
menu1.add_separator()
menu1.add_command(label="Enregistrer le projet en cours", command=alert)
menu1.add_separator()
menubar.add_cascade(label="Fichier", menu=menu1) ######Nom sur la barre de menu

menu2 = Menu(menubar, tearoff=0)
menu2.add_separator()
menu2.add_command(label="Regler les paramètres", command=alert)
menu2.add_separator()
menubar.add_cascade(label="Option", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_separator()
menu3.add_command(label="Qui sommes nous?", command=presentation)
menu3.add_separator()
menu3.add_command(label="Explication du logiciel", command=explicationlogiciel)
menu3.add_separator()
menubar.add_cascade(label="Aide", menu=menu3)

app.config(menu=menubar)
app.mainloop()


############# Variables
