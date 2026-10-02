

students = {
    "Ana": 85,
    "Ben": 90,
    "Carlo": 78,
    "Diana": 95,

}

print("STUDENT GRADES")
print("===============")

print("Ana" , students["Ana"])
print("Ben" , students["Ben"])

students["Ella"] = 88

students["Carlo"] = 82
students["diana"] = 91

name1 = input("Enter Student Name: ")
grade1 = int(input("Enter Grades: "))
students[name1] = grade1
print(students)

print("\nUpdated Students Grades: ")
print("============================")

for name, grade in students.items():
    print(name, "", grade)

    search = input("\nEnter Student Name to Search")
if search in students:
    print(search, "has a grade of", students[search])

else:
    print("Students not Found")


    highest = max(students, value = students.get)
    print(students, highest)

    lowest = min(students, value = students.get)
    print(students, highest)

