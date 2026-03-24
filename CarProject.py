#Constructor that helps to find the class, which is __init__, "Init" stands for Initialize
#class Vehicle:
    #def __init__(self, brand, type, doorCount, model):
        #self.brand = brand
        #self. type = type
        #self. doorCount = doorCount
        #self. model = model

#khoaCar = Vehicle("Tesla", "Truck", 2, "Cyber Truck")
#johanCar = Vehicle("BMW", "Sports Car", "2", "M4")


#print(khoaCar.brand)
#print(johanCar.doorCount)

#Making a classroom with 1 person inside

#class Person:
    #def __init__(self,age, name, major):
        #self.age = age
        #self.name = name
        #self.major = major

#class Classroom:
    #def __init__(self, Person, course):
        #self.Person = Person
        #self.course = course

#student = Person(18, "Olivia", "college")
#introClass = Classroom(student, "Intro to Programming Concepts")

#print(introClass.Person.name)

#adding more than 1 person to a classroom

class Person:
    def __init__(self,age, name, major):
        self.age = age
        self.name = name
        self.major = major

class Classroom:
    def __init__(self, course):
        self.people = []
        self.course = course

    def add_person(self, Person):
        self.people.append(Person)

student = Person(18, "Olivia", "college")
student2 = Person(23, "Fred", "business")
student3 = Person(28, "Laura", "computer science")

introClass = Classroom("Intro to Programming Concepts")

introClass.add_person(student)
introClass.add_person(student2)
introClass.add_person(student3)

for person in introClass.people:
    print(person.name)

print(introClass.people)