"""Right Rotate given array by one place"""

class Solution():
    def right_rotate(self,nums):
        n = len(nums)
        temp = nums[n-1]
        for i in range(n-2,-1,-1):
            nums[i+1] = nums[i]
        nums[0] = temp
        return nums
obj = Solution()
nums = [5,3,5,5,6,2]
print(obj.right_rotate(nums))
# Output : [2, 5, 3, 5, 5, 6]
