class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length*self.breadth
        print("Area is : ", area)


ob1 = rectangle(2, 3)
ob1.area()
ob2 = rectangle(8, 7)
ob2.area()
