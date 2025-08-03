"""You are given two arrays a[] and b[], return the Union of both the arrays in any order.

The Union of two arrays is a collection of all distinct elements present in either of the arrays. If an element appears more than once in one or both arrays, it should be included only once in the result."""

class Solution:    
    def findUnion(self, a, b):
        set1 = set(a)
        set2 = set(b)
        li = list(set1.union(set2))

        return li
obj = Solution()
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
print(obj.findUnion(a,b))