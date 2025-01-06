class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

    def display_info(self):
        return f"Roll No: {self.roll_no}, Name: {self.name}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, roll_no, name):
        # Check if the roll number already exists
        for student in self.students:
            if student.roll_no == roll_no:
                print("Error: A student with this roll number already exists!")
                return
        new_student = Student(roll_no, name)
        self.students.append(new_student)
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found.")
        else:
            print("\nStudent List:")
            for student in self.students:
                print(student.display_info())


# Main program
sms = StudentManagementSystem()

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        roll_no = input("Enter roll number: ")
        name = input("Enter student name: ")
        sms.add_student(roll_no, name)

    elif choice == '2':
        sms.view_students()


    elif choice == '4':
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
