class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.marks = {}

    def input_marks(self, students):
        for student in students:
            mark = float(input(f"Enter mark for {student.name} in {self.name}: "))
            self.marks[student.id] = mark

    def show_marks(self, students):
        print(f"Marks for {self.name} ({self.id}):")
        for student in students:
            mark = self.marks.get(student.id, '-')
            print(f"{student.name}: {mark}")

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def input_student_information(self):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth (DD/MM/YYYY): ")
        student = Student(student_id, student_name, student_dob)
        return student

    def input_course_information(self):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course = Course(course_id, course_name)
        return course

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"ID: {course.id}, Name: {course.name}")

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}, Date of Birth: {student.dob}")

    def input_marks_for_course(self):
        self.list_courses()
        course_id = input("Enter the course ID: ")
        course = next((c for c in self.courses if c.id == course_id), None)
        if course:
            course.input_marks(self.students)
        else:
            print("Invalid course ID")

    def show_student_marks_for_course(self):
        self.list_courses()
        course_id = input("Enter the course ID: ")
        course = next((c for c in self.courses if c.id == course_id), None)
        if course and course.marks:
            course.show_marks(self.students)
        else:
            print("Invalid course ID or marks not yet input")

