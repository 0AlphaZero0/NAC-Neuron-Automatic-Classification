# coding: utf-8
#BLAIS Benjamin
#COTTAIS Déborah
#DE OLIVEIRA Lila
#JOUAN Clement
#THOUVENIN Arthur

import numpy as np # Allows to manipulate the necessary table for sklearn
import matplotlib.pyplot as plt # Allows to create graphics, especially those in 3D
import urllib # Allows to open URL links =============================================== ***** est ce que l'on s'en sert???????****
import tkFont # Allows to modify the TKinter display font
import codecs # Allows to load a file containing UTF-8 characters
import random # Allows to use random variables
import os # Allows to modify some things on the os
import Tkinter as tk # Allows the TKinter database with the abreviation tk
import tkFileDialog  # Allows to create a windows to load files
import shutil #permet la copie de fichier
from sklearn import svm # Allows to use the SVM classification method
from sklearn.neural_network import MLPClassifier # Allows the use of the neural network method from sklearn
from matplotlib import style # Allows to modify the graphics' appearance
from Tkinter import * # Allows the use of the TKinter GUI
from matplotlib.figure import * # Allows the modification of the matplotlib graphics' appearances
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # ???????????????????????????????????????????????
########   If needed   #############
import sys

#################################    Main window of the GUI    ###################################################
app = tk.Tk()
app.title("Classification neuronale") # Give a title to the window
app.geometry("800x600+600+300") # Anchor the window
app.configure(background="SlateGray2")# Background color
fond0=tk.Canvas(app, width=800, height=600, background='SlateGray2')
fond0.pack()
img=tk.PhotoImage(file="miaou2.gif") #https://itsocial.fr/wp-content/uploads/2017/04/iStock-509365378-696x431.png
fond0.create_image(150,350, image=img)
img1=tk.PhotoImage(file="bdx_1.gif")
fond0.create_image(700,550, image=img1)
img2=tk.PhotoImage(file="scikit_learn11.gif")
fond0.create_image(700,450, image=img2)

########    Variables    ########
beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
clf= svm.SVC(kernel='rbf', gamma=0.1, C=0) #### To modify with consistent values
helv36 = tkFont.Font(family='Helvetica', size=10, weight='bold')
listeparam=[]
listeparamcomplete=["nClass","IR","RMP","RH","ST","DTFS","SA","SD","fAHP"]
listetest=[]
listeentrainement=[]
resultdataset=[]
menubar = Menu(app)
methodes=StringVar()
methode=StringVar()
modi=0
nomfichiersortie=StringVar()
nomfichiersortie.set('')
pourtitre = tkFont.Font(family='Helvetica', size=25, weight='bold')
separateur=StringVar()
separateur2=StringVar()
t=IntVar()
gamma=IntVar()
alpha=IntVar()
variableatester=IntVar()
variableparam=IntVar()
variableparametres=IntVar()
tmp=IntVar()
classe=IntVar()
echantillons=IntVar()
echantillonnage=IntVar()
text=Label(app, text="Classification Neuronale", fg="RoyalBlue3", bg="SlateGray2", font=pourtitre)
######Definitions
def Chargementtest(check): #### Gives the absolute path of the file
	'''This function retrieves the path to the Test file
	Description:
		Here, the user is asked to, via the Tkinter GUI, to choose the Test file of his choice. The path to this file will then be retrieved.
	Args:
		No Args required
	Return:
		No return, here, global variables are modified.
	'''
	if check=="avertissement":
		avertissement.destroy()
	separateurfichier(2)

def separateurfichier(verif): #### Give the file separator
	''' This function allows to give the file separator
	Description:
		Here, the user can choose the separator of his file. There are five possibilities.
	Args:
		No Args required
	Return:
		No return. Here, global variables are modified.
	'''
	def resultatsseparateur():
		global separateur
		global separateur2
		separateur2=separateur.get()
		print separateur2
	global separateur
	global loade
	loade=Toplevel()
	s1 = Radiobutton(loade, text = "Virgule", variable = separateur, value =',',command=resultatsseparateur)
	s2 = Radiobutton(loade, text = "Point-virgule", variable = separateur, value =';', command=resultatsseparateur)
	s3 = Radiobutton(loade, text = "Tab", variable = separateur, value ='	',command=resultatsseparateur)
	s4 = Radiobutton(loade, text = "Deux points", variable = separateur, value =':', command=resultatsseparateur)
	s5 = Radiobutton(loade, text = "Espace", variable = separateur, value =' ', command=resultatsseparateur)
	s9 = Button(loade, text="Valider", command=lambda c=verif:Chargemententrainementfinal(c))
	s1.pack();s2.pack();s3.pack();s4.pack();s5.pack();s9.pack();
	loade.mainloop()

