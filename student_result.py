# Student Result Management System

students = []

def add_student():
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))

    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 45:
        grade = "D"
    else:
        grade = "F"

    students.append({
        "name": name,
        "score": score,
        "grade": grade
    })

def display_students():
    print("\nStudent Results:")
    for student in students:
        print(f"Name: {student['name']} | Score: {student['score']} | Grade: {student['grade']}")

while True:
    print("\n1. Add Student")
    print("2. Display Results")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")
