# Multiple Inheritance: Inheriting from two parents

class Worker:
    def do_work(self):
        print("I am working...")

class Student:
    def study(self):
        print("I am studying...")

class TeachingAssistant(Worker, Student):
    """TA is both a Worker and a Student."""
    def assist(self):
        print("I am assisting the professor.")

if __name__ == "__main__":
    ta = TeachingAssistant()
    
    # Can access methods from both parents
    ta.do_work()  # From Worker
    ta.study()    # From Student
    ta.assist()   # Own method