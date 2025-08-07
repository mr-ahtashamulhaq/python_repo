"""Implement the following classes to understand method overriding in Python:

Class Name: Employee

Attributes:
id (integer)
salary (integer)
Constructor:

__init__(self, id, salary): Initializes the id and salary attributes with the given values.
Methods/Functions:

get_info(self):
Parameters: None
Task: Returns a string formatted as: "EmployeeID:{id} Salary:{salary}".


Class Name: SalesEmployee (Subclass of Employee)

Attributes:
Inherited from Employee: id, salary
New attribute: sales (integer, optional, defaults to 0)
Constructor:

__init__(self, id, salary, sales=0): Calls super().__init__(id, salary) to initialize the inherited attributes, and initializes the sales attribute. The sales parameter defaults to 0 if not provided.
Methods/Functions:

get_info(self):
Parameters: None
Task: Overrides the get_info method to include the sales attribute in the output.
Return Format: "EmployeeID:{id} Salary:{salary} Sales:{sales}"."""

class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary

    def get_info(self):
        return f"EmployeeID:{self.id} Salary:{self.salary}"

class SalesEmployee(Employee):
    def __init__(self, id, salary, sales=0):
        super().__init__(id, salary)
        self.sales = sales

    def get_info(self):

        return f"EmployeeID:{self.id} Salary:{self.salary} Sales:{self.sales}"

e1 = Employee(101, 50000)
print(e1.get_info())  

se1 = SalesEmployee(102, 60000, 150)
print(se1.get_info()) 