def Chargemententrainementfinal(verif):
	global listeentrainement
	global listetest
	global modi
	loade.destroy()
	if verif==1:
		modi=1
		nomdufichierentrainement=tkFileDialog.askopenfilename(initialdir = "/net/cremi/athouvenin/Bureau/Projet-Neuro/Arthur",title = "Selection du fichier entrainement",filetypes = (("Fichier csv","*.csv"),("Fichier texte","*.txt")))
		shutil.copyfile(nomdufichierentrainement,'TrainModel.csv')
		shutil.copyfile(nomdufichierentrainement,'Yourbackup.csv')
		listeentrainement=load(nomdufichierentrainement,0)
	else:
		modi=0
		nomdufichiertest = tkFileDialog.askopenfilename(initialdir = "/net/cremi/athouvenin/Bureau/Projet-Neuro/Arthur",title = "Selection du fichier test",filetypes = (("Fichier csv","*.csv"),("Fichier texte","*.txt")))
		listetest=load(nomdufichiertest,1)

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
	global avertissement
	result=file(filename,"r").read().replace(separateur2, ",")
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
			if typefichier==0 : # trainning file
				if len(y)>9 or len(y)<9:
					print "Attention fichier d'entrainement incorrect"
					avertissement=Toplevel()
					beep(1)
					avertissement.title("Avertissement")
					txtavertissement=Label(avertissement,text="Attention le fichier d'entrainement soumis, ne correspond à l'entrée nécessaire. \n Veuillez chargez un fichier d'entrainement pour l'analyse.")
					txtavertissement.pack()
					c="avertissement"
					A1= Button(avertissement,text="Chargement d'un fichier d'un fichier d'entrainement",command=lambda c=c:Chargementtest(c))
					A1.pack();
					avertissement.mainloop()
					return
				y[0]=int(y[0])
				x=1
				while x<len(y):
					y[x]=float(y[x])
					x=x+1
				dataset.append(y)
			if typefichier==1: # test file
				x=0
				if len(y)>8 or len(y)<8:
					print "Attention fichier de test incorrect"
					avertissement=Toplevel()
					beep(1)
					avertissement.title("Avertissement")
					txtavertissement=Label(avertissement,text="Attention le fichier test soumis, ne correspond à l'entrée nécessaire. \n Veuillez chargez un fichier pour l'analyse.")
					txtavertissement.pack()
					c="avertissement"
					A1= Button(avertissement,text="Chargement d'un fichier d'un fichier test",command=lambda c=c:Chargementtest(c))
					A1.pack();
					avertissement.mainloop()
					return
				while x<len(y):
					y[x]=float(y[x])
					x=x+1
				dataset.append(y)
	file.close
	os.remove("tmp.csv")
	return dataset

def Chargemententrainement(check):#### Loading of the training file
	'''This function allows the user to choose a training file from his own data or a default file given by us
	Description:
		Here, a window is created to allow the user to choose whether he wants to use his own data or the default one (thanks to yes/no buttons)
	Args:
		No Args required.
	Return:
		There is no return, only the variable to be tested is modified as a global variable
	'''
	global variableatester
	global entrainement
	if check=="avertissement":
		avertissement.destroy()
	entrainement=Toplevel()
	entrainement.title("Le fichier d'entraînement")
	textefichier="Avez-vous un jeu d'essai?"
	fichiers=Label(entrainement,text=textefichier)
	fichiers.pack()
	R1 = Radiobutton(entrainement, text="Oui", variable=variableatester, value=1,command=lambda c='entrainement':resultatsappui(c))
	R1.pack( anchor = W )
	R2 = Radiobutton(entrainement, text="Non", variable=variableatester, value=2, command=lambda c='entrainement':resultatsappui(c))
	R2.pack(anchor = W)

def resultatsappui(check):#### Choice of the training file
	'''This function allows, via a small TKinter window, to choose among the user's folders the desired file
	Description :
		Here, a TKinter window is opened allowing the user to choose his file and allowing the program to recover the absolute path
		which will be used for the training of the statistical model thanks to the function entrainementdufichier()
	Args :
		No Args required
	Return :
		There is no return, only the listeentrainement variable is modified, which allows to train the statistic model thanks to the entrainementdufichier() function
	'''
	global separateur2
	if check=="entrainement":
		entrainement.destroy()
	variable2=variableatester.get()
	if variable2==1:
		separateurfichier(1)
	if variable2==2:
		nomdufichierentrainement=('ModelG.csv')####Path of our test file
		separateur2=','
		listeentrainement=load(nomdufichierentrainement,0)

