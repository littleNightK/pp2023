# Define input functions
def input_student_information():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth (DD/MM/YYYY): ")
    return {"id": student_id, "name": student_name, "dob": student_dob}

def input_course_information():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return {"id": course_id, "name": course_name}

def input_marks_for_course(students, course):
    marks = {}
    for student in students:
        mark = float(input(f"Enter mark for {student['name']} in {course['name']}: "))
        marks[student['id']] = mark
    return marks

# Define listing functions
def list_courses(courses):
    print("List of courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def list_students(students):
    print("List of students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Date of Birth: {student['dob']}")

def show_student_marks_for_course(students, marks, course):
    print(f"Marks for {course['name']} ({course['id']}):")
    for student in students:
        mark = marks.get(student['id'], '-')
        print(f"{student['name']}: {mark}")

# Main program
students = []
num_students = int(input("Enter the number of students in the class: "))
for i in range(num_students):
    print(f"\nEnter information for student {i+1}:")
    student = input_student_information()
    students.append(student)

courses = []
num_courses = int(input("\nEnter the number of courses: "))
for i in range(num_courses):
    print(f"\nEnter information for course {i+1}:")
    course = input_course_information()
    courses.append(course)

while True:
    print("\nSelect an option:")
    print("1. Input marks for a course")
    print("2. List courses")
    print("3. List students")
    print("4. Show student marks for a course")
    print("5. Quit")
    option = input("Option: ")

    if option == "1":
        list_courses(courses)
        course_id = input("Enter the course ID: ")
        course = next((c for c in courses if c["id"] == course_id), None)
        if course:
            marks = input_marks_for_course(students, course)
            course["marks"] = marks
        else:
            print("Invalid course ID")

    elif option == "2":
        list_courses(courses)

    elif option == "3":
        list_students(students)

    elif option == "4":
        list_courses(courses)
        course_id = input("Enter the course ID: ")
        course = next((c for c in courses if c["id"] == course_id), None)
        if course and "marks" in course:
            show_student_marks_for_course(students, course["marks"], course)
        else:
            print("Invalid course ID or marks not yet input")

    elif option == "5":
        break
