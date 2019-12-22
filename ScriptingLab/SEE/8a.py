atoms = {
    "H": "Hydrogen",
    "He": "Helium",
    "Li": "Lithium"
}

print(atoms)

symbol = input("\nEnter an existing element ")
name = input("Enter the name of the element")
atoms[symbol] = name
print(atoms)

symbol = input("\nEnter a new element ")
name = input("Enter the name of the element")
atoms[symbol] = name
print(atoms)

print("Number of elements in the dictionary: ", len(atoms))

name = input("Enter element name to be searched: ")
if name in atoms.values():
    print("Exists")
else:
    print("Does not exist")