def entrainementdufichier(verif):#### Training of the statistical model
	'''Here, in function of the class and the model as well as hyperparameters of the method, the training table will allow to train the statistical model
	Description :
		Here, thanks to multiple conditions, it is possible to choose the class and the method wished by the user to train the model
	Args :
		No Args required.
	Return :
		There is no return here, only the variable clf is modified, it is the one which contains the training method, it will be modified according to the choice of the user
	'''
	global clf
	# Variables
	dataset=[]
	y_train=[]
	X_train=[]
	#Choix des combinaisons de paramètres
	for sample in listeentrainement:
		s=[]
		s.append(sample[0])
		for i in listeparam:
			s.append(sample[i+1])
		dataset.append(s)
	######## Analyse
	if verif==0:
		print "=== Analyse ==="
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
			if echantillonnage==1:
				div=2
			if echantillonnage==2 or echantillonnage==3:
				div=4
			limit=datalength/div
			if limit<len(dataset):
				if echantillonnage==2 or echantillonnage==1:
					test.append(dataset.pop(rand)) #75% of sample in test
				if echantillonnage==3:
					train.append(dataset.pop(rand)) #75% of sample in train
			else:
				if echantillonnage==2 or echantillonnage==1:
					train.append(dataset.pop(rand)) #75% of sample in train
				if echantillonnage==3:
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
	if classe==1: ########## If SVC were chosen
		if methode=='rbf':
			print "RBF Method"
			clf= svm.SVC(kernel=methode, gamma=gamma, C=t) ###" to change kernel and gamma
		if methode=='sigmoid':
			print "Sigmoid Method"
			clf= svm.SVC(kernel=methode, gamma=gamma, C=t) ###" to change kernel and gamma
		if methode=='poly':
			print "Poly Method"
			clf= svm.SVC(kernel=methode, degree=degre, C=t1poly) ###" to change kernel and degree
		if methode=='linear':
			print "Linear Method"
			clf= svm.SVC(kernel=methode, C=t1linear) ###" to change kernel and gamma
	if classe==2: ########## If NuSVC were chosen
		if methode=='rbf':
			clf= svm.NuSVC(kernel=methode, gamma=gamma, nu=Nu) ###" to change kernel and gamma
		if methode=='sigmoid':
			clf= svm.NuSVC(kernel=methode, gamma=gamma, nu=Nu) ###" to change kernel and gamma
		if methode=='poly':
			clf= svm.NuSVC(kernel=methode, degree=degre, nu=Nu) ###" to change kernel and degree
		if methode=='linear':
			clf= svm.NuSVC(kernel=methode, nu=Nu2) ###" to change kernel and gamma
	if classe==3: ########## If LinearSVC were chosen
			clf= svm.LinearSVC(C=t3linear) ##### To change the t
	if classe==4: ####RN Classifier
		 clf = MLPClassifier(solver='lbfgs', activation=methode, batch_size='auto', alpha=alpha, hidden_layer_sizes=(100,), random_state=None, tol=tol, verbose=False, warm_start=False)
	clf.fit(X_train,y_train)
	if verif==1:
		return X_test,y_test

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
	global parametres
	parametres=Toplevel()
	texteexplication="Veuillez choisir la classe de SVM : "
	textexplication=Label(parametres, text=texteexplication)
	P1 = Radiobutton(parametres, text="SVC", variable=variableparam, value=1,command=choixmethode)
	P2 = Radiobutton(parametres, text="NuSVC", variable = variableparam, value=2, command=choixmethode)
	P3 = Radiobutton(parametres, text="LinearSVC", variable=variableparam, value=3, command=choixmethode)
	P4 = Radiobutton(parametres, text="Classifier", variable=variableparam, value=4, command=choixmethode)
	textexplication.pack();P1.pack();P2.pack();P3.pack();P4.pack()
	parametres.mainloop()

def choixmethode():#### Allows to choose the classification method
	'''This function allows the user to choose between different methods in order to personalize, if he wants to, the training method
	Description:
		Here, via a TKinter window, the user will be able to choose between different methods of training methods
	Args:
	Return :
		There is no return here. It modifies the methods variable which corresponds to the method chosen by the user
	'''
	global methodes
	global classe
	global classe1
	parametres.destroy()
	classe=variableparam.get()
	if classe==1 or classe==2: #### Choice of the method in regard of SVC and NuSVC
		classe1=Toplevel()
		choixmethodes="Veuillez choisir la méthode de votre choix : "
		choixmethode=Label(classe1, text=choixmethodes)
		R1=Radiobutton(classe1, text='rbf', variable=methodes,value="rbf",command=choixhyperparametres)
		R2=Radiobutton(classe1,text='sigmoid',variable=methodes,value="sigmoid",command=choixhyperparametres)
		R3=Radiobutton(classe1, text='poly', variable=methodes, value="poly",command=choixhyperparametres)
		R4=Radiobutton(classe1, text='linear', variable=methodes, value="linear",command=choixhyperparametres)
		choixmethode.pack();R1.pack();R2.pack();R3.pack();R4.pack()
	if classe==3: # Choice of the method from LinearSVC
		choixhyperparametres()
	if classe==4: # Choice of the method in regard of neural network and the Classifier class
		classe1=Toplevel()
		choixmethodes="Quelle est la méthode réseau de neurones de votre choix"
		choixmethode=Label(classe1, text=choixmethodes)
		S1=Radiobutton(classe1, text='Relu',variable=methodes, value='relu', command=choixhyperparametres)
		S2=Radiobutton(classe1, text='Identity',variable=methodes, value='identity', command=choixhyperparametres)
		S3=Radiobutton(classe1, text='Tanh',variable=methodes, value='tanh', command=choixhyperparametres)
		S4=Radiobutton(classe1, text='Logistic',variable=methodes, value='logistic', command=choixhyperparametres)
		choixmethode.pack();S1.pack();S2.pack();S3.pack();S4.pack()

