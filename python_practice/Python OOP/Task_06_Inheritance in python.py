"""Class Name: Employee
Attributes:
id (int)
salary (int)
Constructor: __init__(self, id, salary) — Initializes the values to respective variables.

Class Name: SalesEmployee (Subclass of Employee)
Attributes:
Inherited from Employee: id, salary
New attribute: sales (int)
Constructor: __init__(self, id, salary, sales) — Calls super().__init__(id, salary) to initialize id and salary, and initializes the sales attribute."""
class Employee:
    def __init__(self,id,salary):
        self.id = id
        self.salary = salary

class SalesEmployee(Employee):
    def __init__(self,id,salary,sales):
        super().__init__(id,salary)
        self.sales = sales
        
obj = SalesEmployee(1433,50000,10500)
print(obj.id)
print(obj.salary)
print(obj.sales)