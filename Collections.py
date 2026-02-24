# create a list in python
# lets start with a list of fruit
# mutable
# Index - always start a 0, Grape would be 3, Orange 4, if mentioning 5, it will be nothing
# A list could be dynamic, 0 to many, not static
# a List a square brackets
# A list it Mutable
fruitList = ["Apple", "Banana", "Cherry", "Grape", "Orange"]
print(fruitList)

#specific item in a list
print(fruitList[1])
#Update a index of a list
fruitList[2] = "Pear"
print(fruitList)
#adding a index
fruitList[2] = "Cherry"
fruitList.append("Pear")
print(fruitList)
#append will add the index to the end of the list, pear will now be 5

#adding a index in between two indexes of the list using a function
fruitList.insert(4, "Grapefruit")
print(fruitList)

#removing items from the list
fruitList.pop(4)
print(fruitList)
#removing by value instead of index
fruitList.remove("Pear")
print(fruitList)
#adding a duplicates
fruitList.append("Banana")
print(fruitList)
#when removing a index that has 2, It will pick the first one it sees and remove it
fruitList.remove("Banana")
print(fruitList)

countfruits = len(fruitList)
print(countfruits)
#this will give you the length of the list

fruitList.append(42)
print(fruitList)
#this allows you to add a value to your list

print(fruitList[2:4])
#this code lets you print the range, starting the list a 'Grape' and the offset will be 'Orange'
#Offset +1


#Tuples are different from lists
#Tuples are static, not dynamic like Lists
#Tuples have round brackets
#Tuples are NOT Mutable

carTuple = ("Corolla", "Civic", "Sentra", "Eclipse")
print(carTuple)

# Ex:
#carTuple.append("Tundra")
#print(carTuple)
# - you cannot add to a Tuple

print(carTuple[2])

# A Tuple is secure date, you could turn a Tuple into a list and a list into a Tuple, a list could also pull from a Tuple
# A Tuple cannot be edited

toyTuple = carTuple
print(toyTuple)
