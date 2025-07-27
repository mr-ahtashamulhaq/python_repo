"""You are given two sets:

cs_students = {"Alice", "Bob", "Charlie", "David"}
math_students = {"Charlie", "Eve", "Frank", "Bob"}

Do the following:
Add "Grace" to cs_students.
Add "Henry" and "Isaac" to math_students.
Remove "Eve" from math_students using.
Randomly remove one student from cs_students. Print who was removed.
Find students enrolled in both courses.
Find students enrolled in only CS.
Find students enrolled in either CS or Math but not both.
Check if all CS students are also Math students.
Check if Math students set is a superset of CS students.
Clear the math_students set and print it."""


cs_students = {"Alice", "Bob", "Charlie", "David"}
math_students = {"Charlie", "Eve", "Frank", "Bob"}

cs_students.add("Grace")
print(cs_students)
math_students.update(["Henry","issac"])
print(math_students)
math_students.remove("Eve")
print(math_students)
temp=cs_students.pop()
print(temp,"is removed from cs_students")
print(cs_students)
print(cs_students.intersection(math_students))
print(cs_students.difference(math_students))
print(cs_students.symmetric_difference(math_students))
if math_students.issuperset(cs_students):
  print("yes it is Superset")
else:
  print("no it is not super set")
math_students.clear()
print(math_students)