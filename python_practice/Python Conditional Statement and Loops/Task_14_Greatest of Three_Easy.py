"""Given three numbers a, b, and c. You need to find which is the greatest of them all."""
def greatest(a,b,c):
    if c<a>b:
        print("a is greatest")
    elif c<b>a:
        print("b is greatest")
    else:
        print("c is greatest")

# greatest(3,5,1)