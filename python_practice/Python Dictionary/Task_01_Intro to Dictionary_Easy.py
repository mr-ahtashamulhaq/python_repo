"""Moving on to the question to implement a dictionary. Given a list of strings containing names of students and another list containing marks of corresponding students. The task is to create a dictionary to store marks of students with their names (name will be unique)."""
def create_dict(arr):

    dict = {}
    for name,mark in arr:
        dict[name] = mark
    return dict


arr = [("john",100) ,("ala",200),( "ilia",150), ("sudan",80), ("mercy",300)] 
print(create_dict(arr))