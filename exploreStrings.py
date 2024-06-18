myStringVariable = "learning python the correct way"

def grabPlaceHolder():
    mrp = 200
    taxes= 30
    price= mrp+taxes
    return price

def demoStringSlicing():
    print("Slicing from index 10 to 16 (not included): " +myStringVariable[10:16])
    print("Slicing the string from starting to index 16(not included): " +myStringVariable[:16])
    print("Slicing the string from an index to the end: "+myStringVariable[9:])
    print("Slicing the string from reverse using negative indexes: "+myStringVariable[-11:-5])

def demoStringModification():
    print("String to uppercase: " +myStringVariable.upper())
    print("String to lower: " +myStringVariable.lower())
    print("str.strip() method removes white spaces at the beginning and end")
    print("str.replace(\" \",\",\") will replace space with a comma in the string: " 
          +myStringVariable.replace(" ",","))
    print("str.split(\" \") will return a list of strings using a space seperator: ")
    spaceSperatedList = myStringVariable.split(" ")
    print(spaceSperatedList)

def demoStringFormatting():
    print("Demonstrate formatting using F-Strings:")
    placeHolder=300 #Placeholder could be a function or operation or a modifier
    grabPlaceHolder()
    formattedString = f"The price of apple watch is {placeHolder} dollars."
    print(formattedString)
    formattedString = f"The price of apple watch is {placeHolder:.2f} dollars."
    print(f"The price of apple pen is {grabPlaceHolder()} dollars." )

print("This is the initial string: " + myStringVariable +"\n")

demoStringSlicing()
print()
demoStringModification()
print()
demoStringFormatting()
print()
print("str.count() Returns the number of times a specified value occurs in a string:" + myStringVariable.count('on'))
print()