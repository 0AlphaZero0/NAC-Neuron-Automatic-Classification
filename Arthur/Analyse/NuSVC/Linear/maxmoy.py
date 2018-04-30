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
size=size-1
maxi=0
print len(dataset)
while i<len(dataset):
    if dataset[i][0]>maxi:
        maxi=dataset[i][0]
    if i==size:
        listcombin.append(dataset[i][2:-1])
        somme=somme+float(dataset[i][0])
        moy=somme/tmp
        print moy, "MOY"
        listmoy.append(moy)
        listmaxi.append(maxi)
        print maxi, "MAX"
        print (size+1)/tmp
        #print i
        #print dataset[i][0]
        #print size
        maxi=0
        somme=0
        size=size+tmp
        if size>len(dataset)-1:
            print "FIN"
            break
        i=i+1
        pass
    somme = somme+float(dataset[i][0])
    i=i+1

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