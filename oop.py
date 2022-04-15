#!/usr/bin/python3

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = student("james", 22)
print(student1.name, student1.age)
student2 =student("jane", 30)
print(id(student2))
