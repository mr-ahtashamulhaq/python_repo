"""Given a tuple arr with distinct elements and an integer x, find the index position of x. Assume to have x in the tuple always. Print the index """

#User function Template for python3

arr = tuple(map(int, input("Enter values ").split()))
x = int(input("Enter x "))

for i in range(len(arr)):
    if x == arr[i]:
        print("index is", i)
        break