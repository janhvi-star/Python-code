class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_info(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}"


class Teacher:
    def __init__(self, name, subject, teacher_id):
        self.name = name
        self.subject = subject
        self.teacher_id = teacher_id

    def display_info(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Subject: {self.subject}"


class Course:
    def __init__(self, course_name, teacher_name):
        self.course_name = course_name
        self.teacher_name = teacher_name

    def display_info(self):
        return f"Course: {self.course_name}, Taught by: {self.teacher_name}"


# Create lists to store students, teachers, and courses
students = []
teachers = []
courses = []

while True:
    print("\nSchool Management System")
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. Add Course")
    print("4. View Students")
    print("5. View Teachers")
    print("6. View Courses")
    print("7. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        student_id = input("Enter student ID: ")
        students.append(Student(name, age, student_id))
        print("Student added successfully!")

    elif choice == '2':
        name = input("Enter teacher name: ")
        subject = input("Enter subject taught: ")
        teacher_id = input("Enter teacher ID: ")
        teachers.append(Teacher(name, subject, teacher_id))
        print("Teacher added successfully!")

    elif choice == '3':
        course_name = input("Enter course name: ")
        teacher_name = input("Enter teacher's name for the course: ")
        courses.append(Course(course_name, teacher_name))
        print("Course added successfully!")

    elif choice == '4':
        print("\nStudents List:")
        for student in students:
            print(student.display_info())

    elif choice == '5':
        print("\nTeachers List:")
        for teacher in teachers:
            print(teacher.display_info())

    elif choice == '6':
        print("\nCourses List:")
        for course in courses:
            print(course.display_info())

    elif choice == '7':
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
