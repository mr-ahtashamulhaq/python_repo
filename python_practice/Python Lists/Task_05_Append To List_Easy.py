"""You are given three inputs a, b, c. You need to create a list and append a, b, c to the list and then return that list."""
def appendToList(a,b,c):
    li =[]
    li.append(a)
    li.append(b)
    li.append(c)
    return li

a , b, c = 1,2,3
print(appendToList(a,b,c))