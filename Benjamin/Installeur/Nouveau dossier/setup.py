from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
	name="Classif neuronale",
	version = "1",
	Description = "testduexe"
	executables = [Executable("projetest.py")],
)


