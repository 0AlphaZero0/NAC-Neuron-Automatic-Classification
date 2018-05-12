#!usr/bin/python
# coding: utf-8
#
#
#       Neural Classification programm
#
#     11/05/2018
######################        CONTACT
#   BLAIS Benjamin   #	ben.blais@laposte.net
#   COTTAIS Déborah  #  d.cottais1@gmail.com
#  DE OLIVEIRA Lila  #  lila.de-oliveira@etu.u-bordeaux.fr
#   JOUAN Clement    #  jouan.clement@hotmail.fr
#  THOUVENIN Arthur  #  athouvenin@outlook.fr
######################

'''
											Neural Classification Programm
	
	Ce programmme permet à un utilisateur de classer des neurones via des fichiers prédéfinis, en utilisant des méthodes de 
classification basée sur le Machine learning. Ici la librairie utilisée pour accéder à ces méthodes d'apprentrissage est la 
librairie scikit-learn.   Cette librairie très suivie par la communauté est adpaté pour répondre aux attentes d'un tel pro-
gramme.  Le logiciel utilise également des librairies telles que matplotlib et Tkinter afin de rendre un aperçu plus visuel
des résultats d'une classification.
	Ainsi l'utilisateur pourra choisir selon ses connaissances sur les méthodes de classifications, la méthode, les 
paramètres et hyperparamètres nécessaire à une classification.  Si ce n'est pas son choix, une méthode par défaut est dispo-
nible.  En effet suite à une étude et une exploration approfondie de ces méthodes et paramètres, nous en sommes venus à con-
clure que la classe SVC,
		  la méthode rbf,
		  un C = 1E-7,
		  un gamma = 1E7,
		  et la combinaison de paramètres : RMP RH SA SD fAHP,
sont les paramètres les plus adaptés dans la plupart des cas, en revanche nous conseillons de ne pas utilisé des donnée pro-
venant de diverses expérimentations, en effet il semble que les conditions d'expérimentations ou de prélèvements des données
influencent grandement l'entrainement d'un modèle de classification.
Nous définissons ici deux types de fichiers :
		le fichier test = fichier sur lequel se déroulera la classification
		le fichier d'entrainement = fichier qui va permettre la création du modèle de classification. 
'''

import codecs # Allows to load a file containing UTF-8 characters
import matplotlib.pyplot as plt # Allows to create graphics, especially those in 3D
import matplotlib as mpl # Allow to use matplotlib to make graphs
import numpy as np # Allows to manipulate the necessary table for sklearn
import os # Allows to modify some things on the os
import random # Allows to use random variables
import shutil #permet la copie de fichier
import sys # Allow to modify files on the OS
import tkFont # Allows to modify the TKinter display font
import Tkinter as tk # Allows the TKinter database with the abreviation tk
import tkFileDialog  # Allows to create a windows to load files
import webbrowser
from matplotlib 						 import style # Allows to modify the graphics' appearance
from matplotlib.backends.backend_tkagg	 import FigureCanvasTkAgg # Allw some option in matlpotlib to make 3D graphs
from matplotlib.figure					 import * # Allows the modification of the matplotlib graphics' appearances
from mpl_toolkits.mplot3d				 import Axes3D
from sklearn 							 import svm # Allows to use the SVM classification method
from sklearn.neural_network				 import MLPClassifier # Allows the use of the neural network method from sklearn
from Tkinter							 import * # Allows the use of the TKinter GUI
#################################    Main window of the GUI    ###################################################
app = tk.Tk()
app.title("Classification neuronale") # Give a title to the window
app.geometry("800x600+600+300") # Anchor the window
app.resizable(False,False)
app.configure(background="SlateGray2")# Background color
fond0=tk.Canvas(app, width=800, height=600, background='SlateGray2')
fond0.pack()
img=tk.PhotoImage(file="miaou2.gif") #https://itsocial.fr/wp-content/uploads/2017/04/iStock-509365378-696x431.png
fond0.create_image(150,350, image=img)
img1=tk.PhotoImage(file="bdx_1.gif")
fond0.create_image(700,550, image=img1)
img2=tk.PhotoImage(file="scikit_learn11.gif")
fond0.create_image(700,450, image=img2)

#######################################################    VARIBALES    #######################################################
beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
classes=1
sampling=IntVar()
samples=IntVar()
alpha=IntVar()
gammatest=IntVar()
choice=IntVar()
tol=IntVar()
ttest=IntVar()
testvariable=IntVar()
paramvariable=IntVar()
variableparametres=IntVar()
methods=StringVar()
trainlist=[]
testlist=[]
resultdataset=[]
listclass=["SVC","NuSVC","LinearSVC","Réseau de neurones"]
completeparamlist=["nClass","IR","RMP","RH","ST","DTFS","SA","SD","fAHP"]
paramlist=[2,3,5,6,7]
gamma=10000000
t=0.0000001
userdataset=0
theoutputfilename=''
separator=','
method='rbf'
methods.set('rbf') #### Indique que la method par défaut est rbf
paramvariable.set(1) ###### Par default paramvariable = NuSVC
clf= svm.SVC(kernel='rbf', gamma=10000000, C=0.0000001) #### To modify with consistent values


menubar = Menu(app)

helv36 = tkFont.Font(family='Helvetica', size=10, weight='bold')
fortitle = tkFont.Font(family='Helvetica', size=25, weight='bold')
text=Label(app, text="Classification Neuronale", fg="RoyalBlue3", bg="SlateGray2", font=fortitle)
#######################################################    FUNCTIONS    #######################################################

def loadtest(check): #### Oriente avec gestion d'erreur vers la fonction de chargement						####CLEAN ### A TRADUIRE
	'''Cette fonction permet d'implémeonter une gestion d'erreur lors du chargement du fichier 
	Description:
		Ici si cette fonction est appelée depuis un avertissement elle détruira la fenêtre d'avertissement 
		et exécutera la fonction separatorfile pour un fichier test
	Args:
		Check = permet de vérifier si l'appel de la fonction vient de la fonction avertissement
	Return:
		No return, here, global variables are modified.
	'''
	if check=="avertissement":
		Winwarnings.destroy()
	separatorfile(2)

def separatorfile(verif): #### Give the file separator                                               	 	####CLEAN ### A TRADUIRE
	''' This function allows to give the file separator
	Description:
		Here, the user can choose the separator of his file. There are five possibilities.
	Args:
		No Args required
	Return:
		No return. Here, global variable Winsep is modified, to destroy the window in the next function.
	'''
	def sepresults(tmp): ### Récupération du séparateur sous la forme d'une string
		''' Cette fonction permet de récupérer sous la forme d'une string le séparateur rentré par l'utilisateur
		Description:
			Ici la variable separateur doit être retrournée sous la forme d'une string, on récupère donc la variable separateur 
			qui est sous la forme PYVARx
		Args:
			tmp = valeur sous la forme PYVARx
		Return:
			No return. Here, global variable separateur is modified to get it in other functions
 		'''
		global separator
		separator=tmp.get()
		print separator
	global Winsep
	Winsep=Toplevel()
	Winsep.geometry("150x135+950+500")
	Winsep.title('Séparateur du fichier')
	Winsep.resizable(False,False)
	tmp=StringVar()
	tmp.set(',')
	s1=Radiobutton(Winsep, text = "Virgule", variable = tmp, value =',',command= lambda : sepresults(tmp))
	s2=Radiobutton(Winsep, text = "Point-virgule", variable = tmp, value =';', command=lambda : sepresults(tmp))
	s3=Radiobutton(Winsep, text = "Tab", variable = tmp, value ='	',command=lambda : sepresults(tmp))
	s4=Radiobutton(Winsep, text = "Deux points", variable = tmp, value =':', command=lambda :sepresults(tmp))
	s5=Radiobutton(Winsep, text = "Espace", variable = tmp, value =' ', command=lambda : sepresults(tmp))
	s9=Button(Winsep, text="Valider", command=lambda c=verif:finalload(c))
	s1.pack();s2.pack();s3.pack();s4.pack();s5.pack();s9.pack()
	Winsep.mainloop()

