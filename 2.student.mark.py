from manage_courses import CourseInfor
from manage_mark import MarkInfor
from manage_students import StudentInfor

student_info = StudentInfor()
course_info = CourseInfor()
mark_info = MarkInfor()
students = []
courses = []
finish = False

print("Welcome To Student Management Program!")
while not finish:
    print("-----------menu----------")
    print("[1] Add Students")
    print("[2] Add Courses")
    print("[3] Show list of students")
    print("[4] Show list of courses")
    print("[5] Add student's marks to a course")
    print("[6] Show marks with a given course")
    print("[0] Exit")
    user_choice = input("Please choose an option: ")
    if user_choice == "1":
        students = student_info.add_student()
    elif user_choice == "2":
        courses = course_info.add_course()
    elif user_choice == "3":
        student_info.present_student()
    elif user_choice == "4":
        course_info.present_course()
    elif user_choice == "5":
        mark_info.add_mark(courses, students)
    elif user_choice == "6":
        mark_info.present_mark(courses, students)
    elif user_choice == "0":
        finish = True
        print("Goodbye!")
    else:
        print(f"{user_choice} is an invalid input!")
