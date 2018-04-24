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
while i<(len(dataset)):
    print i
    if i==(size-1):
        listcombin.append(dataset[i][3:-1])
    if dataset[i][0]>maxi:
        maxi=dataset[i][0]
    if i+1==size:
        moy=somme/tmp
        listmoy.append(moy)
        listmaxi.append(maxi)
        print len(listmoy),'moy'
        print len(listmaxi),'max'
        maxi=0
        somme=0
        size=size+tmp
        pass
    somme = somme+float(dataset[i][0])
    i=i+1
print len(dataset),'taille'
file=codecs.open("save.csv","w",encoding="utf-8")
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
    file.write('\n')
    x=x+1