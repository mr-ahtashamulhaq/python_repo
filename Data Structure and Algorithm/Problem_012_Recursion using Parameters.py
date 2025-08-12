"""Using recursion with parameters print 1 to n numbers"""
def func(n):
    if 0 == n:
        return

    func(n-1)
    print(n)

func(5)
# output
# 1
# 2
# 3
# 4
# 5