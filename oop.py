#!/usr/bin/python3

class student:
    gender = "male"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def out(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}"


student1 = student("james", 22) #instantiation of an object
print(student1.out())
