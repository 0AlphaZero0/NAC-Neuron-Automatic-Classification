 # coding: utf-8
 #BLAIS Benjamin
 #COTTAIS Déborah
 #DE OLIVEIRA Lila
 #JOUAN Clement
 #THOUVENIN Arthur

import codecs
import Tkinter  as tk
from Tkinter import *
import tkFileDialog  ##Permet de Charger les fichiers
from matplotlib.figure import * #Importe les parametres de matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #Importe tkinter
import matplotlib.pyplot as plt
import tkFont
from PIL import Image, ImageTk
######################## SI BESOIN
import sys
import os
####################### Import des SVM

from sklearn import datasets
from sklearn import svm
from csv import reader
from matplotlib import style
import numpy as np
import matplotlib.pyplot as plt
import urllib
style.use("ggplot")

#####Main window of the GUI
app = tk.Tk()
fond0=tk.Canvas(app, width=800, height=600, background='SlateGray2')
fond0.pack()
img=tk.PhotoImage(file="miaou2.gif") #https://itsocial.fr/wp-content/uploads/2017/04/iStock-509365378-696x431.png
fond0.create_image(150,350, image=img)
img1=tk.PhotoImage(file="bdx_1.gif")
fond0.create_image(700,550, image=img1)
img2=tk.PhotoImage(file="scikit_learn11.gif")
fond0.create_image(700,450, image=img2)



app.title("Classification neuronale") # Give a title to a window
app.geometry("800x600+600+300") # Place the window
app.configure(background="SlateGray2")# Background color



############# Variables
variableatester=IntVar()
variableparam=IntVar()
variableparametres=IntVar()
t=IntVar()
gamma=IntVar()
classe=IntVar()
nomdufichiertest=StringVar()
methodes=StringVar()
methode=StringVar()
nomfichiersortie=StringVar()
separateur=StringVar()
separateur2=StringVar()
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
	separateurfichier()
	listetest=load(nomdufichiertest,1)

def separateurfichier():
	def resultatsseparateur():
		global separateur
		global separateur2
		separateur2=separateur.get()
		
	global separateur
	load=Toplevel()
	separateur1 = Radiobutton(load, text = "Virgule", variable = separateur, value ='test',command=resultatsseparateur)
	separateur2 = Radiobutton(load, text = "Point-virgule", variable = separateur, value =';', command=resultatsseparateur)
	separateur3 = Radiobutton(load, text = "Tab", variable = separateur, value ='	',command=resultatsseparateur)
	separateur4 = Radiobutton(load, text = "Deux points", variable = separateur, value =':', command=resultatsseparateur)
	separateur5 = Radiobutton(load, text = "Espace", variable = separateur, value =' ', command=resultatsseparateur)
	separateur1.pack();separateur2.pack();separateur3.pack();separateur4.pack();separateur5.pack()


	


