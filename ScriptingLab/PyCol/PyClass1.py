#Demo: Classes in python

class Person:
	def __init__(self, name, age):		#Constructor of the class Person
		self.name = name;
		self.age = age;

#Two objects p1 and p2 are created. The __init__ constructor is automatically called
p1 = Person("Suppandi", 14)
p2 = Person("Ramu", 12)

print("\nName of the person 1: ",p1.name)
print("\nAge of the person 1: ",p1.age)

print("\nName of the person 2: ",p2.name)
print("\nAge of the person 2: ",p2.age)

p2.age = 10	#Attributes of the objects can be modified. By default public

print("\nModified age of person 2: ", p2.age)
