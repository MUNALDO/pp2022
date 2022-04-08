class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

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



class CourseInfor:
    def __init__(self):
        self.__num = 0
        self.__courses = []

    def num_of_student(self):
        self.__num = int(input("Please enter number of courses: "))
        return self.__num

    def add_course(self):
        for i in range(self.num_of_student()):
            id = input("Please enter the Course-ID: ")
            name = input("Please enter the Course-Name: ")
            course = Course(id, name)
            self.__courses.append(course)
        print(f"{self.__num} courses has been added")
        return self.__courses

    def present_course(self):
        print("{:3} | {:12} | {:22} ".format("No.", "ID", "Name"))
        for i in range(len(self.__courses)):
            print("{:3} | {:12} | {:22} ".format(str(i+1), self.__courses[i].id, self.__courses[i].name))
