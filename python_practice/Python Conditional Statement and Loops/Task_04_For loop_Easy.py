"""You are given a number N, you need to print its multiplication table.

Note: Please go through the range function to understand why it's useful in for loops."""
def multiplicationTable(N):
    #code here 
    for i in range(1,11):
        print(N*i , end=" ")

multiplicationTable(6)