def finalload(verif): #### Chargement du fichier d'entrainement / fichier test            					####CLEAN ### A TRADUIRE
	'''Cette fonction en fonction de son appel va charger le fichier test ou entrainement dans nos liste à 2D
	Description:
		Ici le fichier test ou entraînement sera chargé en fonction de l'appel de cette fonction
	Args:
		verif = permet de verifier si la fonction doit s'exécuter pour le test(0) ou l'entrainement(1)
	Return:
		No return. Ici les listes trainlist et testlist vont être remplie par le chargement des fichiers et le userdataset
		permet de récupérer ailleurs l'information selon laquelle l'utilisateur a rentré son fichier d'entraînement
	'''
	global trainlist
	global testlist
	global userdataset
	Winsep.destroy()
	if verif==1:
		userdataset=1
		trainingfilename=tkFileDialog.askopenfilename(initialdir = "/net/cremi",title = "Selection du fichier entrainement",filetypes = (("Fichier csv","*.csv"),("Fichier texte","*.txt")))
		shutil.copyfile(trainingfilename,'TrainModel.csv')
		shutil.copyfile(trainingfilename,'Yourbackup.csv')
		trainlist=load(trainingfilename,0)
	else:
		userdataset=0
		testfilename=tkFileDialog.askopenfilename(initialdir = "/net/cremi",title = "Selection du fichier test",filetypes = (("Fichier csv","*.csv"),("Fichier texte","*.txt")))
		testlist=load(testfilename,1)

def load(filename,typeofile): #### File loading                                                           ####CLEAN ### A TRADUIRE
	'''This function allows to load the file into the script
	Description:
		Here, the file is converted into an array which will be returned for reuse
		The typeofile variable is used to determined whether it is necessary to take into account the first column
		because it can contain (for the training file) the type of neuron
	Args:
		filename = it is the name of the file that is requested as an input
		typeofile = allows to define if it is a Test file or a Training file
	Return:
		Here, a two dimensional list is returned, which is useful for converting into an numpy array
	'''
	result=file(filename,"r").read().replace(separator, ",")
	file("tmp.csv","w").write(result)
	# revoir
	dataset=[]
	files=codecs.open("tmp.csv", "r",encoding="utf-8")
	for line in files.readlines():
		if not line:
			break
		if line and line[0].isalpha():
			pass
		else:
			y=line.split(',')
			if typeofile==0 : # trainning file
				if len(y)>9 or len(y)<9:
					printxt="Attention fichier d'entraînement incorrect"
					labeltxt="Attention le fichier d'entraînement soumis, ne correspond pas à l'entrée nécessaire. \n Veuillez chargez un fichier d'entrainement pour l'analyse."
					buttontxt="Chargement d'un fichier d'entraînement"
					Warnings(printxt,labeltxt,buttontxt,loadtrain)
					return
				y[0]=int(y[0])
				x=1
				while x<len(y):
					y[x]=float(y[x])
					x=x+1
				dataset.append(y)
			if typeofile==1: # test file
				x=0
				if len(y)>8 or len(y)<8:
					printxt="Attention fichier de test incorrect"
					labeltxt="Attention le fichier test soumis, ne correspond à l'entrée nécessaire. \n Veuillez chargez un fichier pour l'analyse."
					buttontxt="Chargement d'un fichier d'un fichier test"
					Warnings(printxt,labeltxt,buttontxt,loadtest)
					return
				while x<len(y):
					y[x]=float(y[x])
					x=x+1
				dataset.append(y)
	file.close
	os.remove("tmp.csv")
	return dataset

def loadtrain(check):#### Loading of the training file														####CLEAN ### A TRADUIRE
	'''This function allows the user to choose a training file from his own data or a default file given by us
	Description:
		Here, a window is created to allow the user to choose whether he wants to use his own data or the default one (thanks to yes/no buttons)
	Args:
		check = permet de savoir si la fenêtre vient d'un avertissement et ainsi détruire lafenêtre avertissement
	Return:
		There is no return, ici seules testvariable et Winent sont modifiées comme variables globales,
		pour la première c'est la variable qui va conserver le choix de l'utilisateur,
		la seconde est la fenêtre créée ici qui pourra ainsi être détruite dans la fonction suivante
	'''
	global testvariable
	global Winent
	if check=="avertissement":
		Winwarnings.destroy()
	Winent=Toplevel()
	Winent.title("Choix du fichier d'entraînement")
	Winent.geometry("200x60+925+500")
	Winent.resizable(False,False)
	filetext="Avez-vous un jeu d'essai?"
	filetext2=Label(Winent,text=filetext)
	filetext2.pack()
	R1 = Radiobutton(Winent, text="Oui", variable=testvariable, value=1,command=lambda c='trainning':choicetrain(c))
	R1.pack()
	R2 = Radiobutton(Winent, text="Non", variable=testvariable, value=2, command=lambda c='trainning':choicetrain(c))
	R2.pack()

def choicetrain(check):#### Choice of the training file													####CLEAN ### A TRADUIRE
	'''This function allows, via a small TKinter window, to choose among the user's folders the desired file
	Description :
		Here, a TKinter window is opened allowing the user to choose his file and allowing the program to recover the absolute path
		which will be used for the training of the statistical model thanks to the function trainingfile()
	Args :
		check = permet de savoir si la fenêtre vient d'un avertissement et ainsi détruire lafenêtre avertissement
	Return :
		There is no return, only the trainlist variable is modified and separateur,
		 which allows to train the statistic model thanks to the trainingfile() function
	'''
	global separator
	global trainlist
	if check=="trainning":
		Winent.destroy()
	variable2=testvariable.get()
	if variable2==1:
		separatorfile(1)
	if variable2==2:
		separator=','
		trainlist=load('Backup_G.csv',0)

