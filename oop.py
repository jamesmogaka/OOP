#!/usr/bin/python3

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = student("james", 22) #instantiation of an object
print(student1)
print(student1.name, student1.age)
