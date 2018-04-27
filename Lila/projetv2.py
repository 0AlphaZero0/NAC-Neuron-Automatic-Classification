 # coding: utf-8
from Tkinter import *
import tkFileDialog  ##Permet de Charger les fichiers
from matplotlib.figure import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkFont



#####Fenetre principale
app = Tk()
app.title("Classification neuronale") # donne un titre à la fenêtre
app.geometry("800x600+600+300") # place la fenêtre
app.configure(background='SlateGray2')#fond du programme




############# Variables
#global variableatester
#variableatester=StringVar()
#variableatester.set('True')
variableatester=IntVar()

######Definitions


def Chargementtest(): #### Permet de retourner le chemin absolue permet l'acces au fichier
	name = tkFileDialog.askopenfilename(initialdir = "/",title = "Selection du fichier test",filetypes = (("Fichier csv","*.csv"),("Fichier texte","*.txt")))
	print (name)
	return (name) #Retourne le chemin absolue du fichier



######Recuperer cette putain d'entrée<<<<<<<<<<<<<<<<

def Chargemententrainement():
	global variableatester
	entrainement=Toplevel()
	entrainement.title("Le fichier d'entraînement")
	entrainement.geometry("800x600+600+300")
	textefichier="Avez-vous un jeu d'essai?"
	fichiers=Label(entrainement,text=textefichier)
	fichiers.pack()
	R1 = Radiobutton(entrainement, text="Oui", variable=variableatester, value=1,command=resultatsappui)
	R1.pack( anchor = W )
	R2 = Radiobutton(entrainement, text="Non", variable=variableatester, value=2, command=resultatsappui)
	R2.pack(anchor = W)


def resultatsappui():
	print (variableatester.get())
	if (variableatester.get())==1:
			nameentrainement=tkFileDialog.askopenfilename(initialdir = "/",title = "Selection du fichier entrainement",filetypes = (("Fichier csv","*.csv"),("Fichier texte","*.txt")))
			print (nameentrainement)
			return (nameentrainement)
	if variableatester==2:
			nomentrainement=()####Chemin de notre fichier test


	#text1=Label(entrainement,text="Choisir le fichier d'entraînement",fg="black",bg="white")

#def Parametres(): #### A faire suivant les paramètres sortant
	#print "Selection et fixation des paramètres"

def Lanceranalyse():
	print "Lancer l'analyse"

def presentation():
	presentation=Toplevel()
	presentation.title("Presentation")
	presentation.geometry("800x600+600+300")
	textepresentation="Actuellement etudiant en master I à l'Université de Bordeaux,\n nous avons pour projet de classer des neurones en deux types : Type I et Type II. \n"
	text=Label(presentation,text=textepresentation)
	text.pack()
	presentation.mainloop()

def explicationlogiciel():
	explication=Toplevel()
	explication.title("Le logiciel")
	explication.geometry("1000x500+600+300")
	texteexplication="Présentation du logiciel : \n - Chargement du fichier test : Prend en entrée le fichier test au format .csv et .txt où l'analyse va être réalisé \n - Choisir le fichier d'entrainement : Si le client dispose d'un fichier d'entraînement ayant les types de neurones, il peut le charger sinon un jeu lui sera fourni \n - Paramètres : Concerne le reglage des paramètres à prendre un compte pour l'analyse \n  - Lancer : Permet de lancer l'analyse et d'y afficher les resultats dans une nouvelle fenetre"   ###A mettre en forme
	text=Label(explication, text=texteexplication)
	text.pack()
	explication.mainloop()


def alert():#####Commande bouton du haut
    showinfo("fonctionne")

def Lanceranalyse():
	Analyse=Toplevel()
	Analyse.title("Les résultats")
	Analyse.geometry("1200x800+600+300")
	titretext=Label(Analyse, text="LES RESULTATS", fg="Black", bg="Grey")
	titretext.place(x=500, y=0, width=200, height=50)
	name = ['TypeI', 'TypeII'] ##### Nom des parties
	data = [5000, 6000] ##### Nombre de type I et nombre de type 2
	explode=(0, 0.2) #### Explosion des deux parties (separation)
	plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True) #####autopct = pourcentage réel par rapport à celui indique, axis = equal permet un diagramme circulaire
	plt.axis('equal')
	plt.show('Test')

helv36 = tkFont.Font(family='Helvetica', size=10, weight='bold')
######## Creation de tous les boutons de chargement
text=Label(app, text="Classification Neuronale", fg="RoyalBlue3", bg="SlateGray2", font=helv36)   #####Mettre en gras et en gros (titre)
b1= Button(app, text="Chargement du fichier test",fg="Black", bg="SkyBlue3", command=Chargementtest, font=helv36)
b2= Button(app, text="Choisir le fichier d'entraînement", fg="Black", bg="SkyBlue3", command=Chargemententrainement, font=helv36)
b3= Button(app, text="Paramètres", fg="Black",bg="SkyBlue3", command=Parametres, font=helv36)
b4= Button(app, text="Lancer", fg="Black",bg="SkyBlue3", command=Lanceranalyse, font=helv36)
b5= Button(app, text="Quitter", fg="Black",bg="SkyBlue3", command=app.destroy,width=10, font=helv36)
b1.place(x=300, y=100, width=200, height=40)
b2.place(x=300, y=170, width=200, height=40)
b3.place(x=300, y=240, width=200, height=40)
b4.place(x=300, y=470, width=200, height=50)
b5.place(x=300, y=550, width=200, height=25)
text.place(x=300, y=0, width=200, height=50)
# Exemple : helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')
#b1.font(family='Helvetica', size=36, weight='bold') Fonctionne pas
#http://tkinter.fdex.eu/doc/bw.html
###### Barre de menu
menubar = Menu(app)
menu1 = Menu(menubar, tearoff=0)
menu1.add_separator()
menu1.add_command(label="Créer un nouveau projet", command=alert)
menu1.add_separator()
menu1.add_command(label="Ouvrir un projet", command=alert)
menu1.add_separator()
menu1.add_command(label="Enregistrer le projet en cours", command=alert)
menu1.add_separator()
menubar.add_cascade(label="Fichier", menu=menu1) ######Nom sur la barre de menu

menu2 = Menu(menubar, tearoff=0)
menu2.add_separator()
menu2.add_command(label="Regler les paramètres", command=alert)
menu2.add_separator()
menubar.add_cascade(label="Option", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_separator()
menu3.add_command(label="Qui sommes nous?", command=presentation)
menu3.add_separator()
menu3.add_command(label="Explication du logiciel", command=explicationlogiciel)
menu3.add_separator()
menubar.add_cascade(label="Aide", menu=menu3)

app.config(menu=menubar)
app.mainloop()