def trainingfile(verif):#### Training of the statistical model										####CLEAN ### A TRADUIRE
	'''Here, in function of the class and the model as well as hyperparameters of the method,
	 the training table will allow to train the statistical model
	Description :
		Here, thanks to multiple conditions, it is possible to choose the class and the method wished by the user to train the model
	Args :
		verif = permet de savoir si la fonction a été appelée pour la classification ou la simulation
	Return :
		X_test = list a deux dimensions contenant les deux sur lesquelles réaliser la simulation
		y_test = list des classes des neurones
		The variable clf is modified, it is the one which contains the training method,
		 it will be modified according to the choice of the user
	'''
	global clf
	# Variables
	dataset=[]
	y_train=[]
	X_train=[]
	#Choix des combinaisons de paramètres
	for sample in trainlist:
		s=[]
		s.append(sample[0])
		for i in paramlist:
			s.append(sample[i+1])
		dataset.append(s)
	######## Classification
	if verif==0:
		print "=== Classification ==="
		for i in dataset:
			y_train.append(i.pop(0))
		y_train=np.array(y_train)
		X_train=np.array(dataset)
		print "Size of trainning dataset : ",len(X_train)
	######## Simulation
	if verif==1:
		print "=== Simulation ===="
		train=[]
		test=[]
		y_test=[]
		X_test=[]
		g=0
		datalength=len(dataset)
		# Echantillonnage
		while g!=len(dataset):
			top=len(dataset)-1
			rand=random.randint(0,top)
			if sampling==1:
				div=2
			if sampling==2 or sampling==3:
				div=4
			limit=datalength/div
			if limit<len(dataset):
				if sampling==2 or sampling==1:
					test.append(dataset.pop(rand)) #75% of sample in test
				if sampling==3:
					train.append(dataset.pop(rand)) #75% of sample in train
			else:
				if sampling==2 or sampling==1:
					train.append(dataset.pop(rand)) #75% of sample in train
				if sampling==3:
					test.append(dataset.pop(rand)) #75% of sample in test
		print "Size of trainning dataset = ",len(train)
		print "Size of test list = ",len(test)
		# Séparation de la liste y d'entrainement
		for sample in train:
			y_train.append(sample.pop(0))
		# Séparation de la liste y pour le test
		for sample in test:
			y_test.append(sample.pop(0))
		X_test=np.array(test)
		X_train=np.array(train)
	if classes==1: ########## If SVC were chosen
		if method=='rbf':
			print "RBF Method"
			clf= svm.SVC(kernel=method, gamma=gamma, C=t) ###" to change kernel and gamma
		if method=='sigmoid':
			print "Sigmoid Method"
			clf= svm.SVC(kernel=method, gamma=gamma, C=t) ###" to change kernel and gamma
		if method=='poly':
			print "Poly Method"
			clf= svm.SVC(kernel=method, degree=degre, C=t) ###" to change kernel and degree
		if method=='linear':
			print "Linear Method"
			clf= svm.SVC(kernel=method, C=t) ###" to change kernel and gamma
	if classes==2: ########## If NuSVC were chosen
		if method=='rbf':
			clf= svm.NuSVC(kernel=method, gamma=gamma, nu=Nu) ###" to change kernel and gamma
		if method=='sigmoid':
			clf= svm.NuSVC(kernel=method, gamma=gamma, nu=Nu) ###" to change kernel and gamma
		if method=='poly':
			clf= svm.NuSVC(kernel=method, degree=degre, nu=Nu) ###" to change kernel and degree
		if method=='linear':
			clf= svm.NuSVC(kernel=method, nu=Nu) ###" to change kernel and gamma
	if classes==3: ########## If LinearSVC were chosen
			clf= svm.LinearSVC(C=t) ##### To change the t
	if classes==4: ####RN Classifier
		print "clf classifier"
		clf = MLPClassifier(solver='lbfgs', activation=method, alpha=alpha, hidden_layer_sizes=(4,), tol=tol)
	clf.fit(X_train,y_train)
	if verif==1:
		return X_test,y_test

def choiceparamclass(): #### Allows to set classes															####CLEAN ### A TRADUIRE
	'''This function allows the user to choose between the different classes in order to personalize, if he wants to, the training method
	Description:
		Here, thanks to a TKinter window, the user will be able to choose between different classes of training methods
	Args:
		No Args required.
	Return :
		There is no return here. It modifies the paramvariable variable to adjust the training method class
		And Winclasse which is the window that can be detroy in he next function
	'''
	global paramvariable
	global Winclasse
	Winclasse=Toplevel()
	Winclasse.title('Choix de la classe')
	Winclasse.geometry('400x150+820+500')
	Winclasse.resizable(False,False)
	explanationtext="Veuillez choisir la classe de SVM (SVC,NuSVC,LinearSVC) \n ou de Réseaux de Neurones (Classifier) : "
	explanationtext=Label(Winclasse, text=explanationtext)
	P1 = Radiobutton(Winclasse, text="SVC", variable=paramvariable, value=1,command=methodchoice)
	P2 = Radiobutton(Winclasse, text="NuSVC", variable = paramvariable, value=2, command=methodchoice)
	P3 = Radiobutton(Winclasse, text="LinearSVC", variable=paramvariable, value=3, command=methodchoice)
	P4 = Radiobutton(Winclasse, text="Classifier", variable=paramvariable, value=4, command=methodchoice)
	P5 = Button(Winclasse, text="Par défaut", command=bydefault)
	explanationtext.pack();P1.pack();P2.pack();P3.pack();P4.pack();P5.pack()
	Winclasse.mainloop()

def bydefault(): #### Permet le réglage par défaut des paramètres											####CLEAN ### A TRADUIRE
	'''Cette fonction permet de rétablir les paramètres par défaut obtenu lors de notre analyse
	Description:
		Ici toute les variables nécessaires seront réglées par défaut
	Args: 
		Pas d'arguments requis
	Return:
		Pas de return
	'''
	Winclasse.destroy()
	global classes
	global method
	global gamma
	global t
	classes=1
	method='rbf'
	gamma=10000000
	t=0.0000001

def methodchoice():#### Allows to choose the classification method											####CLEAN ### A TRADUIRE
	'''This function allows the user to choose between different methods in order to personalize, if he wants to, the training method
	Description:
		Here, via a TKinter window, the user will be able to choose between different methods of training methods
	Args:
		Pas d'arguments requis
	Return :
		There is no return here. It modifies the 
		methods = which corresponds to the method chosen by the user
		classes = qui permet de récupérer la classe choisie par l'utilisateur
		Winmet = qui correspond à la fenêtre Tkinter et pourra ainsi être détruite dans la prochaine fonction
	'''
	global methods
	global classes
	global Winmet
	Winclasse.destroy()
	classes=paramvariable.get()
	if classes==1 or classes==2: #### Choice of the method in regard of SVC and NuSVC
		Winmet=Toplevel()
		Winmet.title('Choix de la méthode de classification')
		Winmet.geometry("300x110+875+500")
		Winmet.resizable(False,False)
		methodschoice="Veuillez choisir la méthode de votre choix : "
		methodchoice=Label(Winmet, text=methodschoice)
		R1=Radiobutton(Winmet, text='rbf', variable=methods,value="rbf",command=hyperparamchoice)
		R2=Radiobutton(Winmet,text='sigmoid',variable=methods,value="sigmoid",command=hyperparamchoice)
		R3=Radiobutton(Winmet, text='poly', variable=methods, value="poly",command=hyperparamchoice)
		R4=Radiobutton(Winmet, text='linear', variable=methods, value="linear",command=hyperparamchoice)
		methodchoice.pack();R1.pack();R2.pack();R3.pack();R4.pack()
	if classes==3: # Choice of the method from LinearSVC
		hyperparamchoice()
	if classes==4: # Choice of the method in regard of neural network and the Classifier class
		Winmet=Toplevel()
		Winmet.title('Choix dela méthode de classification')
		Winmet.geometry("300x110+875+500")
		Winmet.resizable(False,False)
		methodschoice="Veuillez choisir la méthode de votre choix : "
		methodchoice=Label(Winmet, text=methodschoice)
		S1=Radiobutton(Winmet, text='Relu',variable=methods, value='relu', command=hyperparamchoice)
		S2=Radiobutton(Winmet, text='Identity',variable=methods, value='identity', command=hyperparamchoice)
		S3=Radiobutton(Winmet, text='Tanh',variable=methods, value='tanh', command=hyperparamchoice)
		S4=Radiobutton(Winmet, text='Logistic',variable=methods, value='logistic', command=hyperparamchoice)
        methodchoice.pack();S1.pack();S2.pack();S3.pack();S4.pack()

