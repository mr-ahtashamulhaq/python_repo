"""You are given a number n. The number n can be negative or positive. If n is negative, print numbers from n to 0 by adding 1 to n in the neg function. If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function."""
def pos(n):
    for i in range(n,-1,-1):
        print(i,end=" ")
    
def neg(n):
    for i in range(n,1):
        print(i,end=" ")


# pos(14)
# print("\n")
# neg(-13)