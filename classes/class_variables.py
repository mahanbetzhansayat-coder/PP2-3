# Class Variables vs Instance Variables

class Employee:
    # Class variable (shared by all instances)
    company_name = "TechCorp"
    employee_count = 0
    
    def __init__(self, name, salary):
        # Instance variables (unique to each instance)
        self.name = name
        self.salary = salary
        
        # Increment class variable
        Employee.employee_count += 1

if __name__ == "__main__":
    print(f"Employees at start: {Employee.employee_count}")
    
    emp1 = Employee("Alice", 50000)
    emp2 = Employee("Bob", 60000)
    
    print(f"Employees after hiring: {Employee.employee_count}")
    
    # Accessing class variable
    print(f"{emp1.name} works at {emp1.company_name}")
    print(f"{emp2.name} works at {Employee.company_name}")
    
    # Changing class variable affects all
    Employee.company_name = "MegaTech"
    print(f"{emp1.name} now works at {emp1.company_name}")