def hyperparamchoice(): #### Allow to choose the hyperparameters of the method							####CLEAN ### A TRADUIRE
	'''In this function, the user is asked if he wants to adjust hyperparameters of the chosen method
	Description :
		Here, in function of the chosen method, the user can choose values of different hyperparameters
	Args :
		No Args required.
	Return:
		There is no return here.
		Variables globales modifiées :
			Tout d'abord on récupère la method dans method
			On se sert de la variable Winhyper pour la fenêtre Tkinter et ainsi la détruire dans la fonction suivante
			On récupère également la classe

	'''
	def confirmhyperparam(): #### Permet de modifier les hyperparamètres 									####CLEAN ### A TRADUIRE
		'''Ici les hyperparamètres nécessaires vont être modifiés pour être récupéré pour l'entrainement du modèle
		Description:
			Ici on récupère les valeurs entrée par l'utilisateur puis on les transforme afin qu'elles puissent être utilisée pour la classification
		Args:
			No args required.
		Return:
			No return here. En revanche les variables des hyperparamètres sont des variables globales elles seront modifiées ici. 
		'''
		global t; global gamma; global alpha; global tol; global degre; global Nu
		t=1*10**float(ttest.get())
		gamma=1*10**float(gammatest.get())
		alpha=1*10**float(alphatest.get())
		tol = 1*10**float(toltest.get())
		degre = float(degretest.get())
		Nu = float(Nutest.get())
		print alpha
		print tol
		print gamma, "testgamma"
		print t, "testt"
		Winhyper.destroy()
		eightparamchoice('')
	global method
	global Winhyper
	global classes
	method=methods.get()
	classes=paramvariable.get()
	if classes!=3:
		Winmet.destroy()
	Winhyper=Toplevel()
	Winhyper.title('Choix des hyperparamètres')
	Winhyper.geometry("325x210+865+500")
	Winhyper.resizable(False,False)
	gammatest=IntVar(); alphatest=IntVar(); toltest=IntVar(); degretest=IntVar(); ttest=IntVar(); Nutest=IntVar()
	gammatest.set(-12), ttest.set(-5), toltest.set(-7), alphatest.set(-4), degretest.set(0),Nutest.set(0)
	hyperparamtext = "Veuillez régler les hyperparamètres :"
	hyperparamtext2=Label(Winhyper,text=hyperparamtext)
	confirmchoice= Button(Winhyper, text="Valider", fg="Black",bg="SkyBlue3", command=confirmhyperparam, font=helv36)
	hyperparamtext2.pack()
	if (method=='rbf' or method=='sigmoid') and classes==1:
		gammatest=Scale(Winhyper, orient='horizontal', from_=-12, to=3,resolution=1, tickinterval=1, length=350,label="Choix de l'exposant de la valeur de gamma")
		ttest=Scale(Winhyper, orient='horizontal', from_=-5, to=7, resolution=1, tickinterval=1, length=350, label="Choix de la valeur de l'exposant de C")
		gammatest.pack();ttest.pack()
	if method=='poly' and classes==1:
		degretest=Scale(Winhyper, orient='horizontal', from_=0, to=2, resolution=1, tickinterval=1, length=350,label='Choix de la valeur de degree')
		ttest=Scale(Winhyper, orient='horizontal', from_=-5, to=-1,resolution=1, tickinterval=1, length=350,label="Choix de l'exposant de la valeur de C")
		degretest.pack();ttest.pack()
	if method=='linear' and classes==1:
		ttest=Scale(Winhyper, orient='horizontal', from_=-4, to=3, resolution=1, tickinterval=1, length=350, label="Choix de l'exposant de la valeur de C")
		ttest.pack()
	if classes==3:
		ttest=Scale(Winhyper, orient='horizontal', from_=-5, to=7, resolution=1, tickinterval=1, length=350, label='Choix de la valeur de C')
		ttest.pack()
	if (method=='rbf' or method=='sigmoid') and classes==2:
		gammatest=Scale(Winhyper, orient='horizontal', from_=-12, to=3, resolution=1, tickinterval=1, length=350, label="Choix de l'exposant de la valeur de gamma")
		Nutest=Scale(Winhyper, orient='horizontal', from_=0, to=0.9, resolution=0.1, tickinterval=0.1, length=350, label='Choix de la valeur de nu')
		gammatest.pack();Nutest.pack()
	if method=='poly' and classes==2:
		degretest=Scale(Winhyper, orient='horizontal', from_=0, to=2, resolution=1, tickinterval=1, length=350, label='Choix de la valeur de degree')
		Nutest=Scale(Winhyper, orient='horizontal', from_=0, to=0.9, resolution=0.1, tickinterval=0.1, length=350, label='Choix de la valeur de nu')
		degretest.pack();Nutest.pack()
	if method=='linear' and classes==2:
		Nutest=Scale(Winhyper, orient='horizontal', from_=0, to=0.6, resolution=0.1, tickinterval=0.1, length=350, label='Choix de la valeur de nu')
		Nutest.pack()
	if classes==4:
		alphatest=Scale(Winhyper, orient='horizontal', from_=-5, to=3, resolution=1, tickinterval=1, length=350, label="Choix de la valeur de l'exposant de alpha")
		toltest=Scale(Winhyper, orient='horizontal', from_=-7, to=2, resolution=1, tickinterval=1, length=350, label="Choix de la valeur de l'exposant de tol")
		alphatest.pack();toltest.pack()
	confirmchoice.pack()
	Winhyper.mainloop()

def eightparamchoice(check): #### Allow to choose the paramaters										####CLEAN ### A TRADUIRE
	''' This function allows to user to choose a combination of paramaters to run the classification.
	Description:
		Every button return a value between 0 and 8 corresponding of the 8 differents paramaters.
		If the button is not checked it return 9 if the user doesn't want to chose this paramater. This is default value.
	Args:
		check = permet de savoir si cela provient de la fonction Warnings
	Return:
		No return here.
		Only Win8param sert comme fenetre Tkinter afin d'être détruite par la suite
	'''
	def recoveryvalue(): #### Récupération combinaison des paramètres choisi							####CLEAN ### A TRADUIRE
		'''Ici on récupère les combinaisons de paramètres nécessaires à l'entrainement du modèle de classification
		Description:
			On récupère les valeurs des bouttons précèdent puis en fonction de leur valeur (si ils ont été cochés ou non),
			on les ajoute à la paramlist qui correspond à la combinaison de paramètres.
		Args:
			No args required
		Return:
			No return here.
			Ici seule la paramlist va être modifiée comme variable globale permettant aux autres fonctions d'accéder à la combinaison choisie
		'''
		global paramlist
		paramlist=[]
		p1=varparam.get()
		p2=varparam2.get()
		p3=varparam3.get()
		p4=varparam4.get()
		p5=varparam5.get()
		p6=varparam6.get()
		p7=varparam7.get()
		p8=varparam8.get()
		listt=[p1,p2,p3,p4,p5,p6,p7,p8]
		for i in listt:
			if i!=9:
				paramlist.append(i)
		print "Liste des paramètres : ",
		if paramlist==[]:
			printxt="Attention vous n'avez sélectionné aucun paramètre"
			labeltxt="Attention vous n'avez sélectionné aucun paramètre. \n Veuillez sélectionner au moins un paramètre."
			buttontxt="Sélection des paramètres"
			Win8param.destroy()
			Warnings(printxt,labeltxt,buttontxt,eightparamchoice)
			return
		for i in paramlist:
			print completeparamlist[i+1],
		print'.'
		Win8param.destroy()
	global Win8param
	if check=="avertissement":
		Winwarnings.destroy()
	Win8param=Toplevel()
	Win8param.title('Choix de la combinaison de paramètres')
	Win8param.resizable(False,False)
	Win8param.geometry("100x200+975+500")
	varparam=IntVar();varparam2=IntVar();varparam3=IntVar();varparam4=IntVar();varparam5=IntVar();varparam6=IntVar();varparam7=IntVar();varparam8=IntVar()
	varparam.set(9);varparam2.set(9); varparam3.set(9); varparam4.set(9); varparam5.set(9); varparam6.set(9); varparam7.set(9), varparam8.set(9)
	c1 = Checkbutton(Win8param, text="IR", variable = varparam, onvalue=0, offvalue=9)
	c2 = Checkbutton(Win8param, text="RMP", variable = varparam2, onvalue=1, offvalue=9)
	c3 = Checkbutton(Win8param, text="RH", variable = varparam3, onvalue=2, offvalue=9)
	c4 = Checkbutton(Win8param, text="ST", variable = varparam4, onvalue=3, offvalue=9)
	c5 = Checkbutton(Win8param, text="DTFS", variable = varparam5, onvalue=4, offvalue=9)
	c6 = Checkbutton(Win8param, text="SA", variable = varparam6, onvalue=5, offvalue=9)
	c7 = Checkbutton(Win8param, text="SD", variable = varparam7, onvalue=6, offvalue=9)
	c8 = Checkbutton(Win8param, text="fAHP", variable = varparam8, onvalue=7, offvalue=9)
	c9 = Button(Win8param, text="Valider", command=recoveryvalue)
	c1.pack();c2.pack();c3.pack();c4.pack();c5.pack();c6.pack();c7.pack();c8.pack();c9.pack()
	Win8param.mainloop()

