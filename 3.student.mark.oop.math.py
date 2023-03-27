import math
import numpy as np
import curses

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

    def input_marks(self, students, screen):
        for student in students:
            screen.addstr(f"Enter mark for {student.name} in {self.name}: ")
            screen.refresh()
            mark = float(screen.getstr().decode())
            mark = math.floor(mark * 10) / 10.0 # round down to 1 decimal
            self.marks[student.id] = mark

    def show_marks(self, students, screen):
        screen.addstr(f"Marks for {self.name} ({self.id}):\n")
        for student in students:
            mark = self.marks.get(student.id, '-')
            screen.addstr(f"{student.name}: {mark}\n")

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Credits: {self.credits}"

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def input_student_information(self, screen):
        screen.addstr("Enter student ID: ")
        screen.refresh()
        student_id = screen.getstr().decode()
        screen.addstr("Enter student name: ")
        screen.refresh()
        student_name = screen.getstr().decode()
        screen.addstr("Enter student date of birth (DD/MM/YYYY): ")
        screen.refresh()
        student_dob = screen.getstr().decode()
        student = Student(student_id, student_name, student_dob)
        return student

    def input_course_information(self, screen):
        screen.addstr("Enter course ID: ")
        screen.refresh()
        course_id = screen.getstr().decode()
        screen.addstr("Enter course name: ")
        screen.refresh()
        course_name = screen.getstr().decode()
        screen.addstr("Enter course credits: ")
        screen.refresh()
        course_credits = float(screen.getstr().decode())
        course = Course(course_id, course_name, course_credits)
        return course

    def list_courses(self, screen):
        screen.addstr("List of courses:\n")
        for course in self.courses:
            screen.addstr(f"ID: {course.id}, Name: {course.name}, Credits: {course.credits}\n")

    def list_students(self, screen):
        screen.addstr("List of students:\n")
        for student in self.students:
            screen.addstr(f"ID: {student.id}, Name: {student.name}, Date of Birth: {student.dob}\n")

    def input_marks_for_course(self, screen):
        self.list_courses(screen)
        screen.addstr("Enter the course ID: ")
        screen.refresh()
        course_id = screen.getstr().decode()
        course = next((c for c in self.courses if c.id == course_id), None)
        if course:
            course.input_marks(self.students, screen)
        else:
            screen.addstr("Invalid course ID\n")

    def show_student_marks_for_course(self, screen):
        self.list_courses(screen)
        course_id = screen.addstr("Enter the course ID: ")
        screen.refresh()
        course_id = screen.getstr().decode()
        course = next((c for c in self.courses if c.id == course_id), None)
        if course and course.marks:
            course.show_marks(self.students, screen)
        else:
            screen.addstr("Invalid course ID or marks not yet input\n")

    def calculate_gpa_for_student(self, screen):
        self.list_students(screen)
        student_id = screen.addstr("Enter the student ID: ")
        screen.refresh()
        student_id = screen.getstr().decode()
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
                screen.addstr(f"GPA for {student.name}: {gpa:.2f}")
            else:
                screen.addstr(f"No credits found for {student.name}")
    
    def sort_students_by_gpa_descending(self, screen):
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
            screen.addstr(f"{student.name}: {gpa:.2f}")

# Main program
school = School()
screen = curses.initscr()
screen.clear()

num_students = screen.addstr("\nEnter the number of students: ")
screen.refresh()
num_students = int(screen.getstr().decode())
for i in range(num_students):
    screen.addstr(f"\nEnter information for student {i+1}:")
    student = school.input_student_information(screen)
    school.add_student(student)

num_courses = screen.addstr("\nEnter the number of courses: ")
screen.refresh()
num_courses = int(screen.getstr().decode())
for i in range(num_courses):
    screen.addstr(f"\nEnter information for course {i+1}:")
    course = school.input_course_information(screen)
    school.add_course(course)

while True:
    screen = curses.initscr()
    screen.clear()
    screen.addstr("\nSelect an option:")
    screen.addstr("\n1. Input marks for a course")
    screen.addstr("\n2. List courses")
    screen.addstr("\n3. List students")
    screen.addstr("\n4. Show student marks for a course")
    screen.addstr("\n5. Calculate GPA for a student")
    screen.addstr("\n6. Sort students by GPA (descending)")
    screen.addstr("\n7. Quit")
    screen.addstr("\nOption: ")
    screen.refresh()
    option = screen.getstr().decode()
    screen.clear()

    if option == "1":
        school.input_marks_for_course(screen)

    elif option == "2":
        school.list_courses(screen)

    elif option == "3":
        school.list_students(screen)

    elif option == "4":
        school.show_student_marks_for_course(screen)

    elif option == "5":
        school.calculate_gpa_for_student(screen)
 
    elif option == "6":
        school.sort_students_by_gpa_descending(screen)

    elif option == "7":
        break

    else:
        screen.addstr("Invalid option")
   
    screen.addstr("\nPress any key to continue...")
    screen.refresh()
    screen.getch()