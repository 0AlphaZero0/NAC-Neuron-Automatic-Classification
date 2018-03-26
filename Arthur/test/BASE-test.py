#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Projet de programmation Python - Virus killer
# BLAIS Benjamin
# COTTAIS Déborah
# DE OLIVEIRA Lila
# JOUAN Clément
# THOUVENIN Arthur
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
def ID(donnees):#ajoute un ID au neurone compteur de chiffre de 1 à len(donnees)
	'''	Cette fonction permet d'ajouter un identifiant au neurone
	Description:
		Ici un simple compteur va ajouter un ID dans le tableau à deux dimensions demandé en entrée
	Args:
		Un tableau à deux dimensions
	Return:
		Retourne le tableau à deux dimension avec l'ajout d'un ID à chaque sample
	'''
	x=0
	while x<len(donnees):
		donnees[x].append(x)
		x=x+1
	return donnees
#
########################################     MAIN     ######################################
y_train=[]
y_test=[]
train=[]
test=[]
x=0
fichier=raw_input("\nEntrer le nom du fichier : \n")
DATA= load(fichier)
print "\n Le fichier fait",len(DATA),"samples.\n"

##### need to split data  #####
for i in DATA:
	if x%2==0:
		train.append(i)
	else:
		test.append(i)
	x=x+1
####### séparation train ######
for i in train:
	y_train.append(i.pop(0))
####### spéaration test #######
for i in test:
	y_test.append(i.pop(0))
################################
#
#
# ICI JE DOIS FAIRE EN SORTE DE SELECTIONNER LES COMBINAISONS DE PARAMETRES DANS TRAIN ET TEST
#
#
################################
X_test = np.array(test)
X_train = np.array(train)
t=10
first=1
a=0
top=0
while top==0:
	clf = svm.SVC(kernel='linear', C = t)
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
	print percentage,"% pour un C=",t
	if first==0:
		if tmp==percentage:
			a=a+1
			if a==4:
				print "BROKE"
				first =1
				t=10
				break
		else:
			a=0
	tmp=percentage
	first=0
	t=t*0.1