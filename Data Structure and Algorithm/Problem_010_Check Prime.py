"""Given a number n, determine whether it is a prime number or not.
Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself."""
class Solution:
    def isPrime(self, n):
        # code here
        isprime = True
        i = 2
        while(i*i <= n):
            if n%i == 0:
                isprime = False
                break
            i+=1
        return False if n<2 else isprime
        
obj = Solution()
print(obj.isPrime(49))

# output : False