from student import Student

#Inheritence
class InternationalStudent(Student):
    def __init__(self, student_id, name, age, country_of_origin, visa_status):
        super().__init__(student_id, name, age)
        self.country_of_origin = country_of_origin
        self.visa_status = visa_status
    
    def get_country_of_origin(self):
        return self.country_of_origin
    
    def get_visa_status(self):
        return self.visa_status
    
    def display_info(self):
        super().display_info()
        print(f"Country of Origin: {self.get_country_of_origin()}")
        print(f"Visa Status: {self.get_visa_status()}")

inter_student = InternationalStudent(123, "Amani", 33, "Egypt", "st visa")
inter_student.display_info()

