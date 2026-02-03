#let python know you have or will be working with functions 'def'
#enter parameters '()'
def printMessage():
    print("I don't return a value")

#defining function with parameters
def printMessage2(value1, value2): #you could use as many parameters as you want, 0 to many
    ans = value1 + value2
    return ans

answer = printMessage2(4, 2) #calling function with arguments

#(value1, value2) are parameters and (4, 2) are arguments
print(answer)
printMessage()

#Question:
#create a function that will take 1 parameter
#It will convert the argument for the parameter and
#create the next number in a sequence by multiplying it by 2 and adding 3
# return that number and print it to the screen

#Mine
def printMessage3(value1, value2, value3):
    ans = value1 * value2 + value3
    return ans
answer = printMessage3(6, 2, 3)
print(answer)

#teacher
def convert(number):
    converted_number = number * 2 + 3
    return converted_number

myAnswer = convert(5)
print(myAnswer)