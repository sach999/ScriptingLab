# i)Create class having attributes name, age and marks of 3 subjects
class Student:

    # ii) Create a constructor accepting the values
    def __init__(self, name, age, marks):

        self.name = name
        self.age = age
        self.marks = marks[:]

    # iii) Member function to display the details
    def display(self):
        print("NAME: ", self.name)
        print("AGE: ", self.age)
        i = 1
        for mark in self.marks:
            print("Mark ", i, ") = ", mark)
            i += 1


# iv) Ask user for the inputs
marks = []


def accept():
    name = input("Enter name of the student: ")
    age = input("Enter age of the student: ")
    print("Enter 3 marks")
    for i in range(3):
        marks.append(input())

    return name, age, marks


name, age, marks = accept()

s1 = Student(name, age, marks)

marks = []

name, age, marks = accept()

s2 = Student(name, age, marks)

# v) calling display function
print(s1.display())
print()
print(s2.display())
