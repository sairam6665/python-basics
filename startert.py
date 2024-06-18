welcomeMessage = "Hello Python" #Global Variable
floatVariable = 25.0
learnPython = True

def printIntegers():
	x = y = z = 5 #local variable
	var = 25
	VAR = 30
	print("Sum is : ",x+y+z)
	print("var is : ",var)
	print("VAR is : ",VAR)

def printString():
	x,y,z = "Over","ridden","String"
	print(x+y+ " " +z)

def printWelcomeMessage(str):
	print(welcomeMessage)

def variableTypesInPython():
	print(type(welcomeMessage))
	print(type(floatVariable))
	print(type(learnPython))

printWelcomeMessage(welcomeMessage)
printIntegers()
printString()
variableTypesInPython()
	
