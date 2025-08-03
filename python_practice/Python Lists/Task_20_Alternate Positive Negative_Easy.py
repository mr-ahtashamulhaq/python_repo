"""Given an unsorted array arr containing both positive and negative numbers. Your task is to rearrange the array and convert it into an array of alternate positive and negative numbers without changing the relative order.

Note:
- Resulting array should start with a positive integer (0 will also be considered as a positive integer).
- If any of the positive or negative integers are exhausted, then add the remaining integers in the answer as it is by maintaining the relative order.
- The array may or may not have the equal number of positive and negative integers."""
#User function Template for python3
class Solution:
    def rearrange(self, arr):
        i = 0
        temp = []
        a = arr.copy()
        while a:
            for j in range(len(a)):
                if a[j] >= 0:
                    temp.append(a.pop(j))
                    break
            for k in range(len(a)):
                if a[k] < 0:
                    temp.append(a.pop(k))
                    break
        return temp

a = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
sol = Solution()
result = sol.rearrange(a)
print(result)