class Student:
    def __init__(self, first_name, last_name, age, courses):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.courses = courses

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def display_info(self):
        print("Name:", self.get_full_name())
        print("Age:", self.age)
        print("Courses:", ", ".join(self.courses))
        print("-" * 20)

student1 = Student("Alice", "Johnson", 20, ["Math", "English"])
student2 = Student("Bob", "Smith", 22, ["Physics", "History"])

student1.display_info()
student2.display_info()