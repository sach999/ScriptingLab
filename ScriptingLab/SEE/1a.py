l = []

while True:
    print("1. Create\n2.MinMax\n3.Insert\n4.Delete\n5.isPresent\n6.Exit\n")
    ch = int(input())

    if ch == 1:
        n = int(input("Enter number of elements:\n"))
        print("Enter elements\n")
        for i in range(0, n):
            s = int(input())
            l.append(s)
        print(l)

    if(ch == 2):
        print("Max element : ", max(l))
        print("Min element: ", min(l))

    if(ch == 3):
        temp = int(input("Enter a new element to appended\n"))
        l.append(temp)
        print(l)

    if(ch == 4):
        temp = int(input("Enter element to be removed\n"))
        if temp not in l:
            print("Element not found")
        else:
            l.remove(temp)
        print(l)

    if(ch == 5):
        temp = int(input("Enter element to be searched\n"))
        if temp in l:
            print("Found")
        else:
            print("Not found")

    if ch == 6:
        break