def choixhyperparametres(): #### Allow to choose the hyperparameters of the method
	'''In this function, the user is asked if he wants to adjust the hyperparameters of the chosen method
	Description :
		Here, in function of the chosen method, the user can choose between the different hyperparameters
	Args :
		No Args required.
	Return:
		There is no return here. Only the hyperparameters' variables will be modified
	'''
	# Here, vtest and gammatest are defined directly in the function and not globaly because they are used only once
	def validerhyperparam():
		global t; global gamma; global alpha; global tol; global degre; global t1poly
		global t1linear; global t3linear; global Nu; global Nu2
		t=1*10**float(ttest.get())
		gamma=1*10**float(gammatest.get())
		alpha=1*10**float(alphatest.get())
		tol = 1*10**float(toltest.get())
		degre = float(degretest.get())
		t1poly = 1*10**float(ttest1poly.get())
		t1linear = 1*10**float(ttest1linear.get())
		t3linear = 1*10**float(ttest3linear.get())
		Nu = float(Nutest.get())
		Nu2 = float(Nu2test.get())
		print alpha
		print tol
		print gamma, "testgamma"
		print t, "testt"
		choixdeshuitparametres()
		hyperparametres.destroy()
	global methode
	global hyperparametres
	methode=methodes.get()
	classe=variableparam.get()
	if classe!=3:
		classe1.destroy()
	hyperparametres=Toplevel()
	gammatest=IntVar(); alphatest=IntVar(); toltest=IntVar(); degretest=IntVar(); ttest=IntVar(); ttest1poly=IntVar()
	ttest1linear=IntVar(); ttest3linear=IntVar(); Nutest=IntVar(); Nu2test=IntVar()
	gammatest.set(-12), ttest.set(-5), toltest.set(-7), alphatest.set(-4), degretest.set(0)
	ttest1poly.set(-5), ttest1linear.set(-4), ttest3linear.set(-5), Nutest.set(0), Nu2test.set(0)
	textehyperparametres = "Veuillez regler les hyperparamètres :"
	textehyperparametres2=Label(hyperparametres,text=textehyperparametres)
	validerchoix= Button(hyperparametres, text="Valider", fg="Black",bg="SkyBlue3", command=validerhyperparam, font=helv36)
	textehyperparametres2.pack()
	if (methode=='rbf' or methode=='sigmoid') and classe==1:
		gammatest=Scale(hyperparametres, orient='horizontal', from_=-12, to=3,resolution=1, tickinterval=1, length=350,label="Choix de l'exposant de la valeur de gamma")
		ttest=Scale(hyperparametres, orient='horizontal', from_=-5, to=7, resolution=1, tickinterval=1, length=350, label="Choix de la valeur de l'exposant de C")
		gammatest.pack();ttest.pack();
	if methode=='poly' and classe==1:
		degretest=Scale(hyperparametres, orient='horizontal', from_=0, to=2, resolution=1, tickinterval=1, length=350,label='Choix de la valeur de degree')
		ttest1poly=Scale(hyperparametres, orient='horizontal', from_=-5, to=-1,resolution=1, tickinterval=1, length=350,label="Choix de l'exposant de la valeur de C")
		degretest.pack();ttest1poly.pack();
	if methode=='linear' and classe==1:
		ttest1linear=Scale(hyperparametres, orient='horizontal', from_=-4, to=3, resolution=1, tickinterval=1, length=350, label="Choix de l'exposant de la valeur de C")
		ttest1linear.pack()
	if classe==3:
		ttest3linear=Scale(hyperparametres, orient='horizontal', from_=-5, to=7, resolution=1, tickinterval=1, length=350, label='Choix de la valeur de C')
		ttest3linear.pack();
	if (methode=='rbf' or methode=='sigmoid') and classe==2:
		gammatest=Scale(hyperparametres, orient='horizontal', from_=-12, to=3, resolution=1, tickinterval=1, length=350, label="Choix de l'exposant de la valeur de gamma")
		Nutest=Scale(hyperparametres, orient='horizontal', from_=0, to=0.9, resolution=0.1, tickinterval=0.1, length=350, label='Choix de la valeur de nu')
		gammatest.pack();Nutest.pack();
	if methode=='poly' and classe==2:
		degretest=Scale(hyperparametres, orient='horizontal', from_=0, to=2, resolution=1, tickinterval=1, length=350, label='Choix de la valeur de degree')
		Nutest=Scale(hyperparametres, orient='horizontal', from_=0, to=0.9, resolution=0.1, tickinterval=0.1, length=350, label='Choix de la valeur de nu')
		degretest.pack();Nutest.pack();
	if methode=='linear' and classe==2:
		Nu2test=Scale(hyperparametres, orient='horizontal', from_=0, to=0.6, resolution=0.1, tickinterval=0.1, length=350, label='Choix de la valeur de nu')
		Nu2test.pack();
	if classe==4:
		alphatest=Scale(hyperparametres, orient='horizontal', from_=-5, to=3, resolution=1, tickinterval=1, length=350, label="Choix de la valeur de l'exposant de alpha")
		toltest=Scale(hyperparametres, orient='horizontal', from_=-7, to=2, resolution=1, tickinterval=1, length=350, label="Choix de la valeur de l'exposant de tol")
		alphatest.pack();toltest.pack()
	validerchoix.pack()
	hyperparametres.mainloop()

