"""given integer number Extract digits and print """
n = 5873

while(n>0):
    last_digit = n%10
    print(last_digit)
    n = n//10

# output
# 3
# 7
# 8
# 5