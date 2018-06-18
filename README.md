<h1 align="center">NAC</h1>
<p align="center">Neuron Automatic Classification</p>
<p align="center">Tool for automatic classification of biological neural signals.</p>

## Table of contents

- [Descritption](#description)
- [User installation](#user-installation)
  - [Dependencies](#dependencies)
  - [Windows](#windows)
  - [MacOS and UNIX](#macos-unix)
- [Source code](#source-code)
- [Customer](#customer)
- [Contact](#contact)
- [Related documents](#related-docs)
  - [Specifications](#specifications)
  - [Report](#specification)
  - [Defense](#defense)

<a name="description"></a>
## Description 

Des données électrophysiologiques concernant deux populations de neurones distinctes ont
été recueillies par plusieurs équipes de recherche avec des mesures et des paramètres
expérimentaux communs. L'objectif du projet est de trouver un moyen de classer
automatiquement les neurones à partir de ces données avec le meilleur taux de prédiction
possible. Cette alternative présenterait plusieurs avantages comme celui d'éviter le recours à
des animaux transgéniques.

Un jeu de données est mis à la disposition des étudiants avec la catégorie (1 ou 2) de chaque
neurone. Idéalement une méthode d'apprentissage supervisé est envisagée à l'aide de la
bibliothèque **Caret** et du **logiciel R** mais également en utilisant le **langage Python** et **la librairie
Scikit-Learn**. Toute autre solution peut être envisagée et ceci peut être discuté avec le groupe
d'étudiants.

<a name="user-installation"></a>
## User installation 

<a name="dependencies"></a>
#### Dependencies : 
- Python2.7
- Sckiti-leran: sklearn
- Matlplotlib
- Tkinter

<a name="windows"></a>
#### Windows :
Just unpack the file : Classification-Neuronale.zip 
and run LaClassificationNeuronale.exe

<a name="macos-unix"></a>
#### MacOS and UNIX :
Before use the script you need to install some packages:  
  -python2.7 (if you are on MacOS)  
  -pip  
  -numpy  
  -scipy  
  -scikit-learn  
  -matplotlib  
  -Tkinter  

For the first time, open a terminal and use these command :
<pre><code>     sudo apt-get install python2.7
     python ge-pip.py
     pip install -U numpy,scipy,scikit-learn
     python -mpip install matplotlib
     apt-get install python-tk</code></pre>

If you already have a working installation of any of these packages :
  <pre><code>     pip -review --auto
     sudo apt-get update && apt-get upgrade</code></pre>

<a name="source-code"></a>
## Source code 
You can check the latest source swith the command :
<pre><code>     git clone https://github.com/0AlphaZero0/Projet-Neuro.git</code></pre>

<a name="customer"></a>
## Customer 
André Garenne (andre.garenne@u-bordeaux.fr),Equipe MNEMOSYNE, laboratoire IMN

<a name="contact"></a>
## Contact

***Author :***  
  Thouvenin Arthur : athouvenin@outlook.fr

***Contributors :***  
  Blais Benjamin : ben.blais@laposte.net  
  Cottais Déborah : d.cottais1@gmail.com  
  De Oliveira Lila : lila.de-oliveira@etu.u-bordeaux.fr  
  Jouan Clément : jouan.clement@hotmail.fr  

<a name="related-docs"></a>
## Related documents

<a name="specifications"></a>
#### Specifications : 
[specifications](https://www.overleaf.com/13775721dzzjsknmydhv "Link to the document")

<a name="report"></a>
#### Report : 
[report](https://www.overleaf.com/13781350mcsgyrmmnxxg "Link to the document")

<a name="defense"></a>
#### Defense : 
[defense](https://www.overleaf.com/14303504qzthnffthftb#/55103801/ "Link to the document")


Librairie Scikit-Learn : https://makina-corpus.com/blog/metier/2017/initiation-au-machine-learning-avec-python-pratique
Documentation scikit :
- http://scikit-learn.org/stable/modules/svm.html docs
- https://www.youtube.com/watch?v=ZD5lJGq1rvQ Youtube
- https://pythonprogramming.net/linear-svc-example-scikit-learn-svm-python/

---
