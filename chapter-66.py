class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Hi i am constructor")


s1 = Student("Shubham", 25)
print(s1.name)
print(s1.age)

s2 = Student("Amit", 22)
print(s2.name)
print(s2.age)