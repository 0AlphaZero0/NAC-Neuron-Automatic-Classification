 # coding: utf-8
 #BLAIS Benjamin
 #COTTAIS Déborah
 #DE OLIVEIRA Lila
 #JOUAN Clement
 #THOUVENIN Arthur
 
from Tkinter import *
import tkFileDialog  ##Permet de Charger les fichiers
from matplotlib.figure import * #Importe les parametres de matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #Importe tkinter
import matplotlib.pyplot as plt
import tkFont
######################## SI BESOIN
import sys
import os
import random
import codecs
#######################

from sklearn import datasets
from sklearn import svm
from csv import reader
from matplotlib import style
import numpy as np
import matplotlib.pyplot as plt
import urllib
style.use("ggplot")

#####Fenetre principale
app = Tk()
app.title("Classification neuronale") # donne un titre à la fenêtre
app.geometry("800x600+600+300") # place la fenêtre
app.configure(background='SlateGray2')#fond du programme



############# Variables
variableatester=IntVar()
nomdufichiertest=StringVar()
listetest=[]
listeentrainement=[]
clf= svm.SVC(kernel='rbf', gamma=0.1, C=0) #### A modifier avec des valeurs cohérentes

######Definitions


def Chargementtest(): #### Permet de retourner le chemin absolue permet l'acces au fichier
	global nomdufichiertest
	global listetest
	nomdufichiertest = tkFileDialog.askopenfilename(initialdir = "/",title = "Selection du fichier test",filetypes = (("Fichier csv","*.csv"),("Fichier texte","*.txt")))
	listetest=load(nomdufichiertest,1)
	
	
def load(filename,typefichier): # load le fichier
	''' Cette fonction permet de charger le fichier dans le script
	Description:
		Ici on convertit le fichier en un tableau que l'on retourne pour le réutiliser,	
		La variable typefichier permet de déterminer s'il est necessaire de faire attention à la première colonne,
		car elle peut contenir pour le fichier entrainement le type de neurone
	Args:
		filename = C'est le nom du fichier qui est demandé en entrée
		typefichier = permet de définir si nous avons un fichier test ou un fichier entrainement
	Return:
		On retourne ici une liste à deux dimension, ce qui est très utile pour la conversion en array numpy
	'''
	dataset=[]
	file = codecs.open(filename, "r",encoding="utf-8")
	for line in file.readlines():
		if not line:
			break
		if line and line[0].isalpha():
			pass
		if typefichier==0:
			y=line.split(',')
			y[0]=int(y[0])
			x=1
			while x<len(y):
				y[x]=float(y[x])
				x=x+1
			dataset.append(y)
		if typefichier==1:
			y=line.split(',')
			x=0
			while x<len(y):
				y[x]=float(y[x])
				x=x+1
			dataset.append(y)
	return dataset

def Chargemententrainement():
	global variableatester
	entrainement=Toplevel()
	entrainement.title("Le fichier d'entraînement")
	entrainement.geometry("800x600+600+300")
	textefichier="Avez-vous un jeu d'essai?"
	fichiers=Label(entrainement,text=textefichier)
	fichiers.pack()
	R1 = Radiobutton(entrainement, text="Oui", variable=variableatester, value=1,command=resultatsappui)
	R1.pack( anchor = W )
	R2 = Radiobutton(entrainement, text="Non", variable=variableatester, value=2, command=resultatsappui)
	R2.pack(anchor = W)


def resultatsappui():
	global listeentrainement
	variable2=variableatester.get()
	if variable2==1:
			nomdufichierentrainement=tkFileDialog.askopenfilename(initialdir = "/",title = "Selection du fichier entrainement",filetypes = (("Fichier csv","*.csv"),("Fichier texte","*.txt")))
			listeentrainement=load(nomdufichierentrainement,0)
	if variable2==2:
			nomdufichierentrainement=()####Chemin de notre fichier test
			listeentrainement=load(nomdufichierentrainement,0)
	entrainementfichier()
	
		
