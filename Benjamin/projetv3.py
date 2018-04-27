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

#####Main window of the GUI
app = Tk()
app.title("Classification neuronale") # Give a title to a window
app.geometry("800x600+600+300") # Place the window
app.configure(background='SlateGray2')# Background color



############# Variables
variableatester=IntVar()
variableparam=IntVar()
variableparametres=IntVar()
nomdufichiertest=StringVar()
methodes=StringVar()
methode=StringVar()
listetest=[]
listeentrainement=[]
clf= svm.SVC(kernel='rbf', gamma=0.1, C=0) #### To modify with consistent values

######Definitions
def Chargementtest(): #### Gives the absolute path of the file
    '''This function retrieves the path to the Test file
    Description:
        Here, the user is asked to, via the Tkinter GUI, to choose the Test file of his choice. The path to this file will then be retrieved.
    Args:
        No Args required
    Return:
        No return, here, global variables are modified.
    '''

    global nomdufichiertest
    global listetest
    nomdufichiertest = tkFileDialog.askopenfilename(initialdir = "/",title = "Selection du fichier test",filetypes = (("Fichier csv","*.csv"),("Fichier texte","*.txt")))
    listetest=load(nomdufichiertest,1)

def load(filename,typefichier): #### File loading
	'''
    This function allows to load the file into the script
	Description:
        Here, the file is converted into an array which will be returned for reuse
        The typefichier variable is used to determined whether it is necessary to take into account the first column
		because it can contain (for the training file) the type of neuron
	Args:
		filename = it is the name of the file that is requested as an input
		typefichier = allows to define if it is a Test file or a Training file
	Return:
        Here, a two dimensional list is returned, which is useful for converting into an numpy array
	'''
	firstline=1
	dataset=[]
	file = codecs.open(filename, "r",encoding="utf-8")
	for line in file.readlines():
		if not line:
			break
		if line and line[0].isalpha():
			pass
		if typefichier==0:
			if firstline==1:
				firstline=0
				pass
			else:
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

def Chargemententrainement():#### Loading of the training file
    '''This function allows the user to choose a training file from his own data or a default file given by us
    Description:
        Here, a window is created to allow the user to choose whether he wants to use his own data or the default one (thanks to yes/no buttons)
    Args:
        No Args required.
    Return:
        There is no return, only the variable to be tested is modified as a global variable
    '''
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

def resultatsappui():#### Choice of the training file
    '''This function allows, via a small TKinter window, to choose among the user's folders the desired file
    Description :
        Here, a TKinter window is opened allowing the user to choose his file and allowing the program to recover the absolute path
        which will be used for the training of the statistical model thanks to the function entrainementdufichier()
    Args :
        No Args required
    Return :
        There is no return, only the listeentrainement variable is modified, which allows to train the statistic model thanks to the entrainementdufichier() function
    '''
    global listeentrainement
    variable2=variableatester.get()
    if variable2==1:
        nomdufichierentrainement=tkFileDialog.askopenfilename(initialdir = "/",title = "Selection du fichier entrainement",filetypes = (("Fichier csv","*.csv"),("Fichier texte","*.txt")))
        listeentrainement=load(nomdufichierentrainement,0)
    if variable2==2:
        nomdufichierentrainement=('All_ech.csv')####Path of our test file
        listeentrainement=load(nomdufichierentrainement,0)
    entrainementdufichier()

def entrainementdufichier():#### Training of the statistical model
    '''Here, in function of the class and the model as well as hyperparameters of the method, the training table will allow to train the statistical model
    Description :
        Here, thanks to multiple conditions, it is possible to choose the class and the method wished by the user to train the model
    Args :
        No Args required.
    Return :
        There is no return here, only the variable clf is modified, it is the one which contains the training method, it will be modified according to the choice of the user
   '''
    global clf
    y_train=[]
    X_train=[]
    for i in listeentrainement:
        y_train.append(i.pop(0))
    X_train=np.array(listeentrainement)
    if classe==1: ########## If SVC were chosen
        if methode=='rbf':
            clf= svm.SVC(kernel=methode, gamma=gamma, C=C) ###" to change kernel and gamma
        if methode=='sigmoid':
            clf= svm.SVC(kernel=methode, gamma=gamma, C=C) ###" to change kernel and gamma
        if methode=='poly':
            clf= svm.SVC(kernel=methode, degree=degree, C=C) ###" to change kernel and degree
        if methode=='linear':
            clf= svm.SVC(kernel=methode, C=C) ###" to change kernel and gamma
    if classe==2: ########## S'il a choisi les NuSVC
        if methode=='rbf':
            clf= svm.NuSVC(kernel=methode, gamma=gamma, nu=nu) ###" to change kernel and gamma
        if methode=='sigmoid':
            clf= svm.NuSVC(kernel=methode, gamma=gamma, nu=nu) ###" to change kernel and gamma
        if methode=='poly':
            clf= svm.NuSVC(kernel=methode, degree=degree, nu=nu) ###" to change kernel and degree
        if methode=='linear':
            clf= svm.NuSVC(kernel=methode, nu=nu) ###" to change kernel and gamma
    if classe==3: ########## If LinearSVC were chosen
            clf= svm.LinearSVC(C=t) ##### To change the t
    clf.fit(X_train,y_train)

