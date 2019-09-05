print("List manipulation: ")
list1 = ["TinTin", 22, 5.42, "Belgium", "Boy Detective"]
list2 = [45, "Haddock"]

print(list1)
print(list1[0:3])
print(list1[2:])
print(list1*2)
print(list1+list2)

# Tuples cannot be manipulated
print("\nTuple manipulation: ")
myTuple = ("TinTin", 22, 5.42, "Belgium", "Boy Detective")
yourTuple = (45, "Haddock")

print(myTuple)
print(myTuple[0:3])
print(myTuple[2:])

print(""" 
    Tuple elements cannot be changed
    The only way to change is by replacing the whole tuple
""")

myTuple = myTuple + yourTuple
print(myTuple)

yourTuple = yourTuple*2
print(yourTuple)
