# Create a dictionary to hold student details with Register numbers and print details of students with even register number

studDetails = {
    1000: {
        "name": "Rosie",
        "age": 20,
        "section": "A"
    },
    1001: {
        "name": "Roshan",
        "age": 20,
        "section": "A"
    },
    1002: {
        "name": "Reid",
        "age": 21,
        "section": "B"
    },
    1003: {
        "name": "Rahul",
        "age": 21,
        "section": "C"
    },
    1004: {
        "name": "Aaron",
        "age": 20,
        "section": "A"
    }

}

for a in studDetails:
    if a % 2 == 0:
        print(a, " : ", studDetails[a])
