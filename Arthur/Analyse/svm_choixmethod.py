#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Projet de programmation Neuro
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
import urllib
import matplotlib.pyplot as plt
import numpy as np
#######################
# from http://scikit-learn.org/stable/auto_examples/exercises/plot_iris_exercise.html
# details here : http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
from csv import reader
from sklearn import datasets, svm
from pylab import *

########################################   FONCTIONS  ######################################
# features = 0:nClass 1:IR 2:RMP 3:RH 4:ST 5:DTFS 6:SA 7:SD 8:fAHP 9:ID
# Load a CSV file
def load_csv(filename): # load le fichier
	dataset=[]
	file = codecs.open(filename, "r",encoding="utf-8")
	for line in file.readlines():
		if not line:
			break
		y=line.split(',')
		y[0]=int(y[0])
		x=1
		while x<len(y):
			y[x]=float(y[x])
			x=x+1
		dataset.append(y)
	return dataset

def ID(donnees):#ajoute un ID au neurone compteur de chiffre de 1 à len(donnees)
	x=0
	while x<len(donnees):
		donnees[x].append(x)
		x=x+1
	return donnees

def nouvelle_liste(): #permet de sélectionner les features que l'on souhaite
	global donneesx
	global donneesy
	global donnees
	i = 0
	while i < len(donnees):
		donneesx.append(donnees[i][0])
		donneesy.append(donnees[i][1])
		i=i+1

	return donneesx, donneesy

def visualise_data(donneesx,donneesy):
	donnees = load_csv("CR.csv")
	x = donneesx
	y = donneesy
	plt.scatter(x,y,c=y, cmap=plt.cm.coolwarm)
	plt.xlabel('nClass')
	plt.ylabel('IR')
	plt.title('nClass & IR')
	plt.show()

def reformedata():
	global donnees
	global donneesx
	global donneesy
	#Y
	donneesy=donneesx#en y c'est la target
	donneesy=np.array(donneesy)
	donneesy=donneesy.reshape((116, 1))
	donneesy=np.ravel(donneesy)
	#X
	donneesx=[t[1:9]for t in donnees]
	donneesx=np.array(donneesx)#on sélectionne tout les features
	donneesx=donneesx.reshape((116, 8))

######################################      MAIN      ###########################################
######## VARIABLES
donneesx=[]
donneesy=[]
features= ['nClass','IR','RMP','RH','ST','DTFS','SA','SD','fAHP','ID']
C = 1.0  # SVM regularization parameter
h = .02  # step size in the mesh
titles = ['SVC with linear kernel','LinearSVC (linear kernel)','SVC with RBF kernel','SVC with polynomial (degree 3) kernel']# title for the plots
n_sample=116
kern=["linear", "rbf", "poly"]
fracRange=np.arange(0.1,0.9,0.01)
res=""
bestScore=0
bestRes=""
linScores=[]
rbfScores=[]
polScores=[]
###################################
donnees = load_csv("CR.csv")
donnees = ID(donnees)
r=nouvelle_liste()
donneesx= r[0]
donneesy= r[1]
visualise_data(donneesx,donneesy)
reformedata()
np.random.seed(0)
order=np.random.permutation(n_sample)
x=donneesx[order]
y=donneesy[order]


for tFrac in fracRange:
	#print tFrac
	X_train = x[:int(tFrac * n_sample)]
	y_train = y[:int(tFrac * n_sample)]
	X_test = x[int(tFrac * n_sample):]
	y_test = y[int(tFrac * n_sample):]
	res+=str("Training fraction : "+str(tFrac)+"\n")
	for k in kern:
		clf = svm.SVC(kernel=k)
		clf.fit(X_train, y_train)
		predicted = clf.predict(X_test)
		score=sum(predicted==y_test)/float(len(predicted))
		res+="\t"+k+" : "+str(score)+"\n"
		if k=="linear":
			linScores.append(score)
		if k=="rbf":
			rbfScores.append(score)
		if k=="poly":
			polScores.append(score)
		if score>bestScore:
			bestScore=score
			bestRes="Fraction = "+str(tFrac)+", method="+k+", results="+str(score)

print bestRes
plot(fracRange,linScores)
plot(fracRange,rbfScores)
plot(fracRange,polScores)
legend(kern)
show()