"""You are given a number a and you have to print your answer according to the following:

If the number is divisible by 3, you print "Fizz" (without quotes)
If the number is divisible by 5, you print "Buzz" (without quotes)
If the number is divisible by both 3 and 5, you print "FizzBuzz" (without quotes)
In any other case, you print the number itself"""
#User function Template for python3
def check_divisible(a):
    if a%3 == 0 and a%5==0:
        return "FizzBuzz"
    elif a%3 == 0:
        return "Fizz"
    elif a%5 == 0:
        return "Buzz"
    else:
        return a
    
# print(check_divisible(3))