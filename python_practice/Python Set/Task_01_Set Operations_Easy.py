"""You are given an array arr[] of size n. you need to insert the elements of arr[] into a set and display the results. Also, you need to erase a given element x from the set and print "erased x" if successfully erased, else print "not found"""
def setInsert(arr, n):
    s = set()
    for i in range(n):
        s.add(arr[i])
    return s

def setDisplay(s):
    for val in s:
        print(val, end=' ')
    print()

def setErase(s, x):
    if x in s:
        s.remove(x)
        print(f"erased : {x}")
    else:
        print("not found")

arr = [1, 2, 3, 4, 5, 1, 5, 3]
n = len(arr)
x = 3

s = setInsert(arr, n)
setDisplay(s)
setErase(s, x)
setDisplay(s)