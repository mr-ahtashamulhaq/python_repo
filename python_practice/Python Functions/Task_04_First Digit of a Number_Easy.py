"""Given a number n, find the first digit of the number."""
def firstDigit(n):
    while(n>9):
        n = n//10
    return n%10

print(firstDigit(630))
