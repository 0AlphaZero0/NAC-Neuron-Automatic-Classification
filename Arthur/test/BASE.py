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

########################################     MAIN     ######################################
y_train=[]
y_test=[]
train=[]
test=[]
x=0
DATA= load_csv("donnees.csv")
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
X_train = np.array(train)
####### spéaration test #######
for i in test:
	y_test.append(i.pop(0))
X_test = np.array(test)
################################
clf = svm.SVC(kernel='linear', C = 1.0)
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
print y_test
print result
percentage=(float(somme)/length)*100
print percentage