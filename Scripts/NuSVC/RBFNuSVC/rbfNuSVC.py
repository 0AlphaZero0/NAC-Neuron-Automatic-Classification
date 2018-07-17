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
def load(filename): # load file
	''' Cette fonction permet de charger le fichier dans le script
	Description:
		Ici on convertit le fichier en un tableau que l'on retourne pour le reutiliser,
		il faut faire attention cependant on considere ici que la premiere colonne contient la classe du neurone
	Args:
		C'est le nom du fichier qui est demande en entree
	Return:
		On retourne ici une liste a deux dimension, ce qui est tres utile pour la conversion en array numpy
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
for combin in all_combin:# choose the good combination 
    SET=[]
    for sample in DATA: # create dataset with each combinaisons
        u=[]
        u.append(sample[0])
        for j in combin:
            u.append(sample[j])
        SET.append(u)
	####    EQUALIZE    ####
    typeof=countype(SET)
    typeone,typetwo=typeof[0],typeof[1]
    if typetwo>typeone:
        tmp=typetwo-typeone
        SET=equalize(tmp,SET,2)
    if typeone>typetwo:
        tmp=typeone-typetwo
        SET=equalize(tmp,SET,1)
    t=0.1
    while t<0.5: # first hyperparam
		h=10**-12
		while h<1000:# second hyperparam
			k,g,TMP=5,0,0
			meanperc=[]
			while k>0:# mean stabilisation
				dataset=[x[:] for x in SET] # copy a clean version of SET in dataset
				y_test=[]
				y_train=[]
				train=[]
				test=[]
				datalength=len(dataset)
				'''
				print SET[0],"SET",id(SET)
				print dataset[0],"dataset", id(dataset)
				print "train",id(train)
				print "test",id(test)
				'''
				while g!=len(dataset):# random selection for train and test
					top=len(dataset)-1
					rand=random.randint(0,top)
					if datalength/4<len(dataset):
						if len(dataset)%2==0 and dataset[rand][0]==1 or len(dataset)%2!=0 and dataset[rand][0]==2:
							train.append(dataset.pop(rand)) #75%
						else:
							top=top+1
					else:
						test.append(dataset.pop(0)) #25%
				typeof=countype(test)
				typeone,typetwo=typeof[0],typeof[1]
				for i in train: #split train
					y_train.append(i.pop(0))
				for i in test:# split test
					y_test.append(i.pop(0))
				X_test=np.array(test)
				X_train=np.array(train)
				clf=svm.NuSVC(kernel='rbf',gamma=h,nu=t)### MODEL CREATION
				clf.fit(X_train,y_train)
				result=clf.predict(X_test)
				y_test=np.array(y_test)
				somme,x=0,0
				while x<len(y_test):# percentage of this turn go in meanperc[]
					if result[x]==y_test[x]:
						somme=somme+1
					x=x+1
				percentage=(float(somme)/len(y_test))*100
				meanperc.append(percentage)
				summean=0
				for i in meanperc:# mean of all percentage => comparison with precedent mean
					summean=summean+i
				MEAN=summean/len(meanperc)
				"""
				print MEAN,"%"
				"""
				if k==1 and round(MEAN,2)!=round(TMP,2):# PRECISION OF ANALYSE HERE ROUNDED TO XX.xx | if there previous mean (TMP) != actual mean (MEAN) so there is a new turn added
					k=k+1
				TMP=MEAN
				k=k-1
			print "Original ",y_test,"\n","Prediction   ",result,"\n","TYPE 1 = ",typeone,"\n","TYPE 2 = ",typetwo,"\n","TRAIN = ",len(train),"\n","TEST = ",len(test)
			print MEAN,"% pour un C=",t,"ainsi que les parametres : ",
			listftsave=[]
			for j in combin:#save correct param, hyperparam, mean in file
				if j==combin[len(combin)-1]:
					listftsave.append(features[j])
					print features[j]
					break
				listftsave.append(features[j])
				print features[j],
			save(MEAN,t,listftsave)
			h=h*10
		t=t+0.1