def choixdeshuitparametres(): #### Allow to choose the paramaters
	''' This function allows to user to choose the different paramaters to run the analyze.
	Description:
		Every button return a value between 0 and 8 corresponding of the 8 differents paramaters.
		There is also a button which return 9 if the user doesn't want to chose the paramaters. This is default value.
	Args:
		No arguments required.
	Return:
		No return only global variables are modified.
	'''
	def recuperationvaleur():
		global listeparam
		listeparam=[]
		p1=varparam.get()
		p2=varparam2.get()
		p3=varparam3.get()
		p4=varparam4.get()
		p5=varparam5.get()
		p6=varparam6.get()
		p7=varparam7.get()
		p8=varparam8.get()
		liste=[p1,p2,p3,p4,p5,p6,p7,p8]
		for i in liste:
			if i!=9:
				listeparam.append(i)
		print "Liste des paramètres : ",
		for i in listeparam:
			print listeparamcomplete[i+1],
		print'.'
		choixhuitparametres.destroy()
	global choixhuitparametres
	choixhuitparametres=Toplevel()
	varparam=IntVar();varparam2=IntVar();varparam3=IntVar();varparam4=IntVar();varparam5=IntVar();varparam6=IntVar();varparam7=IntVar();varparam8=IntVar()
	varparam.set(9);varparam2.set(9); varparam3.set(9); varparam4.set(9); varparam5.set(9); varparam6.set(9); varparam7.set(9), varparam8.set(9)
	c1 = Checkbutton(choixhuitparametres, text="IR", variable = varparam, onvalue=0, offvalue=9)
	c2 = Checkbutton(choixhuitparametres, text="RMP", variable = varparam2, onvalue=1, offvalue=9)
	c3 = Checkbutton(choixhuitparametres, text="RH", variable = varparam3, onvalue=2, offvalue=9)
	c4 = Checkbutton(choixhuitparametres, text="ST", variable = varparam4, onvalue=3, offvalue=9)
	c5 = Checkbutton(choixhuitparametres, text="DTFS", variable = varparam5, onvalue=4, offvalue=9)
	c6 = Checkbutton(choixhuitparametres, text="SA", variable = varparam6, onvalue=5, offvalue=9)
	c7 = Checkbutton(choixhuitparametres, text="SD", variable = varparam7, onvalue=6, offvalue=9)
	c8 = Checkbutton(choixhuitparametres, text="fAHP", variable = varparam8, onvalue=7, offvalue=9)
	c9 = Button(choixhuitparametres, text="Valider", command=recuperationvaleur)
	c1.pack();c2.pack();c3.pack();c4.pack();c5.pack();c6.pack();c7.pack();c8.pack();c9.pack()

def ChoixNomFichier(check):  #### Give a name to the output file
	''' This function allows to user to give a name to the output file (the results' file).
	Description:
		Here the user can enter the name of his output file.
	Args:
		No arguments here.
	Return:
		No return.
	'''
	if check=="avertissement":
		avertissement.destroy()
	def recuperationnomfichier(event):
		global nomfichiersortie
		nomfichiersortie= entrernomfichier.get()
	global nomfichiersortie
	choixnomfichier = Toplevel()
	textechoixfichier = "Veuillez choisir le nom du fichier de sortie : \n Sous la forme example.csv ou example.txt \n"
	textechoixfichier = Label(choixnomfichier, text=textechoixfichier)
	validernomfichier= Button(choixnomfichier, text="Fermer", command=choixnomfichier.destroy)
	entrernomfichier = Entry(choixnomfichier, width=30, textvariable=nomfichiersortie)
	entrernomfichier.bind("<Return>",recuperationnomfichier)
	textechoixfichier.pack();entrernomfichier.pack();validernomfichier.pack()

