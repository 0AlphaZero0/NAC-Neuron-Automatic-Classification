from sklearn import datasets
from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt


import urllib

from csv import reader

# Load a CSV file
def load_csv(filename):
	file = open(filename, "r")
	lines = reader(file)
	dataset = list(lines)
	return dataset



titles = ['nClass','IR', 'RMP', 'RH', 'ST', 'DTFS', 'SA', 'SD', 'fAHP']

donnees = load_csv("CR.csv")
#print donnees_dataset

donneesx = []
donneesy = []


donnees.values.reshape(-1,1)

def nouvelle_liste():
	global donneesx
	global donneesy
	global donnees
	i = 0
	while i < 116:
		donneesx.append(donnees[i][0])
		donneesy.append(donnees[i][1])
		i+=1

	return donneesx, donneesy

print nouvelle_liste()

def visualise_data(donnesx,donnesy):
	donnees = load_csv("CR.csv")
	x = donneesx
	y = donneesy
	plt.scatter(x,y,c=y, cmap=plt.cm.coolwarm)
	plt.xlabel('nClass')
	plt.ylabel('IR')
	plt.title('nClass & IR')
	plt.show()

nouvelle_liste()
visualise_data(donneesx,donneesy)


#(-1,1) => une seule dimension ; pour plusieurs (1,-1)
C = 1.0
#donneesy = donneesy.reshape(1,-1)
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(donneesx, donneesy)


