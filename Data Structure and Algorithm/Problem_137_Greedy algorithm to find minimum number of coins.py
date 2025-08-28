"""Given an infinite supply of each denomination of Indian currency { 1, 2, 5, 10 } and a target value n. Find the minimum number of coins and/or notes needed to make the change for Rs n. """
class Solution:
    def findMin(self, n):
       # code here 
        coins = [1,2,5,10]
        right  = 3
        total = 0
        while right >=0:
            if n >= coins[right]:
               n -=coins[right]
               total +=1

            else:
               right -=1 
        return total
        
obj =Solution()
print(obj.findMin(39))
# Output : 6