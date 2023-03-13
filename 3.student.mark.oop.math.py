import math
import numpy as np

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        
class Course:
    def __init__(self, id, name, credits):
        self.id = id
        self.name = name
        self.credits = credits
        self.marks = {}

    def input_marks(self, students):
        for student in students:
            mark = float(input(f"Enter mark for {student.name} in {self.name}: "))
            mark = math.floor(mark * 10) / 10.0 # round down to 1 decimal
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
        course_credits = float(input("Enter course credits: "))
        course = Course(course_id, course_name, course_credits)
        return course

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"ID: {course.id}, Name: {course.name}, Credits: {course.credits}")

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

    def calculate_gpa_for_student(self):
        self.list_students()
        student_id = input("Enter the student ID: ")
        student = next((s for s in self.students if s.id == student_id), None)
        if student:
            marks = []
            credits = []
            for course in self.courses:
                mark = course.marks.get(student_id, 0)
                marks.append(mark)
                credits.append(course.credits)
            marks = np.array(marks)
            credits = np.array(credits)
            if np.sum(credits) > 0:
                gpa = np.sum(marks * credits) / np.sum(credits)
                print(f"GPA for {student.name}: {gpa:.2f}")
            else:
                print(f"No credits found for {student.name}")
    
    def sort_students_by_gpa_descending(self):
        student_gpas = []
        for student in self.students:
            marks = []
            credits = []
            for course in self.courses:
                mark = course.marks.get(student.id, 0)
                marks.append(mark)
                credits.append(course.credits)
            marks = np.array(marks)
            credits = np.array(credits)
            if np.sum(credits) > 0:
                gpa = np.sum(marks * credits) / np.sum(credits)
                student_gpas.append((student, gpa))
            sorted_student_gpas = sorted(student_gpas, key=lambda x: x[1], reverse=True)
        for student, gpa in sorted_student_gpas:
            print(f"{student.name}: {gpa:.2f}")


# Main program
school = School()

num_students = int(input("Enter the number of students in the class: "))
for i in range(num_students):
    print(f"\nEnter information for student {i+1}:")
    student = school.input_student_information()
    school.add_student(student)

num_courses = int(input("\nEnter the number of courses: "))
for i in range(num_courses):
    print(f"\nEnter information for course {i+1}:")
    course = school.input_course_information()
    school.add_course(course)

while True:
    print("\nSelect an option:")
    print("1. Input marks for a course")
    print("2. List courses")
    print("3. List students")
    print("4. Show student marks for a course")
    print("5. Calculate GPA for a student")
    print("6. Sort students by GPA (descending)")
    print("7. Quit")
    option = input("Option: ")

    if option == "1":
        school.input_marks_for_course()

    elif option == "2":
        school.list_courses()

    elif option == "3":
        school.list_students()

    elif option == "4":
        school.show_student_marks_for_course()

    elif option == "5":
        school.calculate_gpa_for_student()

    elif option == "6":
        school.sort_students_by_gpa_descending()

    elif option == "7":
        break
