#!/usr/bin/env python
#-*- coding: utf-8 -*-

# http://www.agregationphysique.fr/FAQPython/build/html/graphiques.html


# import matplotlib.pyplot as plt
#
# plt.title("Danger de la vitesse") #titre du graph
# plt.plot([50,100,150,200], [1,2,3,4]) #axes des x et y
# plt.xlabel('Vitesse') #légende x
# plt.ylabel('Temps') #légende y
# plt.show()


#superposition courbes

# plt.plot([50,100,150,200], [1,2,3,4], "r--", linewidth=5, marker="*", label="trajet 1")
# plt.plot([50,100,150,200], [2,3,7,10], "bs")
# plt.plot([50,100,150,200], [2,7,9,10], "g^")
# plt.axis([80, 180, 1, 10]) #échelle des axes x et y
# plt.xlabel('Vitesse')
# plt.ylabel('Temps')
# plt.legend()
# plt.annotate('Limite', xy=(150, 7), xytext=(165, 5.5), #ajout flèche de taille couleur etc
# arrowprops={'facecolor':'black', 'shrink':0.05} )
# plt.show()

#Courbes possibles: - -- -. :
#Couleurs possibles: b g r c m y k w
#grossir les courbes linewidth=5
#ajout texte en indiquant coordonnées plt.text(150, 6.5, r'Danger')



###### graph 3D ######
# """
# tracé des vecteurs champs E et B pour une OemPPH
# """
#
# from __future__ import division
# from scipy import *
# from pylab import *
#
# import matplotlib as mpl
# from mpl_toolkits.mplot3d import Axes3D # librairie 3D
#
# # Type de l'onde
# E0y = 1
# E0z = 1
# phi = pi/2
# T = 125
#
# fig = figure()
# ax = fig.gca(projection='3d')
#
# x,y,z = array([]), array([]), array([])
#
# for i in range(301):
# 	x_fin=i
# 	y_fin=E0y * cos(2*pi*i/T)
# 	z_fin=E0z * cos(2*pi*i/T-phi)
# 	plot([i,x_fin], [0,y_fin], [0,z_fin],color='b')     # Champ E
#
# 	x = append(x,x_fin)
# 	y = append(y,y_fin)
# 	z = append(z,z_fin)
#
# plot(x, y, z,color='b',lw=2)    # Contour du Champ E (paramétrique 3D)
# show()

'''
==============
3D scatterplot
==============

Demonstration of a basic scatterplot in 3D.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 100

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
