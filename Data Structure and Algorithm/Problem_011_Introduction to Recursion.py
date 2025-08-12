"""Print 'Hello World' five Times using recursion"""
def greet(n):
    if n==0:
        return
    print("Hello World")
    greet(n-1)
greet(5)

# OutPut:
# Hello World
# Hello World
# Hello World
# Hello World
# Hello World