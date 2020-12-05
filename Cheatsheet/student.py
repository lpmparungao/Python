class Student:
    def __init__(self, name, age, is_male, major):
        self.name = name
        self.age = age
        self.is_male = is_male
        self.major = major
    def legal_age(self):
        if self.age >= 18:
            return True
        else:
            return False