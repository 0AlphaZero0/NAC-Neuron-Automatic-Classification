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
from sklearn.neural_network import MLPClassifier
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
def save(percentage,t,vf,ft):
	file=codecs.open("result50train-50test-lbfgs-identity-tol.csv","a",encoding="utf-8")
	file.write(str(percentage))
	file.write(',')
	file.write(str(t))
	file.write(',')
	file.write(str(h))
	file.write(',')
	file.write(str(vf))
	file.write(',')
	for i in ft:
		file.write(str(i))
		file.write(',')
	file.write('\n')
	file.close



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
	'''=0
	datalength=len(dataset)
	while g!=len(dataset):
		top=len(dataset)-1
		rand=random.randint(0,top)
		if datalength/4<len(dataset):
			train.append(dataset.pop(rand))
			on met 75% ici
		else:
			test.append(dataset.pop(0))
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
	top=0
	tour = 0
	while top==0:
		tour = 0
		vf = 0
		h=1
		if t==10000:
			print 'BROKE'
			break
		while top==0:
			MLPClassifier(activation='identity', alpha=t, batch_size='auto', hidden_layer_sizes=(100,), random_state=None, tol=h, validation_fraction=vf, verbose=False, warm_start=False)
			clf = MLPClassifier(solver='lbfgs', alpha=t, hidden_layer_sizes=(100,), random_state=None)
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
			print percentage,"	% et un alpha=",t, "et un tol=", h,	"validation fraction=", vf, "ainsi que les paramètres : ",
			listftsave=[]
			for j in combin:
				if j==combin[len(combin)-1]:
					listftsave.append(features[j])
					print features[j]
					break
				listftsave.append(features[j])
				print features[j]
			save(percentage,t,vf,listftsave)
			if tour==9:
				print 'BROKE'
				break
			tour=tour+1
			h=h*10
			vf=vf+0.1
		tmp=percentage
		t=t*10



