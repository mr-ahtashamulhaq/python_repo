"""You are given a number n, take input of n and print its multiplication table in a single line using for loop till n * 10. """

n = int(input("Enter n : "))

for i in range(1,11):
    print(n*i, end=" ")

