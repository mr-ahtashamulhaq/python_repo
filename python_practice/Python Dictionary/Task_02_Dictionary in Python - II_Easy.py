"""The task is to do some operations as described below:
a. i key value: Iserts key and value in the dictionary, and print 'Inserted'.
b. d key: Delete the entry for a given key and print 'Deleted' if the key to be deleted is present, else print '-1'.
c. key: Print marks of a given key in a statement as "Marks of student name is : marks"."""
def insert_dict(query, dict):
    key = query[0]
    dict[key] = query[1]
    print('inserted')
    
def print_dict(key, dic : dict):
    print(dic.items())
    print("printed")

def del_dict(query, dict : dict):
    del dict[query]
    print("deleted")


    
dic = {}
insert_dict(["ali" ,700],dic)
print_dict("ali",dic)
del_dict("ali", dic)