def outputfilename(check):  #### Give a name to the output file											####CLEAN ### A TRADUIRE
	''' This function allows to user to give a name to the output file (the results' file).
	Description:
		Here the user can enter the name of his output file.
	Args:
		check = permet de savoir si l'appel de la fonction vient de la fonction Warnings et ainsi détruire la fenêtre Warnings
	Return:
		No return.
		Golbal variables:
			Winoutfile = fenetre Tkinter
	'''
	if check=="avertissement":
		Winwarnings.destroy()
	def recoveryfilename(): #### Récupération du nom de fichier de sortie								####CLEAN ### A TRADUIRE
		''' On récupère le nom rentré par l'utilisateur 
		Description:
			Ici l'utilisateur à rentré son nom de fichier on le récupère en variable Tkinter pour le transformé en string
		Args:
			No args required
		Return:
			No return here.
			Global variable:
				theoutputfilename = output filename as a string
		'''
		Winoutfile.destroy()
		global theoutputfilename
		theoutputfilename= var_theoutputfilename.get()
		if ".csv" not in theoutputfilename and ".txt" not in theoutputfilename:
			printxt="Attention le nom de fichier ne correspond pas au format attendu."
			labeltxt="Attention le format du fichier en entrée ne correspond pas au format attendu. \n Veuillez entrer un nom de fichier correct."
			buttontxt="Choix du nom de fichier de sauvegarde"
			Warnings(printxt,labeltxt,buttontxt,outputfilename)
			return
		print theoutputfilename, "testestest"
	global Winoutfile
	var_theoutputfilename=StringVar()
	Winoutfile = Toplevel()
	Winoutfile.title('Choix du nom de fichier de sauvegarde')
	Winoutfile.resizable(False,False)
	Winoutfile.geometry("300x85+875+500")
	choicefiletext = "Veuillez choisir le nom du fichier de sortie : \n Sous la forme example.csv ou example.txt"
	choicefiletext = Label(Winoutfile, text=choicefiletext)
	validernomfichier= Button(Winoutfile, text="Valider", command=recoveryfilename)
	entrernomfichier = Entry(Winoutfile, width=30, textvariable=var_theoutputfilename)
	choicefiletext.pack();entrernomfichier.pack();validernomfichier.pack()

def choicesample(): #### Choix de l'échantillonnage												####CLEAN ### A TRADUIRE
	'''Dans cette fonction on propose à l'utilisateur de choisir l'échnatillonnage qu'il souhaite pour lancer la simulation de la classification
	avec son modèle
	Description:
		Ici l'utilisateur pourra choisir entre 3 manières d'échantillonner son fichier d'entrainement soit :
			75% entrainement et 25% pour tester
			50% entrainement et 50% pour tester
			25% entrainement et 75% pour tester
		son choix sera sauvegarder pour la simulation.
	Args:
		No args required
	Return
		No return here
		Global variables:
			Winech = fenêtre Tkinter
			samples= stockant le choix d'échantillonnage
	'''
	global Winech
	global samples
	if trainlist==[]:
		printxt="Attention fichier d'entraînement non chargé"
		labeltxt="Attention il n'y a pas de fichier d'entraînement pour la simulation ou le fichier est vide. \n Veuillez charger un fichier."
		buttontxt="Chargement d'un fichier d'entraînement"
		Warnings(printxt,labeltxt,buttontxt,loadtrain)
	else:
		Winech=Toplevel()
		Winech.title("Choix de l'échantillonnage pour la simulation")
		Winech.resizable(False,False)
		Winech.geometry("325x80+865+500")
		simulationtext="Veuillez choisir votre méthode d'échantillonnage :"
		simulationtext=Label(Winech, text=simulationtext)
		echantillon1= Radiobutton(Winech, text = "50/50", variable = samples, value = 1,command=simulationresults)
		echantillon2= Radiobutton(Winech, text = "25/75", variable = samples, value = 2, command=simulationresults)
		echantillon3= Radiobutton(Winech, text = "75/25", variable = samples, value = 3, command=simulationresults)
		simulationtext.pack();echantillon1.pack();echantillon2.pack();echantillon3.pack()
		Winech.mainloop()

def simulationresults(): #### Simulation de la classification												####CLEAN ### A TRADUIRE
	'''Entrainement du modèle de classification selon l'echantillonage puis simulation de la classification et comparaison 
	des résultats avec les valeurs prédéfinies
	Description:
		On va tout d'abord entrainer un modèle de classification selon l'échantillonnage choisi puis on lance une simulation de classification
		avec les paramètres choisi par l'utilisateur toujours selon l'échantillonnage puis avec les résultats de cette classification on compare 
		avec les valeurs prédéfinies puis on transforme le tout en pourcentage de réussite qui sera alors affiché dans la fenêtre Tkinter.
	Args:
		No args required.
	Return:
		No return here.
		Global variables:
			sampling permet de récupérer le choix d'échantillonnage lors de l'entraînement du modèle.
	'''
	global sampling
	Winech.destroy()
	Winsimulation=Toplevel()
	Winsimulation.resizable(False,False)
	Winsimulation.title("Résultat de la simulation du modèle")
	Winsimulation.geometry("300x250+875+500")
	sampling=samples.get()
	test=trainingfile(1)
	result=clf.predict(test[0])
	beep(1)# Permet d'émettre un son
	x=0
	summ=0
	length=len(test[1])
	while x<len(test[1]):
		if result[x]==test[1][x]:
			summ=summ+1
		x=x+1
	percentage=(float(summ)/length)*100
	percentage=round(percentage,2)
	print percentage,"%"
	simulationtext=Label(Winsimulation, text="Le pourcentage de réussite est de :")
	textepourcentage=Label(Winsimulation, text=percentage)
	txtclass="\nCette simulation a été réalisée avec :\n"
	txtparam=txtrecall(txtclass)
	param=Label(Winsimulation,text=txtparam)
	Q1= Button(Winsimulation, text= "Fermer", command= Winsimulation.destroy)
	simulationtext.pack();textepourcentage.pack();param.pack();Q1.pack()
	Winsimulation.mainloop()

def save(): #### Sauvegarde des résultats de la classification dans le fichier de sortie					####CLEAN ### A TRADUIRE
	'''Ici on sauvegarde les résultats dans le fichier souhaité
	Description:
		Si le nom du fichier n'a pas été choisi, il sera demandé à l'utilisateur
		en revanche si il l'a été alors la sauvegarde est lancé
	'''
	if theoutputfilename=='':
		printxt="Attention nom de fichier non défini"
		labeltxt="Attention le nom de fichier de sortie n'a pas été fourni. \n Veuillez entrer un nom de fichier."
		buttontxt="Choix du nom de fichier de sortie"
		Warnings(printxt,labeltxt,buttontxt,outputfilename)
	else:
		addtodataset(theoutputfilename,"w",0)

