# 1)
list1 = ["Hello", "World", 8, 7]

# Length of the list
print("Length of String: ", len(list1))

# Create a new list as an element of an existing list
print("\nAppeding a Sub List")
list1.append(["sub", "list"])
print(list1)

# using slice operator
print("\nList after slicing: ")
print(list1[0:3])

# Replace second element with a fruit name
list1[1] = "Banana"
print("\nList after Replacing: ")
print(list1)

# Concatenating two lists
list2 = ["second", "list", 3]
print("\nConcatenated List: ")
print(list1+list2)

# 2 ways to clone a list
print("\nCopied List: ")
newList = list1[:]
print(newList)
newList2 = list1.copy()
print(newList2)

# Split a list into evenly sized chunks
print("\nAfter splitting into groups of 3: ")
for i in range(0, len(list1), 3):
    print(list1[i:i+3])


# 2) Create a tuple with numbers and print one item
myTuple = (1, 2, 3, 4, 5, 6, 7, 8)
print("\nTuple list item: ")
print(myTuple[7])

# 3) Converting tuple to list
li = list(myTuple)
print("\nConverted list: ")
print(li)