def load(filename,typefichier): #### File loading
	'''This function allows to load the file into the script
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
	dataset=[]
	file = codecs.open(filename, "r",encoding="utf-8")
	for line in file.readlines():
		if not line:
			break
		if line and line[0].isalpha():
			pass
		else:
			y=line.split(',')
			if typefichier==0 :
				y[0]=int(y[0])
				x=1
				while x<len(y):
					y[x]=float(y[x])
					x=x+1
				dataset.append(y)
			if typefichier==1:
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
	global separateur2
	variable2=variableatester.get()
	if variable2==1:
		nomdufichierentrainement=tkFileDialog.askopenfilename(initialdir = "/",title = "Selection du fichier entrainement",filetypes = (("Fichier csv","*.csv"),("Fichier texte","*.txt")))
		separateurfichier()
		listeentrainement=load(nomdufichierentrainement,0)
	if variable2==2:
		nomdufichierentrainement=('Fichier_test.csv')####Path of our test file
		separateur2=','
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
	y_train=np.array(y_train)
	X_train=np.array(listeentrainement)
	if classe==1: ########## If SVC were chosen
		if methode=='rbf':
			print "RBF Method"
			clf= svm.SVC(kernel=methode, gamma=gamma, C=t) ###" to change kernel and gamma
		if methode=='sigmoid':
			print "Sigmoid Method"
			clf= svm.SVC(kernel=methode, gamma=gamma, C=t) ###" to change kernel and gamma
		if methode=='poly':
			print "Poly Method"
			clf= svm.SVC(kernel=methode, degree=gamma, C=t) ###" to change kernel and degree
		if methode=='linear':
			print "Linear Method"
			clf= svm.SVC(kernel=methode, C=t) ###" to change kernel and gamma
	if classe==2: ########## S'il a choisi les NuSVC
		if methode=='rbf':
			clf= svm.NuSVC(kernel=methode, gamma=gamma, nu=t) ###" to change kernel and gamma
		if methode=='sigmoid':
			clf= svm.NuSVC(kernel=methode, gamma=gamma, nu=t) ###" to change kernel and gamma
		if methode=='poly':
			clf= svm.NuSVC(kernel=methode, degree=gamma, nu=t) ###" to change kernel and degree
		if methode=='linear':
			clf= svm.NuSVC(kernel=methode, nu=t) ###" to change kernel and gamma
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
	texteexplication="Veuillez choisir la classe de SVM : "
	textexplication=Label(parametres, text=texteexplication)
	P1 = Radiobutton(parametres, text="SVC", variable=variableparam, value=1,command=choixmethode)
	P2 = Radiobutton(parametres, text="NuSVC", variable = variableparam, value=2, command=choixmethode)
	P3 = Radiobutton(parametres, text="LinearSVC", variable=variableparam, value=3, command=choixmethode)
	textexplication.pack();P1.pack();P2.pack();P3.pack()
	parametres.mainloop()

def choixmethode():#### Permet de choisir la méthode de Classification
	'''This function allows the user to choose between different methods in order to personalize, if he wants to, the training method
	Description:
		Here, via a TKinter window, the user will be able to choose between different methods of training methods
	Args:
	Return :
		There is no return here. It modifies the methods variable which corresponds to the method chosen by the user
	'''
	global methodes
	global classe
	classe=variableparam.get()
	if classe==1 or classe==2:
		classe1=Toplevel()
		choixmethodes="Veuillez choisir la méthode de votre choix : "
		choixmethode=Label(classe1, text=choixmethodes)
		R1=Radiobutton(classe1, text='rbf', variable=methodes,value="rbf",command=choixhyperparametres)
		R2=Radiobutton(classe1, text='sigmoid',variable=methodes,value="sigmoid",command=choixhyperparametres)
		R3=Radiobutton(classe1, text='poly', variable=methodes, value="poly",command=choixhyperparametres)
		R4=Radiobutton(classe1, text='linear', variable=methodes, value="linear",command=choixhyperparametres)
		choixmethode.pack();R1.pack();R2.pack();R3.pack();R4.pack()
	if classe==3:
		choixhyperparametres()

def choixhyperparametres():#### Permet de choisir les hyperparameters de la méthode
	'''Dans cette fonction on propose à l'utilisateur de régler les hyperparameters de la méthode choisie précèdement
	Description :
		Ici en fonction de la méthode choisie l'utilisateur peut choisir les différents hyperparameters selon son choix.
	Args:
		No Args required.
	Return:
		There is no return here. Seul les variables des hyperparameters vont être modifiés.
	'''
	def validerhyperparam():
		global t
		global gamma
		t=float(ttest.get())
		gamma=float(gammatest.get())
		hyperparametres.destroy

	global methode
	methode=methodes.get()
	classe=variableparam.get()
	hyperparametres=Toplevel()
	textehyperparametres = "Veuillez regler les hyperparamètres :"
	textehyperparametres2=Label(hyperparametres,text=textehyperparametres)
	validerchoix= Button(hyperparametres, text="Valider", fg="Black",bg="SkyBlue3", command=validerhyperparam, font=helv36)
	textehyperparametres2.pack()
	if (methode=='rbf' or methode=='sigmoid') and classe==1:
		gammatest=Scale(hyperparametres, orient='horizontal', from_=0, to=1000,resolution=0.1, tickinterval=10, length=350,label='Choix de la valeur gamma')
		ttest=Scale(hyperparametres, orient='horizontal', from_=0, to=1000, resolution=0.1, tickinterval=10, length=350, label='Choix de la valeur de C')
		gammatest.pack();ttest.pack();
	if methode=='poly' and classe==1:
		gammatest=Scale(hyperparametres, orient='horizontal', from_=0, to=1000,resolution=0.1, tickinterval=10, length=350,label='Choix de la valeur de degree')
		ttest=Scale(hyperparametres, orient='horizontal', from_=0, to=1000,resolution=0.1, tickinterval=10, length=350,label='Choix de la valeur de C')
		gammatest.pack();ttest.pack();
	if methode=='linear' and (classe==1 or classe==3):
		ttest=Scale(hyperparametres, orient='horizontal', from_=0, to=1000, resolution=0.1, tickinterval=10, length=350, label='Choix de la valeur de C')
		ttest.pack();
	if (methode=='rbf' or methode=='sigmoid') and classe==2:
		gammatest=Scale(hyperparametres, orient='horizontal', from_=0, to=1000, resolution=0.1, tickinterval=10, length=350, label='Choix de la valeur de gamma')
		ttest=Scale(hyperparametres, orient='horizontal', from_=0, to=1000, resolution=0.1, tickinterval=10, length=350, label='Choix de la valeur de nu')
		gammatest.pack();ttest.pack();
	if methode=='poly' and classe==2:
		gammatest=Scale(hyperparametres, orient='horizontal', from_=0, to=1000, resolution=0.1, tickinterval=10, length=350, label='Choix de la valeur de degree')
		ttest=Scale(hyperparametres, orient='horizontal', from_=0, to=1000, resolution=0.1, tickinterval=10, length=350, label='Choix de la valeur de nu')
		gammatest.pack();ttest.pack();
	if methode=='linear' and classe==2:
		ttest=Scale(hyperparametres, orient='horizontal', from_=0, to=1000, resolution=0.1, tickinterval=10, length=350, label='Choix de la valeur de nu')
		ttest.pack();
	if classe==3:
		ttest=Scale(hyperparametres, orient='horizontal', from_=0, to=1000, resolution=0.1, tickinterval=10, length=350, label='Choix de la valeur de C')
		ttest.pack()
	validerchoix.pack()

def ChoixNomFichier():  #####Choix du nom du fichier de sortie
	def recuperationnomfichier(event):
		nomdufichier= entrernomfichier.get()
	global nomfichiersortie
	choixnomfichier = Toplevel()
	textechoixfichier = "Veuillez choisir le nom du fichier de sortie : \n"
	textechoixfichier = Label(choixnomfichier, text=textechoixfichier)
	validernomfichier= Button(choixnomfichier, text="Fermer", command=choixnomfichier.destroy)
	entrernomfichier = Entry(choixnomfichier, width=30, textvariable=nomfichiersortie)
	entrernomfichier.bind("<Return>",recuperationnomfichier)
	textechoixfichier.pack();entrernomfichier.pack();validernomfichier.pack()

def Lanceranalyse():
	X_test=np.array(listetest)
	result=clf.predict(X_test)
	Tk().bell()
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
	namepart = ['TypeI', 'TypeII'] ##### Nom des parties
	data = [type1, type2] ##### Nombre de type I et nombre de type 2
	explode=(0, 0.2) #### Explosion des deux parties (separation)
	plt.pie(data, explode=explode, labels=namepart, autopct='%1.1f%%', startangle=90, shadow=True) #####autopct = pourcentage réel par rapport à celui indique, axis = equal permet un diagramme circulaire
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

def presentation(): #### Presentation de notre groupe
	presentation=Toplevel()
	presentation.title("Presentation")
	presentation.geometry("800x600+600+300")
	textepresentation="Actuellement etudiant en master I à l'Université de Bordeaux,\n nous avons pour projet de classer des neurones en deux types : Type I et Type II. \n"
	text=Label(presentation,text=textepresentation)
	text.pack()
	presentation.mainloop()

def explicationlogiciel(): ###### Tuto explication du logiciel
	explication=Toplevel()
	explication.title("Le logiciel")
	explication.geometry("1000x500+600+300")
	texteexplication="Présentation du logiciel : \n - Chargement du fichier test : Prend en entrée le fichier test au format .csv et .txt où l'analyse va être réalisé \n - Choisir le fichier d'entrainement : Si le client dispose d'un fichier d'entraînement ayant les types de neurones, il peut le charger sinon un jeu lui sera fourni \n - Paramètres : Concerne le reglage des paramètres à prendre un compte pour l'analyse \n  - Lancer : Permet de lancer l'analyse et d'y afficher les resultats dans une nouvelle fenetre"   ###A mettre en forme
	text=Label(explication, text=texteexplication)
	text.pack()
	explication.mainloop()

################################################################################ MAIN ##########################################################

####### Police pour le titre
pourtitre = tkFont.Font(family='Helvetica', size=25, weight='bold')
helv36 = tkFont.Font(family='Helvetica', size=10, weight='bold')

######## Creation de tous les boutons de chargement
text=Label(app, text="Classification Neuronale", fg="RoyalBlue3", bg="SlateGray2", font=pourtitre)
b1= Button(app, text="Ajustement des paramètres", fg="Black",bg="SkyBlue3", command=ChoixClasseparam, font=helv36, bd=4)
b2= Button(app, text="Chargement du fichier d'entraînement", fg="Black", bg="SkyBlue3", command=Chargemententrainement, font=helv36, bd=4)
b3= Button(app, text="Chargement du fichier à analyser",fg="Black", bg="SkyBlue3", command=Chargementtest, font=helv36, bd=4)
b4= Button(app, text="Choisir le nom du fichier de sortie", fg="Black", bg="SkyBlue3", command=ChoixNomFichier, font=helv36, bd=4)
b5= Button(app, text="Lancer l'analyse", fg="Black",bg="SkyBlue3", command=Lanceranalyse, font=helv36, bd=4)
b6= Button(app, text="Quitter l'application", fg="Black",bg="SkyBlue3", command=app.destroy, font=helv36, bd=4, bitmap="error")
b1.place(x=300, y=100, width=250, height=40)
b2.place(x=300, y=170, width=250, height=40)
b3.place(x=300, y=240, width=250, height=40)
b4.place(x=300, y=310, width=250, height=40)
b5.place(x=350, y=470, width=150, height=60)
b6.place(x=350, y=540, width=150, height=30)
text.place(x=180, y=0, width=500, height=50)

###### Barre de menu
menubar = Menu(app)
menu1 = Menu(menubar, tearoff=0)
menu1.add_separator()
menu1.add_command(label="Ouvrir un fichier test", command=Chargementtest)
menu1.add_separator()
menu1.add_command(label="Ouvrir un fichier d'entrainement", command=Chargemententrainement)
menu1.add_separator()
menu1.add_command(label="Enregistrer le projet en cours", command=Chargemententrainement)#####Save the project
menu1.add_separator()
menubar.add_cascade(label="Fichier", menu=menu1) ######Nom sur la barre de menu

menu2 = Menu(menubar, tearoff=0)
menu2.add_separator()
menu2.add_command(label="Regler les paramètres", command=ChoixClasseparam)
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
