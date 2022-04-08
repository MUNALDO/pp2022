import math


class Mark:
    def __init__(self, id, name, mark):
        self.__id = id
        self.__name = name
        self.__mark = mark

    # ID
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    # Name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    # Mark
    @property
    def mark(self):
        return self.__mark
    @mark.setter
    def mark(self, mark):
        self.__mark = mark

class MarkInfor:
    def __init__(self):
        self.__marks = {}
        self.__gpa = []

    def select_a_course(self, courses):
        user_select = input("Please enter the course ID: ")
        for i in range(len(courses)):
            if user_select == courses[i].id:
                return courses[i]
        return "No"

    def add_mark(self, courses, students):
        select_course = self.select_a_course(courses)
        if select_course == "No":
            print("Wrong course! Please enter the course ID again! ")
        else:
            mark_list = []
            n = 0
            for i in range(len(students)):
                mark = float(input(f"Enter Student ID: {students[i].id} - Enter Student Name: {students[i].name}\nEnter mark: "))
                student_mark = Mark(students[i].id, students[i].name, math.floor(mark))
                mark_list.append(student_mark)
                n = n + 1
            self.__marks[select_course.id] = mark_list
            print(f"{n} students has been added")
            return self.__marks

    def gpa_mark(self, courses, students):
        select_course = self.select_a_course(courses)
        if select_course == "No":
            print("Wrong course! Please enter the course ID again! ")
        else:
            mark_gpa = []
            n = 0
            for i in range(len(students)):
                gpa_mark = float(input(f"Enter Student ID: {students[i].id} - Enter Student Name: {students[i].name}\n"))


    def present_mark(self, courses, students):
        select_course = self.select_a_course(courses)
        course_mark = self.__marks[select_course.id]
        if select_course == "No":
            print("Wrong course! Please enter the course ID again! ")
        else:
            print(f"{select_course.name} mark sheet")
            print("{:3} | {:12} | {:22} | {:12}".format("No.", "ID", "Name", "Mark"))
            for i in range(len(students)):
                print("{:3} | {:12} | {:22} | {:12} ".format(str(i+1), course_mark[i].id, course_mark[i].name, course_mark[i].mark))
