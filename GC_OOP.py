import datetime
class Student:
    stdCount = 0

    def __init__(self, first, last, id, password):
        self.first = first
        self.last = last
        self.id = id
        self.password = password
        Student.stdCount += 1

    def getusername(self):
        return "{}{}{}".format(self.first.lower(),"_",self.last.lower())

    def studentcount(self):
        print "Total student number %d" % Student.stdCount

    def getemail(self):
        return ("{}{}{}{}").format(self.first.lower(),"_",self.last.lower(),"@edu.aua.am")

    def displayStudent(self):
        print "Student Information", "\n","Name: ", self.first, "\n" "Last name: ", self.last, "\n" "Student ID: ", self.id, "\n", "Username: ", Student.getusername(self), "\n", "Email: ", Student.getemail(self)


student1 = Student("Erik","Hajikyan","AB1112322","*******")
Student.displayStudent(student1)
#print "Total student number %d" % Student.stdCount

class Grade():
    min = 0
    max = 100

    def __init__(self,grade):
        self.grade = grade


    def setGrade(self):
        return 0

    def getGrade(self):
        print  self.grade


    def checkIfValidG(self):
        while not int(self.grade) in range(0, 101):
            self.grade = input("Value Error!!Please enter your grade in range(0-100) : ")


grade1 = Grade(94)
#Grade.checkIfValidG(grade1)
#Grade.getGrade(grade1)


class Assigment():

    def __init__(self,name,percent,deadline,description):
        self.name = name
        self.percent = percent
        self.deadline = deadline
        self.description = description

    def checkIfValidP(self):
        while not int(self.percent) in range(0, 101):
            self.percent = input("Value Error!!Too high percentage. Try in range(0-100) : ")



    def getInfo(self):
        time_left = self.deadline - datetime.date.today()
        print "\n","Assigment Information", "\n","Name :", self.name, "\n", "Percent: ", self.percent,"%","\n", "Deadline: ", self.deadline, "\n" "Time Left: ", time_left, "\n","Description: ", self.description


assig1 = Assigment("Project",30,datetime.date(2018,9,10),"Individual project")
assig1.getInfo()
#Assigment.checkIfValidP(assig1)