def ChoixClasseparam(): #### Allows to set classes
    '''This function allows the user to choose between the different classes in order to personalize, if he wants to, the training method
    Description:
        Here, thanks to a TKinter window, the user will be able to choose between different classes of training methods
    Args:
        No Args required.
    Return :
        There is no return here. It modifies the variableparam variable to adjust the training method class
    '''
    global variableparam
    parametres=Toplevel()
    P1 = Radiobutton(parametres, text="SVC", variable=variableparam, value=1,command=choixmethode)
    P2 = Radiobutton(parametres, text="NuSVC", variable = variableparam, value=2, command=choixmethode)
    P3 = Radiobutton(parametres, text="LinearSVC", variable=variableparam, value=3, command=choixmethode)
    P1.pack();P2.pack();P3.pack()

def choixmethode():#### Permet de choisir la méthode de Classification
    '''This function allows the user to choose between different methods in order to personalize, if he wants to, the training method
    Description:
        Here, via a TKinter window, the user will be able to choose between different methods of training methods
    Args:
    Return :
        There is no return here. It modifies the methods variable which corresponds to the method chosen by the user
    '''
    global methodes
    classe=variableparam.get()
    if classe==1 or classe==2:
        classe1=Toplevel()
        R1=Radiobutton(classe1, text='rbf', variable=methodes,value="rbf",command=choixhyperparametres)
        R2=Radiobutton(classe1, text='sigmoid',variable=methodes,value="sigmoid",command=choixhyperparametres)
        R3=Radiobutton(classe1, text='poly', variable=methodes, value="poly",command=choixhyperparametres)
        R4=Radiobutton(classe1, text='linear', variable=methodes, value="linear",command=choixhyperparametres)
        R1.pack();R2.pack();R3.pack();R4.pack
    if classe==3:
        methodes='linear'
def choixhyperparametres():#### Permet de choisir les hyperparameters de la méthode
    '''Dans cette fonction on propose à l'utilisateur de régler les hyperparameters de la méthode choisie précèdement
    Description :
        Ici en fonction de la méthode choisie l'utilisateur peut choisir les différents hyperparameters selon son choix.
    Args:
        No Args required.
    Return:
        There is no return here. Seul les variables des hyperparameters vont être modifiés.
    '''
    global methode
    methode=methodes.get()
    print methode
    if methode=='rbf' or methode=='sigmoid':
        hyperparametres1=Toplevel()
        gamma=Scale(hyperparametres1, orient='horizontal', from_=0, to=1000,resolution=0.1, tickinterval=10, length=350,label='Choix de la valeur gamma')
        C=Scale(hyperparametres1, orient='horizontal', from_=0, to=1000, resolution=0.1, tickinterval=10, length=350, label='Choix de la valeur de C')
        gamma.pack();C.pack()
    if methode=='poly':
        hyperparametres2=Toplevel()
        degree=Scale(hyperparametres2, orient='horizontal', from_=0, to=1000,resolution=0.1, tickinterval=10, length=350,label='Choix de la valeur degree')
        nu=Scale(hyperparametres2, orient='horizontal', from_=0, to=1000,resolution=0.1, tickinterval=10, length=350,label='Choix de la valeur nu ou C')
    if methode=='linear':
        hyperparametres3=Toplevel()
        Scale(hyperparametres3, orient='horizontal', from_=0, to=1000, resolution=0.1, tickinterval=10, length=350, label='Choix de la valeur de C')
def showIt(event):
    gamaa=gamma.widget.get()
    print gammaa

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
	data = [type1, type2] ##### Nombre de type I et nombre de type 2
	explode=(0, 0.2) #### Explosion des deux parties (separation)
	plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True) #####autopct = pourcentage réel par rapport à celui indique, axis = equal permet un diagramme circulaire
	plt.axis('equal')
	plt.show('Test')






######## Creation de tous les boutons de chargement
helv36 = tkFont.Font(family='Helvetica', size=10, weight='bold')
text=Label(app, text="Classification Neuronale", fg="RoyalBlue3", bg="SlateGray2", font=helv36)   #####Mettre en gras et en gros (titre)
b1= Button(app, text="Chargement du fichier test",fg="Black", bg="SkyBlue3", command=Chargementtest, font=helv36)
b2= Button(app, text="Paramètres", fg="Black",bg="SkyBlue3", command=ChoixClasseparam, font=helv36)
b3= Button(app, text="Choisir le fichier d'entraînement", fg="Black", bg="SkyBlue3", command=Chargemententrainement, font=helv36)
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