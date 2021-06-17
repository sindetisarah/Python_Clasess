class Student:
    school="AkiraChix" 
    def __init__(self,first_name,second_name,age):
        self.first_name=first_name
        self.second_name=second_name
        self.age=age
    def speak(self):
        return f"Hello class, My name is {self.first_name}"
    def year_of_birth(self):
        return f"Hello {self.first_name}your born in {2021-self.age}"   
    def greet(self):
        return f"Hello{self.first_name} welcome to {self.school}"
    def initial(self):
        return f"Hello {self.first_name}your initials are {self.first_name[0]}{self.second_name[0]}"