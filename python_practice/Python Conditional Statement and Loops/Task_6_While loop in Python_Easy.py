"""You are given an integer n. You need to return the total number of digits present in n.
You must use a while loop to count the digits manually.
Note: Do not convert the number to a string and do not use any built-in functions like len()."""
def count_digits(n):
    # code here
    count = 0
    if n == 0:
        return 1
    while n > 0:
        n = n // 10
        count += 1
    return count

# print(count_digits(12345))
