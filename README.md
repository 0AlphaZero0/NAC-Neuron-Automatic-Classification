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
- [Usefull links](#usefull-links)

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
André Garenne (andre.garenne@u-bordeaux.fr), Team MNEMOSYNE, laboratory IMN

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
[Link to specifications](https://drive.google.com/open?id=1pr_l8iCtvyq6EVjVE3XpWFjlLITfh9DM "Link to the document") 
(in french)

<a name="report"></a>
#### Report : 
[Link to report](https://drive.google.com/open?id=18B4_uuUy6er4mA6klom4j2o6S3sJ_avP "Link to the document")
(in french)

<a name="defense"></a>
#### Defense : 
[Link to defense](https://drive.google.com/open?id=1y15v8rmb-nSddkTqOnmX7ppa-vZr1tq2 "Link to the document")
(in french)

<a name="usefull-links"></a>
## Usefull links

- Scikit-Learn : [Sklearn](http://scikit-learn.org/stable/index.html# "Link to Scikit-Learn website")
  - SVM from Scikit-Learn : [SVM](http://scikit-learn.org/stable/modules/svm.html "Link to SVM documentation from Sklearn")
  - Neural Network from Scikit-Learn : [Neural Network](http://scikit-learn.org/stable/modules/neural_networks_supervised.html "Link to Neural Network documentation from Sklearn")
  
- Playlist of youtube videos which explain how scikit-learn work (by Sentdex) : [Scikit-learn Machine Learning with Python and SKlearn](https://www.youtube.com/watch?v=URTZ2jKCgBc&list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3 "Scikit-learn Machine Learning with Python and SKlearn")
