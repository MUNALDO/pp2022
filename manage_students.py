class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob

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

    # DOB
    @property
    def dob(self):
        return self.__dob
    @dob.setter
    def dob(self, dob):
        self.__dob = dob

class StudentInfor:
    def __init__(self):
        self.__num = 0
        self.__students = []

    def num_of_student(self):
        self.__num = int(input("Please enter number of students: "))
        return self.__num

    def add_student(self):
        for i in range(self.num_of_student()):
            id = input("Please enter the Student-ID: ")
            name = input("Please enter the Student-Name: ")
            dob = input("Please enter the Student-Date of Birth: ")
            student = Student(id, name, dob)
            self.__students.append(student)
        print(f"{self.__num} students has been added")
        return self.__students

    def present_student(self):
        print("{:3} | {:12} | {:22} | {:22}".format("No.", "ID", "Name", "Date of Birth"))
        for i in range(len(self.__students)):
            print("{:3} | {:12} | {:22} | {:22}".format(str(i+1), self.__students[i].id, self.__students[i].name, self.__students[i].dob))
