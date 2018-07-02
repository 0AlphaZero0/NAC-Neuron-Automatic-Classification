#!/usr/bin/env python
#-*- coding: utf-8 -*-
# THOUVENIN Arthur
########################
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
			y=line.split('	')
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
	file=codecs.open("resultECH175train-25test-linear2.csv","a",encoding="utf-8")
	file.write(str(percentage))
	file.write(',')
	file.write(str(t))
	file.write(',')
	for i in ft:
		file.write(str(i))
		file.write(',')
	file.write('\n')
	file.close
#
def equalize(tmp,dataset,typ):
	while tmp>0:
		rand=random.randint(0,len(dataset)-1)
		if dataset[rand][0]==typ:
			dataset.pop(rand)
			tmp=tmp-1
	return dataset
#
def countype(dataset):
	typeone=0
	for i in dataset:
		if i[0]==1:
			typeone=typeone+1
	typetwo=len(dataset)-typeone
	return typeone,typetwo
#
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
	typeof=countype(dataset)
	typeone=typeof[0]
	typetwo=typeof[1]
	if typetwo>typeone:
		tmp=typetwo-typeone
		dataset=equalize(tmp,dataset,2)
	if typeone>typetwo:
		tmp=typeone-typetwo
		dataset=equalize(tmp,dataset,1)
	g=0
	datalength=len(dataset)
	while g!=len(dataset):
		top=len(dataset)-1
		rand=random.randint(0,top)
		if datalength/4<len(dataset):
			if len(dataset)%2==0 and dataset[rand][0]==1 or len(dataset)%2!=0 and dataset[rand][0]==2:
				train.append(dataset.pop(rand))
			else:
				top=top+1
				pass
			#on met 75% ici
		else:
			test.append(dataset.pop(0))
			#on met 25% ici
	typeof=countype(test)
	typeone=typeof[0]
	typetwo=typeof[1]
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
		print "Origina",y_test
		print "Prédict",result
		print "TYPE 1 = ",typeone
		print "TYPE 2 = ",typetwo
		print "TRAIN = ",len(train)
		print "TEST = ",len(test)
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
		
		