def Simulationentrainement():
	global simulation
	global echantillons
	if listeentrainement==[]:
		global avertissement
		print "Attention fichier d'entrainement non chargé"
		avertissement=Toplevel()
		beep(1)
		avertissement.title("Avertissement")
		txtavertissement=Label(avertissement,text="Attention il n'y a pas de fichier d'entrainement pour la simulation ou le fichier est vide. \n Veuillez chargez un fichier.")
		txtavertissement.pack()
		c="avertissement"
		A1= Button(avertissement,text="Chargement d'un fichier d'entraînement",command=lambda c=c:Chargemententrainement(c))
		A1.pack();
		avertissement.mainloop()
	else:
		simulation=Toplevel()
		textesimulation="Veuillez choisir votre méthode d'échantillonnage:\n"
		textesimulation=Label(simulation, text=textesimulation)
		echantillon1= Radiobutton(simulation, text = "50/50", variable = echantillons, value = 1,command=choixechantillons)
		echantillon2= Radiobutton(simulation, text = "25/75", variable = echantillons, value = 2, command=choixechantillons)
		echantillon3= Radiobutton(simulation, text = "75/25", variable = echantillons, value = 3, command=choixechantillons)
		textesimulation.pack();echantillon1.pack();echantillon2.pack();echantillon3.pack()
		simulation.mainloop()

def choixechantillons():
	global echantillonnage
	simulation.destroy()
	choixechantillons=Toplevel()
	choixechantillons.title="Résultats de la simulation du modèle"
	echantillonnage=echantillons.get()
	test=entrainementdufichier(1)
	result=clf.predict(test[0])
	beep(1)# Permet d'émettre un son
	x=0
	somme=0
	length=len(test[1])
	while x<len(test[1]):
		if result[x]==test[1][x]:
			somme=somme+1
		x=x+1
	percentage=(float(somme)/length)*100
	percentage=round(percentage,2)
	print percentage,"%"
	textesimulation=Label(choixechantillons, text="Le pourcentage de réussite est de :")
	textepourcentage=Label(choixechantillons, text=percentage)
	Q1= Button(choixechantillons, text= "Fermer", command= choixechantillons.destroy)
	textesimulation.pack();textepourcentage.pack();Q1.pack()
	choixechantillons.mainloop()

def save():
	#gestion d'erreur à revoir
	nomfichier=nomfichiersortie.get()
	if nomfichier=='':
		global avertissement
		print "Attention nom de fichier non défini"
		avertissement=Toplevel()
		beep(1)
		avertissement.title("Avertissement")
		txtavertissement=Label(avertissement,text="Attention le nom de fichier de sortie n'a pas été fourni. \n Veuillez entrer un nom de fichier.")
		txtavertissement.pack()
		c="avertissement"
		A1= Button(avertissement,text="Choix du nom de fichier de sortie",command=lambda c=c:ChoixNomFichier(c))
		A1.pack();
		avertissement.mainloop()
	else:
		file=codecs.open(nomfichier,"w",encoding="utf-8")
		x=0
		while x<len(resultdataset):
			y=0
			while y<len(resultdataset[x]):
				file.write(str(resultdataset[x][y]))
				file.write(',')
				y=y+1
			file.write('\n')
			x=x+1
		file.close

def addtodataset(filename):
	file=codecs.open(filename,"a",encoding="utf-8")
	i=1
	while i<len(resultdataset):
		j=0
		while j<len(resultdataset[i]):
			file.write(str(resultdataset[i][j]))
			file.write(',')
			j=j+1
		file.write('\n')
		i=i+1
	file.close
	
def modiftable():
	global Verif
	def finaladd():
		if modi!=0:
			addtodataset('TrainModel.csv')
		addtodataset('ModelG.csv')
		Verif.destroy()
	Verif=Toplevel()
	txtavertissement=Label(Verif,text="Etes-vous sûr de vouloir entraîner les modèles?")
	A1=Button(Verif, text='Oui',command=finaladd)
	A2=Button(Verif, text='Non', command=Verif.destroy)
	txtavertissement.pack();A1.pack();A2.pack();
	Verif.mainloop()

def cancel():
	shutil.copyfile('Backup_G.csv','ModelG.csv')
	shutil.copyfile('Yourbackup.csv','TrainModel.csv')

