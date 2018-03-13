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
import numpy as np
import matplotlib.pyplot as plt
import urllib


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
donneesx=[]
donneesy=[]
features= ['nClass','IR','RMP','RH','ST','DTFS','SA','SD','fAHP','ID']
C = 1.0  # SVM regularization parameter
h = .02  # step size in the mesh
titles = ['SVC with linear kernel','LinearSVC (linear kernel)','SVC with RBF kernel','SVC with polynomial (degree 3) kernel']# title for the plots
#print load_csv("CR.csv")
donnees = load_csv("CR.csv")
donnees = ID(donnees)
r=nouvelle_liste()
donneesx= r[0]
donneesy= r[1]
visualise_data(donneesx,donneesy)
reformedata()
# SVC with linear kernel
svc = svm.SVC(kernel='linear',C=C).fit(donneesx, donneesy)
# LinearSVC (linear kernel)
lin_svc = svm.LinearSVC(C=C).fit(donneesx, donneesy)
# SVC with RBF kernel
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(donneesx, donneesy)
# SVC with polynomial (degree 3) kernel
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(donneesx, donneesy)
x_min,x_max=donneesx.min()-1,donneesx.max()+1
y_min,y_max=donneesy.min()-1,donneesy.max()+1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h))
#################CLEAN####################
for i, clf in enumerate((svc, lin_svc, rbf_svc, poly_svc)):
	 # Plot the decision boundary. For that, we will assign a color to each
	 # point in the mesh [x_min, x_max]x[y_min, y_max].
	 plt.subplot(2, 2, i + 1)
	 plt.subplots_adjust(wspace=0.4, hspace=0.4)
	 
	 Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])#pose pb comprends pas trop pk - 2 features au lieu de 8
	 
	 '''# Put the result into a color plot
	 Z = Z.reshape(xx.shape)
	 plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
	 # Plot also the training points
	 plt.scatter(donneesx[:, 0], donneesy[:, 1], c=y, cmap=plt.cm.coolwarm)
	 plt.xlabel('IR')
	 plt.ylabel('RMP')
	 plt.xlim(xx.min(), xx.max())
	 plt.ylim(yy.min(), yy.max())
	 plt.xticks(())
	 plt.yticks(())
	 plt.title(titles[i])
'''
plt.show()





"""
#donnees = np.reshape(1, -1)
#(-1,1) => une seule dimension ; pour plusieurs (1,-1)
C = 1.0
#donneesy = donneesy.reshape(1,-1)
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(donneesx, donneesy)
"""

