==============================================
			
	  Neurons Classification

==============================================



This program is the result of a project created by 
	BLAIS Benjamin, 
	COTTAIS Déborah, 
	DE OLIVEIRA Lila, 
	JOUAN Clément and 
	THOUVENIN Arthur during their first year of 
master at the university of Bordeaux in 2018.






What is Neurons Classification ?

===============================


Neurons Classification is an instrument (software) which allows a user to classify in two categories (I and II) neurons thanks to different electrophysiological parameters.





Language and library used ?

===========================


Language = Python 2.7


Libraries = Scikit learn library with svm and MLPClassifier


========Tkinter (graphic interface)
	    	
	    tkFileDialog  (Allows to create a windows to load files)
	    	
	    tkFont (Allows to modify the TKinter display font)
	    	
	    IntVar,StringVar,Menu,Label,Toplevel,Radiobutton,Button,Entry,Scale,
	    	
	    Checkbutton,FLAT (Allow the use of the TKinter GUI)

	
========sklearn
	    sklearn.svm (Allows to use the SVM classification method)
	    	
	    sklearn.neural_network
 
	    MLPClassifier (Allows the use of the neural network method from sklearn)

========Matplotlib (graphic visualization)
	    	
	    matplotlib as mpl (Allow to use matplotlib to make graphs)
	    	
	    matplotlib.pyplot as plt (Allows to create graphics, especially those in 3D)
	    	
	    style (Allows to modify the graphics' appearance)
	    	
	    matplotlib as mpl (Allow to use matplotlib to make graphs)
	    	
	    FigureCanvasTkAgg (Allow some option in matlpotlib to make 3D graphs)
	    	
	    mpl_toolkits.mplot3d
	    		Axes3D

	    
========Numpy
	    	
	    numpy as np (Allows to manipulate the necessary table for sklearn)


========Other	    
	codecs (to load a file containing UTF-8 characters)
	    
	random (to use random variables)
	   
 	webbrowser os (Allows to modify some things on the os)
	    
	sys (Allow to modify files on the OS)
	    
	shutil (Allows file copy)






How do I use Neurons Classification ?

=====================================


Please refer to the manual of utilisation.





Modifications or contributions

==============================

New method:

	1)  If your method need to call a new class then you need to modify choiceparamclass() function line397.
	You just have to had a new line after 'P4= Button......' like:
		'Pn = Radiobutton(Winclasse, text=yourtext, variable=paramvariable,value=n,command=methodchoice)'
	and also add at the end of line 420:'explanationtext.pack();P1.pack();...':
		';Pn.pack()'
	where n correspond to your class number and your text correspond to a string which appear next to the button created.
	
	2)  If your method doesn't need a new class then add to the right class (check function choiceparamclass() 
	to see the right number corresponding to the class) after the last radiobutton of the class:
		'Rn=radiobutton(Winmet,text=yourmethod,variable=methods,value=yourmethod,command=hyperparamchoice)
		or
		'Sn=radiobutton(Winmet,text=yourmethod,variable=methods,value=yourmethod,command=hyperparamchoice)
	and also add at the instruction add your radiobutton.pack():'methodchoice.pack();Rn.pack();....'or'methodchoice.pack();Sn.pack();....':
		';Rn.pack()'
		or
		';Sn.pack()'
	If your method NEED a new class then you need to add at the end of the same paragraph that begin with 'if classes==4:....'
	Just be carefull you jut need to add the number of button corresponding to the number of method added, then follow the same pattern as above 
	
	3)  If your method needs hyperparameters, then you'll need to modify the hyperparamchoice() function
		a) You will need to add a specific condition like:
			'if method==yourmethod and classes=n:
				hyper1=Scale(Winhyper,orient='horizontal',from=start_value,to=end_value,resolution=step_between_2values,tickinterval=step_between_2values,length=350,label=yourtext)
				hyper2....
				hypern=Scale(Winhyper,...'
	where yourmethod is a string, classes n correspond to the number of your class, add hyperparameters like hypern as you want.
	Be carefull with start_value,end_value adn step_between_2values, which make limit of your hyperparameter. If your hyperparameter
	logarithmically varies then use only exhibitors.
		b)  You will also need to modify intern function confirmhyperparam, where you take back your hyperparameter and made him the right value through a 
			'nameofhypern=float(hypern.get())'
		don't forget to declare your nameofhypern atthe end of global declaratio line through a 
			';global nameofhypern'

	4)  In the function trainingfile(verif) line295:
		If it's a new classe then add, after line 392:
			'if classes==nb:
				clf=yourmethod'
	where nb is an integer and yourmethod correspond to the train of the model.
	This scheme is similar all along the function as you can see on top of line 390.
		If there is more than 1 methodin your class or if you add a new method in a pre-existing class:
			'if classes==1:
				if method==yourmethod:
					clf=CLASS(yourmethod,hyper1,...,hypern)'


Reset of Backup files:
	First of all you should always save trainning file from programm directory to another one of your directory
	Like it's descript in the programm you can modify your results BUT first it is strongly recommended to save 
	your result and then modify them and again save in another file.
	You also have the choice to add you results to your trainning file, you should be really carrefull there is only one 
	backup so save your new trainning files in an another directory 
	If you have any problems with your trainning file, and you want to reset them THEN you should delete 'Yourbackup.csv' and 
	'TrainModel.csv', and then replace by the two files which are in the Backup directory your 'Backup_G.csv' and 'ModelG.csv'.


Support ?

===========================


Linux

Windows





Installing on Unix system :

=====================

Before using the software, you have to install the python language and the following libraries :
	
- python,pip,numpy,scipy,scikit-learn,matplotlib,Tkinter

====Commands to install:
	-sudo apt-get install python2.7
	
	-python get-pip.py
	
	
	-pip install -U numpy, scipy, scikit-learn
	
	-python -mpip install matplotlib
		
	-apt-get install python-tk
====Commands to check installation:
	-python
	-import pip
	-import numpy
	-import scipy
	-import sklearn
	-import matplotlib
	-import Tkinter
if you get an error with the execution of these lines, so there is a problem with module's installation.
====Commands to run programm:
	-python filename (if you are in the directoryof the programm)
	-python pathfile

If you already have any of these :
	-pip -review --auto

	-sudo apt-get update && apt-get upgrade
	


Installing on Windows :

=====================

Install the program ClassificationNeuronale in the folder of your choice
Execute ClassificationNeuronale.exe as administrator.


Use on Mac :
============

There is no executable file for MacOS so it's like Unix system,
 you'll have to install:
- python2.7,pip,numpy,scipy,scikit-kearn,matplotlib and Tkinter
Then you'll need to check if installation is correct.(see Unix part)

At the end just run the file ClassificationNeuronale.py with python:
	-python ClassificationNeuronale.py (in the corresponding directory)
	or
	-python path_of_ClassificationNeuronale.py

Image sources :

===============

Brain image 509365378 @ iStock Ukusucha

http://scikit-learn.org/stable/

https://www.u-bordeaux.fr/
