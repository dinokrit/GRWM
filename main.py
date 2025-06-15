# 👉 Code for Stage 7 goes here
class Student:
    def __init__(self, name, age, courses, pocket_money, location, salary):
        self.name = name
        self.age = age
        self.courses = courses
        self.money = pocket_money
        self.location = location
        self.salary = salary

#Function => Method

def display_student_info(student):
    print("Name:", student.name)
    print("Age:", student.age)
    print("Courses:", ", ".join(student.courses))
    print("Pocket money:", student.money)
    print("Location:", student.location)
    print("Your salary is", student.salary)
    print("-" * 20)

student1 = Student("Alice", 20, ["Math", "English"], 120, "Wonder Land", 1024)
student2 = Student("Bob", 22, ["Physics", "History"], 300, " Siren Cty", 5000000)
student3 = Student("Nara", 4, ["Math", "Physics"], 1000000, "Frozen island", 20)

display_student_info(student1)
display_student_info(student2)
display_student_info(student3)
# Feel free to modify or expand it