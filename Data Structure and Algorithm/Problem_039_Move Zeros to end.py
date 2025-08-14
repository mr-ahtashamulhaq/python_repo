"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array."""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        if n ==1:
            return

        while(i<n):
            if nums[i] == 0:
                break
            i+=1
        if i == n:
            return
        
        j = i+1
        while(j<n):
            if nums[j] != 0:
                nums[j] , nums[i] = nums[i] , nums[j]
                i +=1
            j+=1
obj = Solution()
nums = [0,1,0,3,12]
obj.moveZeroes(nums)
print(nums)
# Output : [1, 3, 12, 0, 0]