def Lanceranalyse(): #### Start the analyse of neuron classification
	''' This function allows to give the neuron's type (I or II).
	Description:
		Allows the visualization of the results as well as their graphics' representation (diagram with the number of type I and type II)
	Args:
		No Args here.
	Return:
		No return.
	'''
	global resultdataset
	global avertissement
	if listetest==[]:
		print "Attention fichier de test non chargé"
		avertissement=Toplevel()
		beep(1)
		avertissement.title("Avertissement")
		txtavertissement=Label(avertissement,text="Attention il n'y a pas de fichier de test pour l'analyse ou le fichier est vide. \n Veuillez chargez un fichier.")
		txtavertissement.pack()
		c="avertissement"
		A1= Button(avertissement,text="Chargement d'un fichier d'un fichier test",command=lambda c=c:Chargementtest(c))
		A1.pack();
		avertissement.mainloop()
		return
	if listeentrainement==[]:
		print "Attention fichier d'entrainement non chargé"
		avertissement=Toplevel()
		beep(1)
		avertissement.title("Avertissement")
		txtavertissement=Label(avertissement,text="Attention il n'y a pas de fichier d'entrainement pour l'analyse ou le fichier est vide. \n Veuillez chargez un fichier.")
		txtavertissement.pack()
		c="avertissement"
		A1= Button(avertissement,text="Chargement d'un fichier d'un fichier d'entrainement",command=lambda c=c:Chargemententrainement(c))
		A1.pack();
		avertissement.mainloop()
		return
	resultdataset=[]
	#
	def entrernom(c):
		global tmp
		test=Toplevel()
		A1= Radiobutton(test, text='1',variable=tmp, value=1,command=lambda c=c:vartest(c))
		A2= Radiobutton(test, text='2',variable=tmp, value=2,command=lambda c=c:vartest(c))
		A3= Button(test,text='Valider',command=test.destroy)
		A1.pack();A2.pack();A3.pack();
		test.mainloop()
	#
	def vartest(c):
		test=tmp.get()
		global resultdataset
		resultdataset[c][0]=test
		tmp.set(0)
		testfichier(frame)
	#
	def onFrameConfigure(canvas):
		canvas.configure(scrollregion=canvas.bbox("all"))
	#
	def testfichier(frame):
		i=0
		while i<len(resultdataset): #### i = row
			j=0
			while j<len(resultdataset[i]): #### j = column
				if j==0:
					if i==0:
						tk.Label(frame,text=resultdataset[i][j],relief=FLAT, borderwidth=1).grid(row=i,column=j,ipadx=5,ipady=4)
					if i!=0:
						Button(frame,text=resultdataset[i][j], relief=FLAT, borderwidth=1, command=lambda c=i:entrernom(c)).grid(row=i,column=j,ipadx=5,ipady=4)
				else:
					tk.Label(frame,text=resultdataset[i][j],relief=FLAT, borderwidth=1).grid(row=i,column=j,ipadx=5,ipady=4)
				j=j+1
			i=i+1
	#
	def diagram():
		namepart = ['TypeI', 'TypeII'] #### Part's name
		data = [type1, type2] #### Number of type I neurons and number of type II
		explode=(0, 0.1) #### Separation of the two parts
		plt.pie(data, explode=explode, labels=namepart, autopct='%1.1f%%', startangle=90, shadow=True) #### autopct = actual percentage compared to the one indicated
		plt.axis('equal') #### axis = Create a circular diagram
		plt.show('Test')
		'''
		name = ['TypeI', 'TypeII'] #### Part's name
		data = [type1, type2] #### Number of type I neurons and number of type II
		explode=(0, 0.2) #### Separation of the two parts
		plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True) #####autopct = actual percentage compared to the one indicated
		plt.axis('equal') #### axis = Create a circular diagram
		plt.show('Test')
		'''
		return
	#
	entrainementdufichier(0)
	Analyse=Toplevel()
	Analyse.title("Résultats de l'analyse")
	Analyse.geometry("1200x800+600+300")
	A1=Button(Analyse, text="Sauvegarder les résultats", command=save, bg="SkyBlue3")
	di1=Button(Analyse, text="Afficher le diagramme", command=diagram, bg="SkyBlue3")
	modif=Label(Analyse,text="\n Si vous souhaitez modifier les résultats, \n appuyez sur le 1 ou 2 souhaité. \n Puis choisissez le résultat attendu.\n \n Si vous souhaitez entraîner les modèles,\n cliquer sur le bouton ci-dessous,\n ATTENTION veillez à bien vérifier les résultats \n AVANT l'entraînement!",relief=FLAT,borderwidth=1)
	A2=Button(Analyse,text="Entraîner les modèles avec vos résultats",command=modiftable,bg="thistle")
	A3=Button(Analyse,text="Rétablir les modèles à l'original",command=cancel,bg="thistle")
	instruc=Label(Analyse,text="Pour charger le modèle entraîné, \n il faudra choisir le fichier d'entraînement : \n 'TrainModel.csv'.")
	canvas=tk.Canvas(Analyse,borderwidth=1)
	frame = tk.Frame(canvas)
	vsb = tk.Scrollbar(Analyse, orient="vertical", command=canvas.yview)
	canvas.configure(yscrollcommand=vsb.set)
	vsb.pack(side="right", fill="y");canvas.pack(side="left", fill="both", expand=True);A1.pack();di1.pack();modif.pack();A2.pack();A3.pack();
	canvas.create_window((4,4), window=frame, anchor="nw")
	frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
	dataset=[]
	for sample in listetest:
		s=[]
		for i in listeparam:
			s.append(sample[i])
		dataset.append(s)
	X_test=np.array(dataset)# Passage du tableau en format numpy
	result=clf.predict(X_test)####################### PREDICTION !!!!!!
	resultdataset.append(listeparamcomplete) # ajout de l'entête
	#boucle pour former le tableau à 2D final
	d=0
	while d<len(result):
		sample=[]
		sample.append(result[d])
		k=0
		while k<len(listetest[d]):
			sample.append(listetest[d][k])
			k=k+1
		resultdataset.append(sample)
		d=d+1
	beep(1)# Permet d'émettre un son
	testfichier(frame)
	type1=0
	type2=0
	for i in result:
		if i==1:
			type1=type1+1 #### Counter to find out the number of type I neurons
		if i==2:
			type2=type2+1 #### Counter to find out the number of type II neurons
	print "Analyse terminée"
	Analyse.mainloop()