def addtodataset(filename,mod,nb): #### Ecris dans le fichier souhaité à la suite ou réécrit				####CLEAN ### A TRADUIRE
	'''Cette fonction permet d'écrire dans les fichiers souhaité
	Description:
		Cette donction permet d'écrire dans un fichier, selon les arguments lors de l'appel, elle permet de sauvegarder les résultats
		de la classification à la suite du fichier ou de réécrire le fichier.
	Args:
		filename = nom du fichier dans lequel on écrit
		mod = permet de modifier le mode, d'écriture, à la suite ou non 
		nb = permet d'ignorer ou non la première list de resultdataset (en-tête: nClass,IR,RMP,...) lors de l'écriture
	'''
	file=codecs.open(filename,mod,encoding="utf-8")
	i=nb
	while i<len(resultdataset):
		j=0
		while j<len(resultdataset[i]):
			file.write(str(resultdataset[i][j]))
			file.write(',')
			j=j+1
		file.write('\n')
		i=i+1
	file.close

def modiftable(): #### Permet de modifier les jeux de données												####CLEAN ### A TRADUIRE
	'''Cette première partie de la fonction permet de vérifier que l'utilisateur est sûr de vouloir modifier les fichiers d'entrainement
	Description:
		Ici une fenêtre Tkinter est créée pour vérifier que l'utilisateur souhaite ajouter ses résultats aux prochains entrainements.
	Args:
		No args required.
	Return:
		No return here.
	'''
	global Winverif
	def finaladd(): #### Ajout aux fichiers des résulats obtenu et vérifié									####CLEAN ### A TRADUIRE
		'''Ecriture dans les fichiers des résultats de la classification
		Description:
			Ici on écrit dans nos fichiers d'entrainements et si l'utilisateur a entré son fichier son fichier cela sera ajouté au sien également
		Args:
			No args required.
		Return:
			No return
		'''
		if userdataset!=0:
			addtodataset('TrainModel.csv',"a",1)
		addtodataset('ModelG.csv',"a",1)
		Winverif.destroy()
	Winverif=Toplevel()
	Winverif.title('Vérification')
	Winverif.resizable(False,False)
	Winverif.geometry("350x85+875+500")
	txtavertissement=Label(Winverif,text="Etes-vous sûr de vouloir entraîner les modèles?")
	A1=Button(Winverif, text='Oui',command=finaladd)
	A2=Button(Winverif, text='Non', command=Winverif.destroy)
	txtavertissement.pack();A1.pack();A2.pack()
	Winverif.mainloop()

def cancel(): ####Copier le backup dans le modelG.csv et copie Yourbackup dans TrainModel					####CLEAN ### A TRADUIRE
	'''Permet de revenir à l'état des fichiers backups
	Description:
		Si l'utilisateur choisi d'utiliser ces résultats pour entrainer ses prochains modèles alors qu'il n'avait pas vérifié ses résultats
		ou même qu'ils souhaitent revenir à l'étape précédente cette fonction permettra de copier ce qui se trouve dans les fichier backup vers 
		les model
	Args:
		No args required.
	Return:
		No return here.
	'''
	shutil.copyfile('Backup_G.csv','ModelG.csv')
	shutil.copyfile('Yourbackup.csv','TrainModel.csv')

def Warnings(printxt,labeltxt,buttontxt,function): #### Permet la gestion d'erreurs							####CLEAN ### A TRADUIRE
	'''Cette fonction est une fonction appelée lorsqu'une erreur peu avoir lieu, en prévention d'éventuelles erreurs
	Description:
		Ici c'est une fonction complétement customisable lors de son appel, on pourra choisir ce qui s'affiche dans la fenêtre mais également 
		quelle fonction appeler pour résoudre l'erreur
	Args:
		printxt = string qui s'affichera dans le terminal
		labeltxt = label sous forme de string qui s'affichera dans la fenêtre tkinter
		buttontxt = string qui s'affichera sur le bouton de la fenêtre Warnings
		function = correspon à la fonction a appeler pour éviter l'erreur
	Return:
		No return needed.
		Global variables:
			Winwarnings = fenêtre Tkinter
	'''
	global Winwarnings
	print printxt
	Winwarnings=Toplevel()
	Winwarnings.resizable(False,False)
	Winwarnings.geometry("550x85+775+500")
	beep(1)
	Winwarnings.title("Avertissement")
	txtavertissement=Label(Winwarnings,text=labeltxt)
	txtavertissement.pack()
	c="avertissement"
	A1= Button(Winwarnings,text=buttontxt,command=lambda c=c:function(c))
	A1.pack()
	Winwarnings.mainloop()

def txtrecall(mod):
	txtclass=mod+listclass[classes-1]+"\n"
	txtmethod=''
	if classes!=3:
		txtmethod="La méthode :\n"
		txtmethod=txtmethod+method+"\n"
	txthyperparam=""
	if classes==3:
		txthyperparam="C ="+str(t)+"\n"
	if classes==1 or classes==2:
		if method=='rbf' or method=='sigmoid':
			txthyperparam=txthyperparam+"gamma = "+str(gamma)+"\n"
		if method=='poly':
			txthyperparam=txthyperparam+"degree = "+str(degre)+"\n"
		if classes==1:
			txthyperparam="Mais également l'hyperparamètre : \nC = "+str(t)+"\n"+txthyperparam
		if classes==2:
			txthyperparam="Mais également l'hyperparamètre : \nNu = "+str(Nu)+"\n"+txthyperparam
	if classes==4:
		txthyperparam="alpha = "+str(alpha)+"\n"+"tol = "+str(tol)+"\n"
	txtcombiparam='Et le combinaison de paramètres :\n'
	for i in paramlist:
		txtcombiparam=txtcombiparam+" "+completeparamlist[i+1]
	txtcombiparam=txtcombiparam+"\n"
	txtparam=txtclass+txtmethod+txthyperparam+txtcombiparam
	return txtparam

