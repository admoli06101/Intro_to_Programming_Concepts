# Structure of a while loop
#while(Condition):
    #some code
    #run if the condition is true
    #break this loop if the condition is false
    #anything that is indented bleongs to the while loop
    #tbe while loop contains the keyword "while" and has a colon at the end

#code that is not in the while loop. Will run after the while loop ends.

heartWants = int(input("How many times do you love me?"))
runThisLoop = 0

while(runThisLoop < heartWants):
    print("I love this many times", runThisLoop)
    runThisLoop = runThisLoop + 1
    #Try not to use this code 'break', since it's bad practice, avoid using when possible

print("The loop ended, and I am outside the loop")

# When you see a statement that is repetitive and/or need to fill data and/or
# need to retrieve more than one data set

# structure of a for loop
# for a variable in list:
    #code here
    #run for loop until the end
    #will run through a list from the beginning to end

# outside code here. Won't run until end of for loop

groceryList = ["apple", "banana", "cherry", "bread", "eggs", "cereal"]

for item in groceryList:
    print(item)

print("The end of the list, and out of the loop")

# different example
heartWants = int(input("We the Best music?"))
runThisLoop = 0

while(runThisLoop < heartWants):
    print("Dj Khalid")
    if(runThisLoop > 0):
        print("And another one")
    runThisLoop = runThisLoop + 1

print("The loop ended, and I am outside the loop")