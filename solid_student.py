class Student:

    @property #getter
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return "There is no first name listed"
    
    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('The first name must be a string')
        
    @property #getter
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return "There is no last name listed"
        
    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError('The last name must be a string')
        
    @property #getter
    def age(self):
        try:
            return self.__age_name
        except AttributeError:
            return "There is no age listed"
    
    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('The age must be an integer')
        
    @property #getter
    def cohort(self):
        try:
            return self.__cohort
        except AttributeError:
            return "There is no cohort listed"
    
    @cohort.setter
    def cohort(self, new_cohort):
        if type(new_cohort) is int:
            self.__cohort = new_cohort
        else:
            raise TypeError('The cohort must be an integer')
        
    @property #getter
    def full_name(self): #READ-ONLY
        try:
            return f"{self.__first_name} {self.__last_name}"
        except AttributeError:
            return "There is no full name listed"

# Testing try/excepts:
student_one = Student()
student_one.first_name = "Rosie"
# student_one.first_name = 123
student_one.last_name = "Pita"
student_one.age = 2
student_one.cohort = 36
print(student_one.full_name)