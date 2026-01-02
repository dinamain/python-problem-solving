"""Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average."""

# class Student:
#     def __init__(self, name, m1, m2, m3):
#         self.name=name
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3

#     def average(self):
#         avg=(self.m1+self.m2+self.m3)/3
#         print(f"average of {self.name} is: {avg}")

# if __name__=="__main__":
#     s1=Student("dina", 49, 50, 48)
#     s1.average()

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        total=0
        for val in self.marks:
            total += val
        print("avgerage of ",self.name, "is:",total/len(self.marks))
        # return total/len(self.marks)

s1= Student("dina", [49,50,48])
# avg=s1.get_avg()
s1.get_avg()
# print(f"average of {s1.name} is: {avg}")
s1.name="ironman"
s1.get_avg()