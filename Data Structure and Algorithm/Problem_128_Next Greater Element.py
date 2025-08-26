"""Given an array arr[ ] of integers, the task is to find the next greater element for each element of the array in order of their appearance in the array. Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1"""

class Solution:
    def nextLargerElement(self, arr):

        result = [-1] * len(arr)
        stack = []
        
        for i in range(len(arr)-1,-1,-1):
            
            while stack and arr[i] >= stack[-1]:
                stack.pop()
            
            if stack:
                result[i]  = stack[-1]
            stack.append(arr[i])
        

        return result

obj = Solution()
print(obj.nextLargerElement([41, 88, 58, 69, 93, 42,69, 93, 42, 44, 25, 12, 47]))
# Output   : [88, 93, 69, 93, -1, 69, 93, -1, 44, 47, 47, 47, -1]