"""For a given number N, find whether it is a factorial number or not. A Factorial number is a number which is equal to the factorial value of other numbers."""
def isfactorial(n):
    isfact = 0
    for j in range(1,n):
        fact = 1
        for i in range(1,j+1):
            fact*=i
        if fact == n:
            isfact = 1
            break

    return isfact

print(isfactorial(120))