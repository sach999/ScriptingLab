class student:

    def __init__(self):
        self.name = 0
        self.age = 0

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        i = 1
        for mark in self.marks:
            print("Mark ", i, " = ", mark)
            i += 1

    def accept(self):
        self.name = input("Enter name of the student: ")
        self.age = input("Enter age of the studen")
        self.marks = input("Enter 3 marks")
        self.marks = list(self.marks.split(" "))


s1 = student()
s1.accept()

s2 = student()
s2.accept()

s1.display()
s2.display()
