#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import Tkinter

fenetre =Tk()
tmp=IntVar()

dataset=[['test',2,3],[4,5,6],[7,8,9]]

def entrernom(c):
	global dataset
	global tmp
	test=Toplevel()
	A1= Radiobutton(test, text='1',variable=tmp, value=1,command=lambda c=c:vartest(c))
	A2= Radiobutton(test, text='2',variable=tmp, value=2,command=lambda c=c:vartest(c))
	A3= Button(test,text='Valider',command=test.destroy)
	A1.pack();A2.pack();A3.pack();

def vartest(c):
	test=tmp.get()
	global dataset
	print test
	dataset[c][0]=test
	testfichier()


def testfichier():
	i=0
	a=0
	while i<len(dataset):# i = ligne
		j=0
		while j<len(dataset[i]):# j = colonne
			if j==0:
				Button(fenetre,text=dataset[i][j], relief=FLAT, borderwidth=1, command=lambda c=i:entrernom(c)).grid(row=i,column=j,ipadx=5,ipady=5)
			else:
				Tkinter.Label(fenetre,text=dataset[i][j],relief=FLAT, borderwidth=1).grid(row=i,column=j,ipadx=5,ipady=5)
				#Button(fenetre,text=dataset[i][j], relief=FLAT, borderwidth=1).grid(row=i,column=j,ipadx=5,ipady=5)
			j=j+1
		i=i+1

testfichier()
fenetre.mainloop()

print dataset
