# from http://scikit-learn.org/stable/auto_examples/exercises/plot_iris_exercise.html
# details here : http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm
from pylab import *

iris = datasets.load_iris()
X = iris.data
y = iris.target
X = X[y != 0, :2]
y = y[y != 0]
n_sample = len(X)
np.random.seed(0)
order = np.random.permutation(n_sample)
X = X[order]
y = y[order].astype(np.float)
kern=["linear", "rbf", "poly"]
fracRange=np.arange(0.1,0.9,0.01)
res=""
bestScore=0
bestRes=""
linScores=[]
rbfScores=[]
polScores=[]
print X

for tFrac in fracRange:
	#print tFrac
	X_train = X[:int(tFrac * n_sample)]
	y_train = y[:int(tFrac * n_sample)]
	X_test = X[int(tFrac * n_sample):]
	y_test = y[int(tFrac * n_sample):]
	res+=str("Training fraction : "+str(tFrac)+"\n")
	for k in kern:
		clf = svm.SVC(kernel=k)
		clf.fit(X_train, y_train)
		predicted = clf.predict(X_test)
		score=sum(predicted==y_test)/float(len(predicted))
		res+="\t"+k+" : "+str(score)+"\n"
		if k=="linear":
			linScores.append(score)
		if k=="rbf":
			rbfScores.append(score)
		if k=="poly":
			polScores.append(score)
		if score>bestScore:
			bestScore=score
			bestRes="Fraction = "+str(tFrac)+", method="+k+", results="+str(score)

print bestRes
plot(fracRange,linScores)
plot(fracRange,rbfScores)
plot(fracRange,polScores)
legend(kern)
show()