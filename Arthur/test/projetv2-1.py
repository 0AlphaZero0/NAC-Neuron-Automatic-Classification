#!/usr/bin/env python
#-*- coding: utf-8 -*-
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
from Tkinter import *
import tkFileDialog  ##Permet de Charger les fichiers
from matplotlib.figure import * #Importe les parametres de matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #Importe tkinter
import matplotlib.pyplot as plt
import subprocess ### Ouvre un script present dans le repertoire courant

#####Fenetre principale
app = Tk()
app.title("Classification neuronale") # donne un titre à la fenêtre
app.geometry("800x600+600+300") # place la fenêtre
app.configure(background='blue')#fond du programme


############# Variables
variableatester=IntVar()


########################################   FONCTIONS   ######################################
# features = 0:nClass 1:IR 2:RMP 3:RH 4:ST 5:DTFS 6:SA 7:SD 8:fAHP 9:ID
def load(filename): # load le fichier
	''' Cette fonction permet de charger le fichier dans le script
	Description:
		Ici on convertit le fichier en un tableau que l'on retourne pour le réutiliser,
		il faut faire attention cependant on considère ici que la première colonne contient la classe du neurone
	Args:
		C'est le nom du fichier qui est demandé en entrée
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
		else:
			y=line.split(',')
			y[0]=int(y[0])
			x=1
			while x<len(y):
				y[x]=float(y[x])
				x=x+1
			dataset.append(y)
	return dataset
#
def combinaisons(a):
    def fn(n,src,got,all):
        if n==0:
            if len(got)>0:
                all.append(got)
            return
        j=0
        while j<len(src):
            fn(n-1, src[:j], [src[j]] + got, all)
            j=j+1
        return
    all=[]
    i=0
    while i<len(a):
        fn(i,a,[],all)
        i=i+1
    all.append(a)
    return all #a=[1,2,3,4] print(combinaisons(a))
#
def save(percentage,t,ft):
	file=codecs.open("result25train-75test-linear2.csv","a",encoding="utf-8")
	file.write(str(percentage))
	file.write(',')
	file.write(str(t))
	file.write(',')
	for i in ft:
		file.write(str(i))
		file.write(',')
	file.write('\n')
	file.close

 # coding: utf-8



######Definitions


def Chargementtest(): #### Permet de retourner le chemin absolue permet l'acces au fichier
	name = tkFileDialog.askopenfilename(initialdir = "/",title = "Selection du fichier test",filetypes = (("Fichier csv","*.csv"),("Fichier texte","*.txt")))
	print (name)
	return (name) #Retourne le chemin absolue du fichier
	


######Recuperer cette putain d'entrée<<<<<<<<<<<<<<<<

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
	variable2=variableatester.get()
	if variable2==1:
	#if (variableatester.get())==1:
			nameentrainement=tkFileDialog.askopenfilename(initialdir = "/",title = "Selection du fichier entrainement",filetypes = (("Fichier csv","*.csv"),("Fichier texte","*.txt")))
			print (nameentrainement)
			return (nameentrainement)
	if variable2==2:
			nomentrainement=()####Chemin de notre fichier test


	#text1=Label(entrainement,text="Choisir le fichier d'entraînement",fg="black",bg="white")

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

def Lanceranalyse(fichier):
	listecombin=[1,2,3,4,5,6,7,8]
	features = ['nClass','IR','RMP','RH','ST','DTFS','SA','SD','fAHP']
	DATA= load(fichier)
	print "\n Le fichier fait",len(DATA),"samples.\n"
	all_combin=combinaisons(listecombin)
	for combin in all_combin:
		dataset=[]
		y_train=[]
		y_test=[]
		train=[]
		test=[]
		x=0
		for sample in DATA:
			u=[]
			u.append(sample[0])
			for j in combin:
				u.append(sample[j])
			dataset.append(u)
		##### need to split data  #####
		#les échantillons ne sont pas mélangés dans dataset donc besoin de random
		g=0
		datalength=len(dataset)
		while g!=len(dataset):
			top=len(dataset)-1
			rand=random.randint(0,top)
			if datalength/4<len(dataset):
				test.append(dataset.pop(rand))
				#on met 75% ici
			else:
				train.append(dataset.pop(0))
				#on met 25% ici
		print "TRAIN = ",len(train)
		print "TEST = ",len(test)
		'''
		#print dataset
		for i in dataset:
			if x%2==0:
				train.append(i)
			else:
				test.append(i)
			x=x+1
		'''
		####### séparation train ######
		for i in train:
			y_train.append(i.pop(0))
		####### spéaration test #######
		for i in test:
			y_test.append(i.pop(0))
		################################
		X_test = np.array(test)
		X_train = np.array(train)
		t=0.00001
		first=1
		a=0
		top=0
		while top==0:
			if t==100000000:
				print 'BROKE'
				break
			clf = svm.LinearSVC(C = t)
			clf.fit(X_train,y_train)
			################################
			result=clf.predict(X_test)
			################################
			y_test=np.array(y_test)
			x=0
			somme=0
			length=len(y_test)
			while x<len(y_test):
				if result[x]==y_test[x]:
					somme=somme+1
				x=x+1
			percentage=(float(somme)/length)*100
			print percentage,"% pour un C=",t,"ainsi que les paramètres : ",
			listftsave=[]
			for j in combin:
				if j==combin[len(combin)-1]:
					listftsave.append(features[j])
					print features[j]
					break
				listftsave.append(features[j])
				print features[j],
			save(percentage,t,listftsave)
			if first==0:
				if tmp==percentage:
					a=a+1
					if a==8:
						print "BROKE"
						break
				else:
					a=0
			tmp=percentage
			first=0
			t=t*10
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
text=Label(app, text="Classification Neuronale", fg="White", bg="Grey")   #####Mettre en gras et en gros (titre)
b1= Button(app, text="Chargement du fichier test",fg="Black", bg="Purple", command=Chargementtest, width=25)
b2= Button(app, text="Choisir le fichier d'entraînement", fg="Black", bg="White", command=Chargemententrainement,width=25)
b3= Button(app, text="Paramètres", fg="Black",bg="White", command=Parametres,width=25)
b4= Button(app, text="Lancer", fg="Black",bg="White", command=Lanceranalyse(name))
b5= Button(app, text="Quitter", fg="Black",bg="White", command=app.destroy,width=10)
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







	
########################################     MAIN     ######################################
listecombin=[1,2,3,4,5,6,7,8]
features = ['nClass','IR','RMP','RH','ST','DTFS','SA','SD','fAHP']
fichier=raw_input("\nEntrer le nom du fichier : \n")
DATA= load(fichier)
print "\n Le fichier fait",len(DATA),"samples.\n"
all_combin=combinaisons(listecombin)
for combin in all_combin:
	dataset=[]
	y_train=[]
	y_test=[]
	train=[]
	test=[]
	x=0
	for sample in DATA:
		u=[]
		u.append(sample[0])
		for j in combin:
			u.append(sample[j])
		dataset.append(u)
	##### need to split data  #####
	#les échantillons ne sont pas mélangés dans dataset donc besoin de random
	g=0
	datalength=len(dataset)
	while g!=len(dataset):
		top=len(dataset)-1
		rand=random.randint(0,top)
		if datalength/4<len(dataset):
			test.append(dataset.pop(rand))
			#on met 75% ici
		else:
			train.append(dataset.pop(0))
			#on met 25% ici
	print "TRAIN = ",len(train)
	print "TEST = ",len(test)
	'''
	#print dataset
	for i in dataset:
		if x%2==0:
			train.append(i)
		else:
			test.append(i)
		x=x+1
	'''
	####### séparation train ######
	for i in train:
		y_train.append(i.pop(0))
	####### spéaration test #######
	for i in test:
		y_test.append(i.pop(0))
	################################
	X_test = np.array(test)
	X_train = np.array(train)
	t=0.00001
	first=1
	a=0
	top=0
	while top==0:
		if t==100000000:
			print 'BROKE'
			break
		clf = svm.LinearSVC(C = t)
		clf.fit(X_train,y_train)
		################################
		result=clf.predict(X_test)
		################################
		y_test=np.array(y_test)
		x=0
		somme=0
		length=len(y_test)
		while x<len(y_test):
			if result[x]==y_test[x]:
				somme=somme+1
			x=x+1
		percentage=(float(somme)/length)*100
		print percentage,"% pour un C=",t,"ainsi que les paramètres : ",
		listftsave=[]
		for j in combin:
			if j==combin[len(combin)-1]:
				listftsave.append(features[j])
				print features[j]
				break
			listftsave.append(features[j])
			print features[j],
		save(percentage,t,listftsave)
		if first==0:
			if tmp==percentage:
				a=a+1
				if a==8:
					print "BROKE"
					break
			else:
				a=0
		tmp=percentage
		first=0
		t=t*10
		
		
