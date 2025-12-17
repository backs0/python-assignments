students = {}

def add_student():
    name = input("Enter the student's name: ").strip()
    if name in students:
        print("Error: Student already exists.")
        return

    while True:
        try:
            grade = int(input(f"Enter {name}'s grade: ").strip())
            break
        except ValueError:
            print("Invalid input! Please enter a whole number.")

    students[name] = [grade]
    print(f"{name} added successfully with grade {grade}!")

def update_grade():
    name = input("Enter the student's name: ").strip()
    if name not in students:
        print("Error: Student not found.")
        return

    print(f"Current grades for {name}: {students[name]}")
    print("Note: indices start at 0. For example, the first grade is index 0.")

    try:
        index_text = input("Enter the index of the grade to update (starting from 0): ").strip()
        index = int(index_text)
    except ValueError:
        print("Invalid input! Please enter a whole number for the index.")
        return

    try:
        new_grade_text = input("Enter the new grade: ").strip()
        new_grade = int(new_grade_text)
    except ValueError:
        print("Invalid input! Please enter a whole number for the grade.")
        return

    try:
        students[name][index] = new_grade
        print(f"{name}'s grade at index {index} updated to {new_grade} successfully!")
    except IndexError:
        print("Invalid index! Please choose an index that exists in the list.")
        return

def remove_student():
    name = input("Enter the student's name to remove: ").strip()
    if name in students:
        del students[name]
        print(f"{name} removed successfully!")
    else:
        print("Error: Student not found.")

def display_students():
    if not students:
        print("No students in the system.")
        return

    print("Student Grades: ")
    for name, grades in students.items():
        grade_strings = []
        for grade in grades:
            grade_strings.append(str(grade))

        grade_line = ", ".join(grade_strings)

        print(f"{name}: {grade_line}")
    print()


def main():
    while True:
        print("Student Management System")
        print("1. Add a new student")
        print("2. Update a grade")
        print("3. Remove a student")
        print("4. Display all students")
        print("5. Quit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            update_grade()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
