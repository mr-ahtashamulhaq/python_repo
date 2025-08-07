"""Design a class as described below.

class: User
instance variable: name(String)
constructor: parameter: none, task: initialize the instance variable to "Default"

Note: The driver's code will print instance variable (name) of your designed class."""
class User:
    def __init__(self):
        self.name = "Ahtasham"

user = User()
print(user.name)