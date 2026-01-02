"""
File: oops_basics.py
Topic: Python OOPS - Basics
Concepts:
- Class
- Object
- __init__
- Instance variables
- Methods
"""
class Student:
    name="dinaah"
    def __init__(self, name=None, age=None):#Make constructor arguments OPTIONAL
        if name is not None:
            self.name = name  #obj attr > class attr
        # instance attribute overrides class attribute
        self.age = age
    def greet(self):
        print("Hello, my name is",self.name)

if __name__ == "__main__":
    s1 = Student("dina",24)
    print(s1.name)
    print(s1.age)
    s1.greet()
"""
>   __init__ runs automatically when object is created
>   Used to initialize object data
"""
print(Student.name)
s2 = Student()
print(s2.name) 