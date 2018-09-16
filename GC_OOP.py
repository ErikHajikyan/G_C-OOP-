import datetime


class Grade:
    __min = 0
    __max = 100

    def __init__(self, grade):
        self.__grade = grade

    def setGrade(self, grade):
        self.__grade = grade
        if self.__grade in range(0,101):
            pass
        else:
            print "Invalid input"
        #while not int(self.grade) in range(0, 101):
        #    self.__grade = input("Value Error!!Please enter your grade in range(0-100) : ")

    def getGrade(self):
        return self.__grade


class Assigment:

    def __init__(self, name, percent, deadline, description):
        self.name = name
        self.percent = percent
        self.deadline = deadline
        self.description = description


    def checkIfValidP(self):
        if self.percent in range(0,101):
            pass
        else:
            print "Invalid input"
        #while not int(self.percent) in range(0, 101):
            #self.percent = input("Value Error!!Too high percentage. Try in range(0-100) : ")

    def displayInfo(self):
        time_left = self.deadline - datetime.date.today()
        print "\n", "Name :", self.name, "\n",\
            "Percent: ", self.percent,"%","\n", "Deadline: ", self.deadline, \
            "\n" "Time Left: ", time_left, "\n","Description: ", self.description

class AssignmentGrade():

    def __init__(self, course, assignment, grade):
        self.course = course
        self.assignment = assignment
        self.grade = Grade(grade)
        self.state = 0

class Course:
    def __init__(self, name, ID, credit):
        self.name = name
        self.ID = ID
        self.credit = credit
        self.lecturer = ""
        self.assigments = []

    def addAssignment(self, name, percent, deadline, description):
        assignment = Assigment(name, percent, deadline, description)
        self.assigments.append(assignment)

    def displayAssignments(self):
        print "Assigments: "
        for a in self.assigments:
            a.displayInfo()
            print "\n"

    def displayInfo(self):
        print "\n","Course Information: ","\n","Course name: ", self.name, \
            "\n", "Course ID: ", self.ID, "\n","Course Credits: ",self.credit, \
            "\n", "Lecturer: ", self.lecturer.first
        self.displayAssignments()


class User(object):
    stdCount = 0

    def __init__(self, first, last, id, password):
        self.first = first
        self.last = last
        self.id = id
        self.password = password

    def getUsername(self):
        return "{}{}{}".format(self.first.lower(),"_",self.last.lower())

    def getEmail(self):
        return "{}{}{}{}".format(self.first.lower(),"_",self.last.lower(),"@edu.aua.am")

    def fullname(self):
        print "{} {}".format(self.first,self.last)

    def displayInfo(self):
        print "\n""Information", "\n", "Name: ", self.first, "\n" "Last name: ", self.last, "\n"\
        "ID: ", self.id, "\n", "Username: ", User.getUsername(self), \
            "\n", "Email: ", User.getEmail(self)


class Student(User):
    def __init__(self, first, last, id, password):
        super(Student, self).__init__(first,last,id,password)
        self.courses = []
        # Student.stdCount += 1

    # def studentCount(self):
    # print "Total student number %d" % Student.stdCount
    def addCourse(self, course):
          self.courses.append(course)

    def printCourses(self):
        for c in self.courses:
            c.displayInfo()

class Lecturer(User):
    def __init__(self, first, last, id, password):
        User.__init__(self, first, last, id, password)


def main():

    grade1 = Grade(94)
    #Grade.getGrade(grade1)
    #assig1.getInfoA()
    #Assigment.checkIfValidP(assig1)
    course1 = Course("Data Structures and Algoritms", "ENGS115", 3)
    course1.addAssignment("Project", 30, datetime.date(2018, 9, 20), "Individual project")
    course1.addAssignment("Homework", 30, datetime.date(2018, 9, 20), "Homework description")

    lecturer1 = Lecturer("Satenik", "Mnatsakanyan","AB11122122","*******")
    course1.lecturer = lecturer1

    #course2 = Course("Linear Algebra and ODE", "ENGS11", 4)
    #course2.addAssignment("Homework", 10, datetime.date(2018, 9, 14), "Each week")
    #course2.addAssignment("Quiz", 10, datetime.date(2018, 9, 14), "Each 2 weeks")

    #lecturer2 = Lecturer("Gayane", "Ghazaryan", "AB1112333", "*******")
    #course2.lecturer = lecturer2


    #course1.addAssignment(assig1)
    #course1.getInfoG()
    student1 = Student("Erik", "Hajikyan", "AB1112322", "*******")

    #student1.fullname()
    #Student.displayStudent(student1)
    #Lecturer.displayLecturer(lecturer1)
    # print "Total student number %d" % Student.stdCount
    student1.addCourse(course1)
    #student1.addCourse(course2)
    student1.printCourses()

main()