def startanalyse(): #### Start the analyse of neuron classification
	''' This function allows to give the neuron's type (I or II).
	Description:
		Allows the visualization of the results as well as their graphic's representation (diagram with the number of type I and type II)
	Args:
		No Args here.
	Return:
		No return.
		Global variables:
			resultdatset = correpsond à une liste à deux dimension dans laquelle on va mettre nos deux résultats, les en-têtes, mais aussi
			les valeurs des paramètres pour chaque neurones
	'''
	global resultdataset
	resultdataset=[]
	if testlist==[]:
		printxt="Attention fichier de test non chargé"
		labeltxt="Attention il n'y a pas de fichier de test pour l'analyse ou le fichier est vide. \n Veuillez charger un fichier."
		buttontxt="Chargement d'un fichier test"
		Warnings(printxt,labeltxt,buttontxt,loadtest)
		return
	if trainlist==[]:
		printxt="Attention fichier d'entrainement non chargé"
		labeltxt="Attention il n'y a pas de fichier d'entrainement pour l'analyse ou le fichier est vide. \n Veuillez charger un fichier."
		buttontxt="Chargement d'un fichier d'entrainement"
		Warnings(printxt,labeltxt,buttontxt,loadtrain)
		return
	def changetype(c): #### Correction de la valeur déterminée par le modèle									####CLEAN ### A TRADUIRE
		'''Ici lors de l'affichage du tableau des résultats on pourra éditer le type du neurone
		Description:
			L'utilisateur pourra cliquer sur le chiffre de son choix pour le modifier selon son envie
		Args:
			No args required.
		Return:
			No return here
			Global variables:
				choice = sauvegarde le choix de l'utilisateur
				Winchoiceclass = fenêtre Tkinter
		'''
		global choice
		global Winchoiceclass
		Winchoiceclass=Toplevel()
		A1= Radiobutton(Winchoiceclass, text='1',variable=choice, value=1)
		A2= Radiobutton(Winchoiceclass, text='2',variable=choice, value=2)
		A3= Button(Winchoiceclass,text='Valider',command=lambda c=c:vartest(c))
		A1.pack();A2.pack();A3.pack()
		Winchoiceclass.mainloop()
	#
	def vartest(c): #### Modification de la valeur souhaité dans les résultats									####CLEAN ### A TRADUIRE
		'''Permet de modifier le résultat de la classification pour le neurone souhaité
		Description:
			On modifie selon le choix de l'utilisateur la valeur dans resultdataset
		Args:
			No args needed
		Return:
			No return here
		'''
		Winchoiceclass.destroy()
		tmp=choice.get()
		global resultdataset
		resultdataset[c][0]=tmp
		choice.set(0)
		tableresults(frame)
	#
	def onFrameConfigure(canvas): #### Scrollbar dans le tableau de résultats									####CLEAN ### A TRADUIRE
		'''Permet l'utilisation d'une scrollbar dans la fenêtre de résultats
		Description:
			La fenêtre résultats de la classification aura une scrollbar, en effet si la taille du tableau est plus grande que la fenêtre,
			il sera nécessaire d'avoir une scrollbar pour visualiser les autres résultats.
		Args:
			No args needed.
		Return:
			No return needed.		
		'''
		canvas.configure(scrollregion=canvas.bbox("all"))
	#
	def tableresults(frame): #### Tableau de résultats															####CLEAN ### A TRADUIRE
		'''Affichage des résultats de la classification sous la forme d'un tableau
		Description:
			Ici via deux boucles imbriquées on affiche le tableau dans la fenêtre des résultats
		Args:
			frame = correspond à la fenêtre dans laquelle sera affichée le tableau de réultats
		Return:
			No return here.
		'''
		i=0
		while i<len(resultdataset): #### i = row
			j=0
			while j<len(resultdataset[i]): #### j = column
				if j==0:
					if i==0:
						tk.Label(frame,text=resultdataset[i][j],relief=FLAT, borderwidth=1).grid(row=i,column=j,ipadx=5,ipady=4)
					if i!=0:
						Button(frame,text=resultdataset[i][j], relief=FLAT, borderwidth=1, command=lambda c=i:changetype(c)).grid(row=i,column=j,ipadx=5,ipady=4)
				else:
					tk.Label(frame,text=resultdataset[i][j],relief=FLAT, borderwidth=1).grid(row=i,column=j,ipadx=5,ipady=4)
				j=j+1
			i=i+1
	#
	def diagram(): #### Affichage du diagramme																	####CLEAN ### A TRADUIRE 
		'''Permet d'afficher un diagramme en forme de camembert
		Description:
			Ici on va servir du nombre de type 1 et du nombre de type 2 pour avoir un pourcentage que l'on va utiliser dans le graph
		Args:
			No args needed
		Return:
			No return here
		'''
		namepart = ["TypeI", "TypeII"] #### Part's name
		typeofneuron = [type1, type2] #### Number of type I neurons and number of type II
		explosion=(0, 0.1) #### Separation of the two parts
		plt.pie(typeofneuron, explode=explosion, labels=namepart, autopct='%1.1f%%', startangle=90, shadow=True) #### autopct = actual percentage compared to the one indicated
		plt.axis("equal") #### axis = Create a circular diagram
		plt.show("Type de neurones")
		return
	#
	def plot(): #### Affiche un graph en 3D ou 2D selon la liste de paramètre
		'''Permet d'afficher un graph en 3D ou 2D selon la sélection des paramètres de l'utilisateur
		Description:
			Ici on va mettre en place les données pour le graph et la visualisation cependant nous somme limité par une vision en 3D et donc on ne peut pas
			choisir plus de 3 paramètres. 
			Ainsi en fonction de la longueur de la paramlist on pourra déterminer si l'utilisateur doit choisir parmis ces paramètres ou non.
		Args:
			No args required.
		Return:
			No return here.
		'''
		TMP1=[]
		TMP2=[]
		tmp11=[]
		tmp12=[]
		tmp21=[]
		tmp22=[]
		tmp31=[]
		tmp32=[]
		if len(paramlist)>3:
			printxt="Attention il est nécessaire de ne pas sélectionner plus de 3 paramètres pour cette visualisation"
			labeltxt="Attention il est nécessaire de ne pas sélectionner \n plus de 3 paramètres pour cette visualisation. \n Veuillez choisir vos paramètres."
			buttontxt="Sélectionner les 3 paramètres nécessaires"
			Warnings(printxt,labeltxt,buttontxt,eightparamchoice)
			return
		else:
			i=0
			while i<len(resultdataset):
				if resultdataset[i][0]==1:
					tmp11.append(resultdataset[i][paramlist[0]+1])
					if len(paramlist)>1:
						tmp21.append(resultdataset[i][paramlist[1]+1])
						if len(paramlist)>2:
							tmp31.append(resultdataset[i][paramlist[2]+1])
				if resultdataset[i][0]==2:
					tmp12.append(resultdataset[i][paramlist[0]+1])
					if len(paramlist)>1:
						tmp22.append(resultdataset[i][paramlist[1]+1])
						if len(paramlist)>2:
							tmp32.append(resultdataset[i][paramlist[2]+1])
				i=i+1
		if len(paramlist)==1:
			for i in range(len(tmp11)):
				TMP1.append(i)
			for j in range(len(tmp12)):
				TMP2.append(j)
			plt.title(u"Représentation des classes de neurones",fontsize=16) #titre du graph
			plt.scatter(TMP1,tmp11,label='Type 1',color='b',s=10,marker='^')
			plt.scatter(TMP2,tmp12,label='Type 2',color='r',s=10,marker='*')
			plt.xlabel('Neurones x') #légende x
			plt.ylabel(completeparamlist[paramlist[0]+1]) #légende y
			plt.legend(loc=4)
			plt.show()
			return
		elif len(paramlist)==2:
			plt.title(u"Représentation des classes de neurones",fontsize=16) #titre du graph
			plt.scatter(tmp11,tmp21,label='Type 1',color='b',s=10,marker='^')
			plt.scatter(tmp12,tmp22,label='Type 2',color='r',s=10,marker='*')
			plt.xlabel(completeparamlist[paramlist[0]+1]) #légende x
			plt.ylabel(completeparamlist[paramlist[1]+1]) #légende y
			plt.legend(loc=4)
			plt.show()
			return
		elif len(paramlist)==3:
			fig = plt.figure()
			ax = fig.add_subplot(111, projection='3d')
			plt.title(u"Représentation des classes de neurones",fontsize=16) #titre du graph
			ax.scatter(tmp11,tmp21,tmp31,label='Type 1', c='b',s=10,marker='^')
			ax.scatter(tmp12,tmp22,tmp32,label='Type 2', c='r',s=10,marker='*')
			ax.set_xlabel(completeparamlist[paramlist[0]+1])
			ax.set_ylabel(completeparamlist[paramlist[1]+1])
			ax.set_zlabel(completeparamlist[paramlist[2]+1])
			plt.legend(loc=4)
			plt.show()
			return
	#
	trainingfile(0)
	Winclassification=Toplevel()
	Winclassification.title("Résultats de l'analyse")
	Winclassification.geometry("1200x800+500+200")
	A1=Button(Winclassification, text="Sauvegarder les résultats", command=save, bg="SkyBlue3")
	di1=Button(Winclassification, text="Afficher le diagramme", command=diagram, bg="SkyBlue3")
	A4=Button(Winclassification, text="Afficher un aperçu de la classification", command=plot, bg="SkyBlue3")
	A5= Button(Winclassification, text= "Choix des paramètres", command= lambda c='':eightparamchoice(c),bg= "SkyBlue3")
	txtclass="Cette classification a été réalisée avec la classe :\n"
	txtparam=txtrecall(txtclass)
	modif=Label(Winclassification,text="\n Si vous souhaitez modifier les résultats, \n appuyez sur le 1 ou 2 souhaité. \n Puis choisissez le résultat attendu.\n \n Si vous souhaitez entraîner les modèles,\n cliquer sur le bouton ci-dessous,\n ATTENTION veillez à bien vérifier les résultats \n AVANT l'entraînement!",relief=FLAT,borderwidth=1)
	A2=Button(Winclassification,text="Entraîner les modèles avec vos résultats",command=modiftable,bg="thistle")
	A3=Button(Winclassification,text="Rétablir les modèles à l'original",command=cancel,bg="thistle")
	instruc=Label(Winclassification,text="Pour charger le modèle entraîné, \n il faudra choisir le fichier d'entraînement : \n 'TrainModel.csv' si vous avez entré \n votre fichier d'entraînement \n ou sinon 'ModelG.csv'.\n")
	param=Label(Winclassification,text=txtparam,relief=FLAT,borderwidth=1)
	canvas=tk.Canvas(Winclassification,borderwidth=1)
	frame = tk.Frame(canvas)
	vsb = tk.Scrollbar(Winclassification, orient="vertical", command=canvas.yview)
	canvas.configure(yscrollcommand=vsb.set)
	vsb.pack(side="right", fill="y");canvas.pack(side="left", fill="both", expand=True);A1.pack();di1.pack();A4.pack();A5.pack();modif.pack();A2.pack();A3.pack();instruc.pack();param.pack()
	canvas.create_window((4,4), window=frame, anchor="nw")
	frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
	dataset=[]
	for sample in testlist:
		s=[]
		for i in paramlist:
			s.append(sample[i])
		dataset.append(s)
	X_test=np.array(dataset)# Passage du tableau en format numpy
	result=clf.predict(X_test)####################### PREDICTION !!!!!!
	resultdataset.append(completeparamlist) # ajout de l'entête
	#boucle pour former le tableau à 2D final
	d=0
	while d<len(result):
		sample=[]
		sample.append(result[d])
		k=0
		while k<len(testlist[d]):
			sample.append(testlist[d][k])
			k=k+1
		resultdataset.append(sample)
		d=d+1
	beep(1)# Permet d'émettre un son
	tableresults(frame)
	type1=0
	type2=0
	for i in result:
		if i==1:
			type1=type1+1 #### Counter to find out the number of type I neurons
		if i==2:
			type2=type2+1 #### Counter to find out the number of type II neurons
	print "Classification terminée"
	Winclassification.mainloop()

