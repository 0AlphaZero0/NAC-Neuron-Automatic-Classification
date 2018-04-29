#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import os
import random
import codecs

filename=raw_input("\nEntrer le nom du fichier : \n")
dataset=[]
file=codecs.open(filename,"r",encoding="utf-8")
for line in file.readlines():
    if not line:
        break
    else:
        y=line.split(',')
        dataset.append(y)
i=0
somme = 0
listmoy=[]
listcombin=[]
listmaxi=[]
size=input("\nEntrer la taille de la combinaison : \n")
tmp=size
maxi=0
while i<len(dataset):
    if i==(size-1):
        listcombin.append(dataset[i][2:9])
    if dataset[i][0]>maxi:
        maxi=dataset[i][0]
    if i==(size-1):
        somme=somme+float(dataset[i][0])
        moy=somme/tmp
        listmoy.append(moy)
        listmaxi.append(maxi)
        print maxi
        maxi=0
        somme=0
        size=size+tmp
        i=i+1
        pass
    somme = somme+float(dataset[i][0])
    i=i+1

#print listmaxi
file=codecs.open("saveech1.csv","w",encoding="utf-8")
x=0
while x < len(listcombin):
    file.write(str(listmoy[x]))
    file.write(';')
    file.write(listmaxi[x])
    file.write(';')
    for i in listcombin[x]:
        file.write(i)
        file.write('-')
    file.write(';')
    x=x+1