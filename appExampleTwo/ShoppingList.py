#------Connecting to file

shoppingList = "Shopping.txt"

#------Opening File, spliting into lines

o = open(shoppingList,"r")
myShoppingList = o.read().split("\n")

#------Closing file

o.close

#------Printing Title

print("")
print("Shopping List:".upper())
print("")

#------splitting item and category from list

for line in range(0, len(myShoppingList)):
    currentLine = myShoppingList[line]
    food = currentLine.split(",")[0]
    category = currentLine.split(",")[1]

#------Assign aisle to category

    if category == "Meat":
        print("You need " + food, " you will find this in " + "Aisle 1")
    elif category == "Vegetable":
        print("You need " + food, " you will find this in " + "Aisle 2")
    elif category == "Fruit":
        print("You need " + food, " you will find this in " + "Aisle 3")
    else:
        print("You need " + food, " aisle unknown")