def presentation(): #### Presentation of the project's group
	''' This function allows to present the project's group.
	Args:
		No arguments.
	Return:
		No return.
	'''
	presentation=Toplevel()
	presentation.title("Presentation")
	presentation.geometry("800x600+600+300")
	textepresentation="Actuellement etudiant en master I à l'Université de Bordeaux,\n nous avons pour projet de classer des neurones en deux types : Type I et Type II.\n Les données electrophysiologiques vont être la source de classification.\n 8 paramètres sont donc retenus : IR,RMP,RH,SD,DTFS,SA,SD,fAHP \n"
	text=Label(presentation,text=textepresentation)
	text.pack()
	presentation.mainloop()

def explicationlogiciel(): ###### Explications of the software
	explication=Toplevel()
	explication.title("Le logiciel")
	explication.geometry("1000x500+600+300")
	texteexplication="Présentation du logiciel : \n"
	text=Label(explication, text=texteexplication)
	text.pack()
	explication.mainloop()

###############################################################    MAIN    ###############################################################
b1= Button(app, text= "Ajustement des paramètres", fg= "Black",bg= "SkyBlue3", command= ChoixClasseparam, font= helv36, bd= 4)
b2= Button(app, text= "Chargement du fichier d'entraînement", fg= "Black", bg= "SkyBlue3", command=lambda c='':Chargemententrainement(c), font= helv36, bd= 4)
b3= Button(app, text= "Lancer la simulation", fg= "Black", bg= "SkyBlue3", command= Simulationentrainement, font= helv36, bd= 4)
b4= Button(app, text= "Chargement du fichier à analyser",fg= "Black", bg= "SkyBlue3", command=lambda c='':Chargementtest(c), font= helv36, bd= 4)
b5= Button(app, text= "Choisir le nom du fichier de sortie", fg= "Black", bg= "SkyBlue3", command=lambda c='':ChoixNomFichier(c), font= helv36, bd= 4)
b6= Button(app, text= "Lancer l'analyse", fg= "Black",bg= "SkyBlue3", command= Lanceranalyse, font= helv36, bd= 4)
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
b6.place(x=350, y=470, width=150, height=60)
b7.place(x=350, y=540, width=150, height=30)
text.place(x=180, y=0, width=500, height=50)

#####################################    Toolbar
####   Menu 1
menu1.add_separator()
menu1.add_command(label="Ouvrir un fichier test", command=lambda c='':Chargementtest(c))
menu1.add_separator()
menu1.add_command(label="Ouvrir un fichier d'entrainement", command=lambda c='':Chargemententrainement(c))
menu1.add_separator()
menu1.add_command(label="Enregistrer le projet en cours", command=lambda c='':Chargemententrainement(c))#####Save the project
menu1.add_separator()
menubar.add_cascade(label="Fichier", menu=menu1) ###### Name on the toolbar

####   Menu 2
menu2.add_separator()
menu2.add_command(label="Regler les paramètres", command=ChoixClasseparam)
menu2.add_separator()
menubar.add_cascade(label="Option", menu=menu2)

####   Menu 3
menu3.add_separator()
menu3.add_command(label="Qui sommes nous?", command=presentation)
menu3.add_separator()
menu3.add_command(label="Explication du logiciel", command=explicationlogiciel)
menu3.add_separator()
menubar.add_cascade(label="Aide", menu=menu3)

####   Toolbar/tools
app.config(menu=menubar)
app.mainloop()
