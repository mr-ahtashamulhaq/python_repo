"""Given a tuple arr , print "True" if all elements of tuple are different otherwise print "False"."""
#User function Template for python3
arr = tuple(map(int, input("Enter values").split()))
length = len(arr)
flag = True
for i in range (length):
    for j in range(i+1,length):
        if (arr[i] == arr[j]):
            flag = False
            break
if (flag):
    print("True")
else:  
    print("False")  