# i) Atomic dictionary with symbol and name
atoms = {
    "H": "Hydrogen",
    "He": "Helium",
    "Ne": "Neon"
}


def AtomicDictionary():

    # ii) Add a unique and duplicate element by the user
    print(atoms)
    print("Add an existing and a unique element into the dictionary")
    symbol = input("\nEnter an existing symbol of the element: ")
    name = input("Enter the name of the element: ")
    atoms[symbol] = name

    symbol = input("\nEnter a new symbol of the element: ")
    name = input("Enter the name of the element: ")
    atoms[symbol] = name

    print(atoms)

    # iii) Display the number of elements in the dictionary
    print("\nNumber of elements in the Atomic dictionary: ", len(atoms))

    # iv) Search for an element in the dictionary
    name = input("\nEnter the element to be searched in the dictionary: ")
    if name in atoms.values():
        print(name, " exists")
    else:
        print(name, " does not exist")
