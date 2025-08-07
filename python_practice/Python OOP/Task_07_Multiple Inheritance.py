"""Implement the following classes to understand multiple inheritance in Python:

Class Name: Student
Attributes:
sid (int) — Student ID.
deptid (int) — Department ID.
Constructor: __init__(self, sid, deptid) — Initializes the sid and deptid attributes.
Method: get_info(self) — Returns a formatted string with the student ID and department ID, eg., "StudentID:101 DepartmentID:42"

Class Name: Faculty
Attributes:
eid (int) — Employee ID.
deptid (int) — Department ID.
Constructor: __init__(self, eid, deptid) — Initializes the eid and deptid attributes.
Method: get_info(self) — Returns a formatted string with the employee ID and department ID, eg., "EmployeeID:555 DepartmentID:42"

Class Name: PhDStudent (Inherits from both Student and Faculty)
Constructor: __init__(self, sid, eid, deptid) — Calls the constructors of Student and Faculty to initialize sid, eid, and deptid.
Method: get_info(self) — Returns a formatted string with the student ID, employee ID and department ID, eg., "Student ID:101 EmployeeID:555 DepartmentID:42"."""

class Student:
    def __init__(self, sid, deptid):
        self.sid = sid
        self.deptid = deptid

    def get_info(self):
        return f"StudentID:{self.sid} DepartmentID:{self.deptid}"

class Faculty:
    def __init__(self, eid, deptid):
        self.eid = eid
        self.deptid = deptid

    def get_info(self):
        return f"EmployeeID:{self.eid} DepartmentID:{self.deptid}"

class PhDStudent(Student, Faculty):
    def __init__(self, sid, eid, deptid):
        Student.__init__(self, sid, deptid)
        Faculty.__init__(self, eid, deptid)

    def get_info(self):
        return f"StudentID:{self.sid} EmployeeID:{self.eid} DepartmentID:{self.deptid}"

p1 = PhDStudent(101, 555, 42)
print(p1.get_info())