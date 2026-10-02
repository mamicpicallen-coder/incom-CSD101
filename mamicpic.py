Mamicpicstudents = [
    ("Jonah Perez", "BSCS", 1),
    ("Alex Santos", "BSMT", 2),
    ("Micah Mendoza", "BSCS", 3),
    ("Allen Torres", "BSMT", 4),

    ("John Cruz", "BSCS", 3),
    ("Maria Reyes", "BSMT", 3),

    ("Kevin Garcia", "BSCS", 4),
    ("Angela Dela Cruz", "BSMT", 4)
]

print("\nStudent Information ")


Mamicpicprogram = input("Enter program to search (BSCS/BSMT): ").upper()

print("\nStudents in", Mamicpicprogram)

Mamicpicfound = False

for Mamicpicstudent in Mamicpicstudents:
    if Mamicpicstudent[1] == Mamicpicprogram:
        print("Name:", Mamicpicstudent[0])
        print("Program:", Mamicpicstudent[1])
        print("Year Level:", Mamicpicstudent[2])
        print()
        Mamicpicfound = True

if Mamicpicfound == False:
    print("No students found for", Mamicpicprogram)
    
