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
size=raw_input("\nEntrer la taille dela combinaison : \n")
tmp=size
maxi=0
while i<len(dataset-1):
    if i==size-1:
        listcombin.append(dataset[i][2:9])
    if i==size:
        moy=somme/size
        listmoy.append(moy)
        listmaxi.append(maxi)
        maxi=0
        somme=0
        size=size+tmp
    if dataset[i][0]>maxi:
        maxi=dataset[i][0]
    somme = somme+dataset[i][0]
    i=i+1

file=codecs.open("save.csv","w",encoding="utf-8")
x=0
while x < len(listcombin):
    file.write(listcombin[x])
    file.write(';')
    file.write(listmaxi[x])
    file.write(';')
    file.write(listcombin[x])
    x=x+1