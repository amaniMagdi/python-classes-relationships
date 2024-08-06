from logging_student_activity import LoggingStudentActivity
from address import Address
from log import Logger


#Relationships between classes:
#Inheritence: like InternationalStudent inherited from Student
#Interface
#Composition
#Dependency

#Interface
class Student(LoggingStudentActivity):
    def __init__(self, student_id, name, age, address):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.address = address # Composition: Student has an Address

    def get_student_id(self):
        return self.student_id
        
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    # Method to display all attributes
    def display_info(self):
        print(f"Student ID: {self.get_student_id()}")
        print(f"Name: {self.get_name()}")
        print(f"Age: {self.get_age()}")
        print(f"Address: {self.address.get_street()}, {self.address.get_city()}")
    
    def log_student_activity(self, activity_description):
        print(f"[LOG] {self.get_name()} ({self.get_student_id()}): {activity_description}")

    #Dependency
    def log(self, message):
        Logger.log(message)

a = Address("haram", "giza")
s = Student("333", "amani", 33, a)

s.display_info()
s.log("undersatnd class dependency")
