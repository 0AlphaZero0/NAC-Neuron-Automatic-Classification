#!/usr/bin/env python
#-*- coding: utf-8 -*-
# THOUVENIN Arthur
########################
import sys
import os
import random
import codecs
########################################   VARIABLES   ######################################
i=1
dataset=[]
finaldataset=[]
count=0
########################################   FONCTIONS   ######################################
def load(filename): # load le fichier
	''' Cette fonction permet de charger le fichier dans le script
	Description:
		Ici on convertit le fichier en un tableau que l'on retourne pour le réutiliser,
	Args:
		C'est le nom du fichier qui est demandé en entrée
	Return:
		On retourne ici une liste à deux dimension
	'''
	global count
	dataset=[]
	try:
		file = codecs.open(filename, "r",encoding="utf-8")
		count=count+1
	except IOError:
		print "AVERTISSEMENT : Nom de fichier éroné!!!"
		return
	for line in file.readlines():
		if not line:
			break
		if line and line[0].isalpha():
			pass
		else:
			y=line.split(',')
			y[0]=float(y[0])
			dataset.append(y)
	return dataset
########################################   MAIN   ######################################
while i!=0:
	os.system("clear")
	print "Veuillez entrer un nom de fichier à additionner"
	print "Entrez 0 pour quitter"
	choice=raw_input("")
	if choice=="0":
		moy=[]
		for i in dataset:
			y=[]
			for j in i:
				y.append(j[0])
			moy.append(y)
		#faire les moyenne et tout mettre dans le final dataset ou juste remplacer dans le premier dataset
		break
	explo=load(choice)
	dataset.append(explo)
print dataset