def presentation(): #### Presentation of the project's group
	''' This function allows to present the project's group.
	Args:
		No arguments.
	Return:
		No return.
	'''
	presentation=Toplevel()
	presentation.resizable(False,False)
	presentation.title("Presentation")
	presentation.geometry("800x600+600+300")
	textepresentation="Actuellement étudiants en Master 1 à l'Université de Bordeaux,\n nous avons pour projet de classer des neurones en deux types : Type I et Type II.\n Les données electrophysiologiques vont être la source de classification.\n 8 paramètres sont donc retenus : IR,RMP,RH,SD,DTFS,SA,SD,fAHP \n"
	text=Label(presentation,text=textepresentation)
	text.pack()
	presentation.mainloop()

def softwarexplanation(): ###### Explications of the software
	''' Cette fonction permet d'arriver sur l'aide pour le client
	Args:
		No arguments.
	Return:
		No return.
	'''
	explanation=Toplevel()
	explanation.title("Aide")
	explanation.resizable(False,False)
	explanation.geometry("350x150+850+500")
	Sklearn=Button(explanation, text="Lien vers Scikit-Learn",fg="Black",bg="SkyBlue3",command=lambda:webbrowser.open('http://scikit-learn.org/stable/'))
	SVM=Button(explanation, text="Lien vers la documentation des SVM",fg="Black",bg="SkyBlue3",command=lambda:webbrowser.open('http://scikit-learn.org/stable/modules/svm.html#'))
	NeuronNetwork=Button(explanation, text="Lien vers la documentation des Réseaux de neurones",fg="Black",bg="SkyBlue3",command=lambda:webbrowser.open('http://scikit-learn.org/stable/modules/neural_networks_supervised.html'))
	presentationtext="Veuillez vous reporter au manuel d'utilisation" ### Manuel + Lien scikit-learn
	text=Label(explanation, text=presentationtext)
	text.pack();Sklearn.pack();SVM.pack();NeuronNetwork.pack()
	explanation.mainloop()

###############################################################    MAIN    ###############################################################
b1= Button(app, text= "Ajustement des paramètres", fg= "Black",bg= "SkyBlue3", command= choiceparamclass, font= helv36, bd= 4)
b2= Button(app, text= "Chargement du fichier d'entraînement", fg= "Black", bg= "SkyBlue3", command=lambda c='':loadtrain(c), font= helv36, bd= 4)
b3= Button(app, text= "Lancer la simulation", fg= "Black", bg= "SkyBlue3", command= choicesample, font= helv36, bd= 4)
b4= Button(app, text= "Chargement du fichier à analyser",fg= "Black", bg= "SkyBlue3", command=lambda c='':loadtest(c), font= helv36, bd= 4)
b5= Button(app, text= "Choisir le nom du fichier de sortie", fg= "Black", bg= "SkyBlue3", command=lambda c='':outputfilename(c), font= helv36, bd= 4)
b6= Button(app, text= "Lancer la classification", fg= "Black",bg= "SkyBlue3", command= startanalyse, font= helv36, bd= 4)
b7= Button(app, text= "Quitter l'application", fg= "Black",bg= "SkyBlue3", command= sys.exit, font= helv36, bd= 4, bitmap= "error")
menu1 = Menu(menubar, tearoff=0)
menu2 = Menu(menubar, tearoff=0)
menu3 = Menu(menubar, tearoff=0)
######################### Anchoring elements in the GUI
b1.place(x=300, y=100, width=250, height=40)
b2.place(x=300, y=150, width=250, height=40)
b3.place(x=300, y=200, width=250, height=40)
b4.place(x=300, y=250, width=250, height=40)
b5.place(x=300, y=300, width=250, height=40)
b6.place(x=340, y=470, width=170, height=60)
b7.place(x=350, y=540, width=150, height=30)
text.place(x=180, y=0, width=500, height=50)

#####################################    Toolbar
####   Menu 1
menu1.add_separator()
menu1.add_command(label = "Ouvrir un fichier d'entraînement", command=lambda c='':loadtrain(c))
menu1.add_separator()
menu1.add_command(label="Ouvrir un fichier test", command=lambda c='':loadtest(c))
menu1.add_separator()
menubar.add_cascade(label="Fichier", menu=menu1) ###### Name on the toolbar

####   Menu 2
menu2.add_separator()
menu2.add_command(label="Regler les paramètres", command=choiceparamclass)
menu2.add_separator()
menu2.add_command(label="Lancer la simulation", command=choicesample)
menu2.add_separator()
menubar.add_cascade(label="Option", menu=menu2)

####   Menu 3
menu3.add_separator()
menu3.add_command(label="Qui sommes nous?", command=presentation)
menu3.add_separator()
menu3.add_command(label="Aide d'utilisation", command=softwarexplanation)
menu3.add_separator()
menubar.add_cascade(label="Aide", menu=menu3)

####   Toolbar/tools
app.config(menu=menubar)
app.mainloop()
