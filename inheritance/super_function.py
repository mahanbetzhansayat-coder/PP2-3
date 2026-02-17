# Using super() to extend parent methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age}.")

class Student(Person):
    def __init__(self, name, age, student_id):
        # Call the parent's __init__ method
        super().__init__(name, age)
        self.student_id = student_id
    
    def show_id(self):
        print(f"My Student ID is {self.student_id}.")

if __name__ == "__main__":
    s = Student("Mike", 20, "S12345")
    s.introduce() # From Parent
    s.show_id()   # From Child