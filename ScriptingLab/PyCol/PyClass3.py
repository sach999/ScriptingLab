#Demo: Classes in python

class Person:
	def __init__(self, name, age):		#Constructor of the class Person
		self.name = name;
		self.age = age;


p1 = Person("Suppandi", 14)

print("\nName of the person : ",p1.name)
print("\nAge of the person : ",p1.age)

print("\n*** Printing after deleting age attribute ***")

del p1.age	#Deleting age attribute

print("\nName of the person : ",p1.name)
#print("\nAge of the person : ",p1.age) 		#Gives an error - 'Person' object has no attribute age

print("\n*** Printing after deleting p1 ***")
del p1
print("\nName of the person : ",p1.name)  	#Gives an error - name 'p1' is not defined

