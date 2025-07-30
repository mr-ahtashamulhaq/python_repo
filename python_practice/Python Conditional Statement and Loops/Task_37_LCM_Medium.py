"""Given two numbers a and b. The task is to find out their LCM."""

def find_lcm(a, b):
    lcm = 1
    i = 2
    while a > 1 or b > 1:
        if a % i == 0 and b % i == 0:
            a //= i
            b //= i
            lcm *= i
        elif a % i == 0:
            a //= i
            lcm *= i
        elif b % i == 0:
            b //= i
            lcm *= i
        else:
            i += 1

    return lcm


a = int(input("Enter a  : "))
b = int(input("Enter b  : "))
print(find_lcm(a,b))
        