def entrainementdufichier():
	global clf
	y_train=[]
	X_train=[]
	for i in listeentrainement:
		y_train.append(i.pop(0))
	X_train=np.array(listeentrainement)
	if classe==1: ########## S'il a choisi les SVC
		if methode=='rbf':
			clf= svm.SVC(kernel=methode, gamma=x, C=t) ###" changer kernel, et gamma
		if methode=='sigmoid':
			clf= svm.SVC(kernel=methode, gamma=x, C=t) ###" changer kernel, et gamma
		if methode=='poly':
			clf= svm.SVC(kernel=methode, degree=h, C=t) ###" changer kernel, et degree
		if methode=='linear':
			clf= svm.SVC(kernel=methode, C=t) ###" changer kernel, et gamma
	if classe==2: ########## S'il a choisi les NuSVC
		if methode=='rbf':
			clf= svm.NuSVC(kernel=methode, gamma=x, nu=t) ###" changer kernel, et gamma
		if methode=='sigmoid':
			clf= svm.NuSVC(kernel=methode, gamma=x, nu=t) ###" changer kernel, et gamma
		if methode=='poly':
			clf= svm.NuSVC(kernel=methode, degree=h, nu=t) ###" changer kernel, et degree
		if methode=='linear':
			clf= svm.NuSVC(kernel=methode, nu=t) ###" changer kernel, et gamma
	if classe==3: ########## S'il a choisi les LinearSVC
			clf= svm.LinearSVC(C=t) ##### Changer le t 
	clf.fit(X_train,y_train)

def Parametres(): #### A faire suivant les paramètres sortant
	print "Selection et fixation des paramètres"

def presentation():
	presentation=Toplevel()
	presentation.title("Presentation")
	presentation.geometry("800x600+600+300")
	textepresentation="Actuellement etudiant en master I à l'Université de Bordeaux,\n nous avons pour projet de classer des neurones en deux types : Type I et Type II. \n"
	text=Label(presentation,text=textepresentation)
	text.pack()
	presentation.mainloop()

def explicationlogiciel():
	explication=Toplevel()
	explication.title("Le logiciel")
	explication.geometry("1000x500+600+300")
	texteexplication="Présentation du logiciel : \n - Chargement du fichier test : Prend en entrée le fichier test au format .csv et .txt où l'analyse va être réalisé \n - Choisir le fichier d'entrainement : Si le client dispose d'un fichier d'entraînement ayant les types de neurones, il peut le charger sinon un jeu lui sera fourni \n - Paramètres : Concerne le reglage des paramètres à prendre un compte pour l'analyse \n  - Lancer : Permet de lancer l'analyse et d'y afficher les resultats dans une nouvelle fenetre"   ###A mettre en forme
	text=Label(explication, text=texteexplication)
	text.pack()
	explication.mainloop()


def alert():#####Commande bouton du haut
    showinfo("fonctionne")
    

def Lanceranalyse():
	X_test=np.array(listetest)
	result=clf.predict(X_test)
	type1=0
	type2=0
	for i in result:
		if i==1:
			type1=type1+1
		if i==2:
			type2=type2+1
	print "Lancer l'analyse"
	Analyse=Toplevel()
	Analyse.title("Les résultats")
	Analyse.geometry("1200x800+600+300")
	titretext=Label(Analyse, text="LES RESULTATS", fg="Black", bg="Grey")
	titretext.place(x=500, y=0, width=200, height=50)
	name = ['TypeI', 'TypeII'] ##### Nom des parties
	data = [type1, type2] ##### Nombre de type I et nombre de type 2
	explode=(0, 0.2) #### Explosion des deux parties (separation)
	plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True) #####autopct = pourcentage réel par rapport à celui indique, axis = equal permet un diagramme circulaire
	plt.axis('equal')
	plt.show('Test')	
	Analyse=Toplevel()
	Analyse.title("Les résultats")
	Analyse.geometry("1200x800+600+300")
	titretext=Label(Analyse, text="LES RESULTATS", fg="Black", bg="Grey")
	titretext.place(x=500, y=0, width=200, height=50)
	name = ['TypeI', 'TypeII'] ##### Nom des parties
	data = [5000, 6000] ##### Nombre de type I et nombre de type 2
	explode=(0, 0.2) #### Explosion des deux parties (separation)
	plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True) #####autopct = pourcentage réel par rapport à celui indique, axis = equal permet un diagramme circulaire
	plt.axis('equal')
	plt.show('Test')






######## Creation de tous les boutons de chargement
helv36 = tkFont.Font(family='Helvetica', size=10, weight='bold')
text=Label(app, text="Classification Neuronale", fg="RoyalBlue3", bg="SlateGray2", font=helv36)   #####Mettre en gras et en gros (titre)
b1= Button(app, text="Chargement du fichier test",fg="Black", bg="SkyBlue3", command=Chargementtest, font=helv36)
b2= Button(app, text="Choisir le fichier d'entraînement", fg="Black", bg="SkyBlue3", command=Chargemententrainement, font=helv36)
b3= Button(app, text="Paramètres", fg="Black",bg="SkyBlue3", command=Parametres, font=helv36)
b4= Button(app, text="Lancer", fg="Black",bg="SkyBlue3", command=Lanceranalyse, font=helv36)
b5= Button(app, text="Quitter", fg="Black",bg="SkyBlue3", command=app.destroy, font=helv36)
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











